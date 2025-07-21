"""An extension to provide Git user information."""

from __future__ import annotations

import subprocess
from typing import TYPE_CHECKING

from jinja2.ext import Extension

if TYPE_CHECKING:
    from jinja2.environment import Environment


def git_user_name() -> str:
    """Return the username from Git user information."""
    try:
        user_name = subprocess.check_output(
            ("git", "config", "user.name"),
            encoding="utf-8",
        ).rstrip()

    except subprocess.CalledProcessError:
        user_name = ""

    return user_name


def git_user_email() -> str:
    """Return the email address from Git user information."""
    try:
        user_email = subprocess.check_output(
            ("git", "config", "user.email"),
            encoding="utf-8",
        ).rstrip()

    except subprocess.CalledProcessError:
        user_email = ""

    return user_email


class GitExtension(Extension):
    """An extension to provide Git user information."""

    def __init__(self, environment: Environment) -> None:
        """Initialize the extension."""
        super().__init__(environment)
        environment.globals["git_user_name"] = git_user_name()
        environment.globals["git_user_email"] = git_user_email()
