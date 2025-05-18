# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "packaging>=24.2",
#   "towncrier>=24.8",
# ]
# ///
"""Automation for releases."""

# ruff: noqa: S603, T201

from __future__ import annotations

import argparse
import subprocess
import sys
from functools import partial
from typing import TYPE_CHECKING

from packaging.version import Version

if TYPE_CHECKING:
    from collections.abc import Sequence

print_error = partial(print, file=sys.stderr)

run = partial(
    subprocess.check_call,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)


def main(argv: Sequence[str] | None = None) -> int:  # noqa: PLR0911, PLR0915
    """Prepare a new release."""
    # Parse command-line arguments.
    parser = argparse.ArgumentParser(description="prepare a new release")
    parser.add_argument(
        "--version",
        type=Version,
        required=True,
        help="provide the release version",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="perform a dry run",
    )
    args = parser.parse_args(argv)

    # Get the public portion of the version.
    version = args.version.public

    # Check if the Git repository is dirty.
    try:
        run(("git", "diff", "--quiet"))

    except subprocess.CalledProcessError:
        print_error("The Git repository is dirty.")
        return 1

    # Get the name of the base branch.
    base_branch = subprocess.check_output(
        ("git", "rev-parse", "--abbrev-ref", "HEAD"),
        encoding="utf-8",
    ).rstrip()

    # Create the release branch.
    release_branch = f"release/{version}"

    try:
        run(("git", "branch", release_branch))

    except subprocess.CalledProcessError:
        print_error(f"The release branch already exists: {release_branch!r}.")
        return 1

    print(f"Created release branch {release_branch!r}.")

    # Switch to the release branch.
    run(("git", "checkout", release_branch))

    print(f"Switched from branch {base_branch!r} to release branch {release_branch!r}.")

    # Build the changelog.
    try:
        run(("towncrier", "build", "--yes", "--version", version))

    except subprocess.CalledProcessError:
        run(("git", "checkout", base_branch))
        run(("git", "branch", "-D", release_branch))
        print_error("An error occurred while building the changelog.")
        print_error(
            f"Removed release branch {release_branch!r} "
            f"and switched back to {base_branch!r}."
        )
        return 1

    # Commit changes.
    run(("git", "add", "-A", ":/changelog.d/*", "CHANGELOG.md"))
    run(("git", "commit", "-m", f"chore: prepare release {version}", "--no-verify"))

    print(f"Committed changes on branch {release_branch!r}.")

    # Create the release tag.
    release_tag = f"v{version}"

    try:
        run(("git", "tag", "-a", release_tag, "-m", f"bump version to {version}"))

    except subprocess.CalledProcessError:
        run(("git", "checkout", base_branch))
        run(("git", "branch", "-D", release_branch))
        print_error(f"The release tag already exists: {release_tag!r}.")
        print_error(
            f"Removed release branch {release_branch!r} "
            f"and switched back to {base_branch!r}."
        )
        return 1

    # Exit on dry run.
    if args.dry_run:
        print("Dry run success!")
        run(("git", "checkout", base_branch))
        run(("git", "branch", "-D", release_branch))
        print(
            f"Removed release branch {release_branch!r} "
            f"and switched back to {base_branch!r}."
        )
        return 0

    # Push changes to the remote repository and push the release tag.
    try:
        run(("git", "push", "origin", f"{release_branch}:main", "--follow-tags"))

    except subprocess.CalledProcessError:
        run(("git", "checkout", base_branch))
        run(("git", "branch", "-D", release_branch))
        print_error("An error occurred while pushing changes.")
        print_error(
            f"Removed release branch {release_branch!r} "
            f"and switched back to {base_branch!r}."
        )
        return 1

    print(f"Pushed changes from {release_branch!r} to 'origin/main'.")

    # Remove the release branch and switch to the main branch.
    run(("git", "checkout", "main"))
    run(("git", "branch", "-D", release_branch))
    run(("git", "fetch"))
    run(("git", "reset", "--hard", "origin/main"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
