# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "packaging",
#     "towncrier",
# ]
# ///
"""Prepare a new release."""

from __future__ import annotations

import argparse
import subprocess
from typing import TYPE_CHECKING

from packaging.version import Version

if TYPE_CHECKING:
    from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> None:
    """Prepare a new release.

    Args:
        argv: Arguments passed from the command-line.
    """
    parser = argparse.ArgumentParser(description="prepare a new release")
    parser.add_argument("--version", type=Version, required=True, help="target version")
    parser.add_argument("--dry-run", action="store_true", help="perform dry run")
    args = parser.parse_args(argv)

    version = args.version.public

    subprocess.check_call(("git", "diff", "--quiet"))

    base_branch = subprocess.check_output(
        ("git", "rev-parse", "--abbrev-ref", "HEAD"),
        encoding="utf-8",
    ).rstrip()

    release_branch = f"release/{version}"
    release_tag = f"v{version}"

    subprocess.check_call(("git", "checkout", "-b", release_branch))

    try:
        release_notes = subprocess.check_output(
            ("towncrier", "build", "--draft", "--version", version),
            encoding="utf-8",
        )
        subprocess.check_call(("towncrier", "build", "--yes", "--version", version))
        subprocess.check_call(("git", "add", "-A", ":/CHANGELOG.md", ":/changelog.d"))
        subprocess.check_call(
            (
                "git",
                "commit",
                "-m",
                f"chore: prepare release {version}",
                "--no-verify",
            ),
        )
        subprocess.check_call(
            (
                "git",
                "tag",
                "-a",
                release_tag,
                "-m",
                release_notes,
                "--cleanup",
                "whitespace",
            )
        )

    except subprocess.CalledProcessError:
        subprocess.check_call(("git", "checkout", base_branch))
        subprocess.check_call(("git", "branch", "-D", release_branch))
        raise

    if args.dry_run:
        return

    try:
        subprocess.check_call(
            ("git", "push", "--follow-tags", f"{release_branch}:main")
        )

    finally:
        subprocess.check_call(("git", "checkout", "main"))
        subprocess.check_call(("git", "branch", "-D", release_branch))
        subprocess.check_call(("git", "fetch"))
        subprocess.check_call(("git", "reset", "--hard", "origin/main"))


if __name__ == "__main__":
    main()
