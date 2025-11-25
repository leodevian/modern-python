# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "towncrier>=24.8",
#   "uv>=0.8.6",
# ]
# ///
"""Release a new version."""

# ruff: noqa: S603, S607

from __future__ import annotations

import argparse
import json
import subprocess
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def create_parser() -> argparse.ArgumentParser:
    """Return the argument parser."""
    parser = argparse.ArgumentParser(
        description="release a new version",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="do not update the origin remote and reset the local repository",
    )
    parser.add_argument(
        "version_args",
        nargs=argparse.PARSER,
        help="provide arguments or options to pass to the uv version command",
    )
    return parser


def check_repository() -> None:
    """Check whether the local repository is dirty or clean."""
    subprocess.check_call(["git", "diff", "--exit-code"])


def update_version(args: Sequence[str] | None) -> str:
    """Update and return the version."""
    # Update the version.
    version_json = subprocess.check_output(
        [
            "uv",
            "version",
            "--no-sync",
            "--output-format",
            "json",
            *args,
        ],
    )
    version = json.loads(version_json)
    return version["version"]


def get_current_branch() -> str:
    """Get the current Git branch."""
    return subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        text=True,
    ).rstrip()


def get_release_notes(version: str) -> str:
    """Return the release notes."""
    release_notes = subprocess.check_output(
        ["towncrier", "build", "--version", version, "--draft"],
        stderr=subprocess.DEVNULL,
        text=True,
    ).rstrip()
    release_notes = "".join(release_notes.splitlines(keepends=True)[1:])
    release_notes = release_notes.strip()
    return f"## Release notes\n\n{release_notes}"


def update_changelog(version: str) -> None:
    """Update the changelog."""
    subprocess.check_call(["towncrier", "build", "--version", version, "--yes"])


def create_release_tag(version: str) -> str:
    """Create and return the release tag."""
    release_tag = f"v{version}"
    message = f"bump version to {version}"
    # Make sure to create an annotated tag.
    subprocess.check_call(
        ["git", "tag", "--annotate", release_tag, "--message", message],
    )
    return release_tag


def create_release(release_tag: str, release_notes: str) -> None:
    """Create the GitHub release with release notes."""
    subprocess.check_call(
        ["gh", "release", "create", release_tag, "--notes", release_notes]
    )


def main(argv: Sequence[str] | None = None) -> int:
    """Release a new version."""
    # Parse command-line arguments.
    parser = create_parser()
    args = parser.parse_args(argv)

    # Check whether the local repository is dirty or clean.
    check_repository()

    # Run the uv version command to update the version.
    version = update_version(args.version_args)

    release_branch = f"release/{version}"
    base_branch = get_current_branch()

    try:
        # Create the release branch and switch to it.
        subprocess.check_call(["git", "switch", "--create", release_branch])

        # Update the changelog.
        release_notes = get_release_notes(version)
        update_changelog(version)

        # Add all changes as the local repository was clean.
        subprocess.check_call(["git", "add", "--all", "."])

        # Commit changes.
        message = f"chore: prepare release {version}"
        subprocess.check_call(["git", "commit", "--no-verify", "--message", message])

        # Create the release tag.
        release_tag = create_release_tag(version)

        if args.dry_run:
            # Remove the release tag.
            subprocess.check_call(["git", "tag", "--delete", release_tag])
            return 0

        # Push the release branch and the release tag to the origin remote.
        # The local release branch is pushed to the remote main branch.
        subprocess.check_call(
            ["git", "push", "--atomic", "origin", f"{release_branch}:main", release_tag]
        )

        # Create the GitHub release.
        create_release(release_tag, release_notes)

    finally:
        # Switch back to the base Git branch.
        subprocess.check_call(["git", "checkout", base_branch])
        # Remove the release branch.
        subprocess.check_call(["git", "branch", "--delete", "--force", release_branch])

    # Fetch all changes from the remote main branch.
    subprocess.check_call(["git", "fetch", "origin", "main"])
    # Switch to the main branch.
    subprocess.check_call(["git", "switch", "main"])
    # Pull changes from the remote main branch.
    subprocess.check_call(["git", "pull", "--ff-only", "origin", "main"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
