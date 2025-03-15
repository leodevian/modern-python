# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "click>=8.1.8",
#   "packaging>=24.2",
#   "towncrier>=24.8",
# ]
# ///
"""Prepare a new release."""

from __future__ import annotations

import subprocess

import click
from packaging.version import Version


@click.command()
@click.argument("release", type=Version)
@click.option("--dry-run", is_flag=True, help="Perform a dry run.")
def prepare_release(
    release: Version,
    *,
    dry_run: bool,
) -> None:
    """Prepare a new release."""
    version = release.public

    subprocess.check_call(("git", "diff", "--quiet"))

    base_branch = subprocess.check_output(
        ("git", "rev-parse", "--abbrev-ref", "HEAD"),
        encoding="utf-8",
    ).rstrip()

    release_branch = f"release/{version}"
    release_tag = f"v{version}"

    subprocess.check_call(("git", "checkout", "-b", release_branch))

    try:
        subprocess.check_call(("towncrier", "build", "--yes", "--version", version))
        subprocess.check_call(("git", "add", "-A", ":/changelog.d/*", ":/CHANGELOG.md"))
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
            ("git", "tag", "-a", release_tag, "-m", f"bump version to {version}")
        )

    except subprocess.CalledProcessError:
        subprocess.check_call(("git", "checkout", base_branch))
        subprocess.check_call(("git", "branch", "-D", release_branch))
        raise

    if dry_run:
        return

    try:
        subprocess.check_call(
            ("git", "push", "origin", f"{release_branch}:main", "--follow-tags")
        )

    finally:
        subprocess.check_call(("git", "checkout", "main"))
        subprocess.check_call(("git", "branch", "-D", release_branch))
        subprocess.check_call(("git", "fetch"))
        subprocess.check_call(("git", "reset", "--hard", "origin/main"))


if __name__ == "__main__":
    prepare_release()
