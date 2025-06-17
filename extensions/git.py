"""An extension to provide Git user information."""

from __future__ import annotations

import subprocess
from typing import TYPE_CHECKING

from jinja2.ext import Extension

if TYPE_CHECKING:
    from jinja2.environment import Environment


def git_user_name(user_name: str) -> str:
    """Return the Git username."""
    return (
        subprocess.check_output(
            ("git", "config", "user.name"),
            encoding="utf-8",
        ).rstrip()
        or user_name
    )


def git_user_email(user_email: str) -> str:
    """Return the Git user email."""
    return (
        subprocess.check_output(
            ("git", "config", "user.email"),
            encoding="utf-8",
        ).rstrip()
        or user_email
    )


class GitExtension(Extension):
    """An extension to provide Git user information."""

    def __init__(self, environment: Environment) -> None:
        """Initialize the extension."""
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email
