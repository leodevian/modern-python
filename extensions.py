"""This module contains custom extensions and Copier hooks."""

from __future__ import annotations

import re
import subprocess
import unicodedata
from datetime import date
from typing import TYPE_CHECKING, Any

from copier import Phase
from copier_templates_extensions import ContextHook
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


def slugify(string: str, separator: str = "-") -> str:
    """Create a slug from the given string."""
    string = (
        unicodedata.normalize("NFKD", string).encode("ascii", "ignore").decode("ascii")
    )
    string = re.sub(r"[^\w\s-]", "", string.lower())
    return re.sub(r"[-_\s]+", separator, string).strip("-_")


class GitExtension(Extension):
    """An extension to provide Git user information."""

    def __init__(self, environment: Environment) -> None:
        """Initialize an extension."""
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email


class ContextUpdater(ContextHook):
    """A hook to update Copier context."""

    def hook(self, context: dict[str, Any]) -> None:  # type: ignore[override]
        """Update Copier context."""
        if context["_copier_phase"] != Phase.PROMPT:
            # Update distribution name and package name.
            project_name = context["project_name"]
            distribution_name = slugify(project_name)
            context["distribution_name"] = distribution_name
            context["package_name"] = slugify(project_name, separator="_")

            # Update GitHub URLs.
            github_user = context["github_user"]
            repository_path = f"{github_user}/{distribution_name}"
            context["repository_path"] = repository_path
            context["repository_url"] = f"https://github.com/{repository_path}"
            context["documentation_url"] = (
                f"https://{github_user}.github.io/{distribution_name}/"
            )

            # Update ownership.
            context["copyright_owner"] = context["user_name"]
            context["copyright_year"] = date.today().year

            # Update dependencies.
            context["dependencies"] = []

            if context.get("cli") == "click":
                context["dependencies"].append("click>=8.1.8")

            elif context.get("cli") == "typer":
                context["dependencies"].append("typer>=0.15.4")
