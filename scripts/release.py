# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "towncrier>=24.8",
#   "uv>=0.8.6",
# ]
# ///
"""Make a release."""

# ruff: noqa: S603, T201

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from contextlib import contextmanager
from functools import partial
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator, Sequence

print_error = partial(print, file=sys.stderr)

run = partial(
    subprocess.check_call,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(description="make a release")
    parser.add_argument(
        "--bump",
        required=True,
        help="update the version using the given semantics",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="do not push changes and reset the repository",
    )
    return parser


def check_repository() -> None:
    """Check whether the repository is dirty."""
    try:
        run(("git", "diff", "--quiet"))

    except subprocess.CalledProcessError:
        print_error("The Git repository is dirty.")
        raise SystemExit(1) from None


def bump_version(bump: str) -> str:
    """Bump the version and return the new version."""
    try:
        version_json = subprocess.check_output(
            (
                "uv",
                "version",
                "--no-sync",
                "--output-format",
                "json",
                "--bump",
                bump,
            )
        )

    except subprocess.CalledProcessError:
        print_error("An error occurred while bumping the version.")
        raise SystemExit(1) from None

    version = json.loads(version_json)
    return version["version"]


@contextmanager
def switch_to_branch(branch: str) -> Generator[None]:
    """Create a new branch and switch to it.

    It is removed on exit.
    """
    base_branch = subprocess.check_output(
        ("git", "rev-parse", "--abbrev-ref", "HEAD"),
        text=True,
    ).rstrip()

    try:
        run(("git", "branch", branch))

    except subprocess.CalledProcessError:
        print_error(f"The branch already exists: {branch!r}.")
        raise SystemExit(1) from None

    print(f"Created new branch {branch!r}.")

    try:
        run(("git", "checkout", branch))
        print(f"Switched from branch {base_branch!r} to branch {branch!r}.")
        yield

    finally:
        run(("git", "checkout", base_branch))
        run(("git", "branch", "-D", branch))
        print(f"Removed branch {branch!r} and switched back to {base_branch!r}.")


def build_changelog(version: str) -> None:
    """Build the changelog."""
    try:
        run(("towncrier", "build", "--yes", "--version", version))

    except subprocess.CalledProcessError:
        print_error("An error occurred while building the changelog.")
        raise SystemExit(1) from None


def create_release_tag(version: str) -> str:
    """Create the release tag."""
    release_tag = f"v{version}"
    message = f"bump version to {version}"

    try:
        run(("git", "tag", "-a", release_tag, "-m", message))

    except subprocess.CalledProcessError:
        print_error(f"The release tag already exists: {release_tag!r}.")
        raise SystemExit(1) from None

    print(f"Created release tag {release_tag!r}.")
    return release_tag


def push_changes(branch: str, remote_branch: str = "main") -> None:
    """Push the changes to the target branch."""
    run(("git", "push", "origin", f"{branch}:{remote_branch}", "--follow-tags"))
    print(f"Pushed changes from {branch!r} to 'origin/{remote_branch}'.")


def main(argv: Sequence[str] | None = None) -> None:
    """Prepare a new release."""
    parser = create_parser()
    args = parser.parse_args(argv)

    check_repository()

    version = bump_version(args.bump)

    release_branch = f"release/{version}"

    with switch_to_branch(release_branch):
        build_changelog(version)

        # Commit changes.
        run(("git", "add", ":/pyproject.toml", ":/uv.lock"))
        run(("git", "add", "-A", ":/changelog.d/*", ":/CHANGELOG.md"))
        message = f"chore: prepare release {version}"
        run(("git", "commit", "--no-verify", "-m", message))
        print(f"Committed changes on branch {release_branch!r}.")

        release_tag = create_release_tag(version)

        # Exit on dry run.
        if args.dry_run:
            print("Dry run success!")
            run(("git", "tag", "-d", release_tag))
            print(f"Removed release tag {release_tag!r}.")
            return

        push_changes(release_branch, "main")

    # Switch to the main branch.
    run(("git", "checkout", "main"))
    run(("git", "fetch"))
    run(("git", "reset", "--hard", "origin/main"))


if __name__ == "__main__":
    raise SystemExit(main())
