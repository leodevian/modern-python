"""This module contains Copier context hooks."""

from __future__ import annotations

import re
import unicodedata
from datetime import date
from typing import Any

from copier import Phase
from copier_templates_extensions import ContextHook


def slugify(string: str, separator: str = "-") -> str:
    """Create a slug from the given string."""
    string = (
        unicodedata.normalize("NFKD", string).encode("ascii", "ignore").decode("ascii")
    )
    string = re.sub(r"[^\w\s-]", "", string.lower())
    return re.sub(r"[-_\s]+", separator, string).strip("-_")


class ContextUpdater(ContextHook):
    """A hook to update Copier context."""

    def hook(self, context: dict[str, Any]) -> None:  # type: ignore[override]
        """Update Copier context."""
        if context["_copier_phase"] == Phase.PROMPT:
            return

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
        context["copyright_year"] = date.today().year  # noqa: DTZ011

        # Update dependencies.
        context["dependencies"] = []

        if context.get("cli") == "click":
            context["dependencies"].append("click>=8.2")

        elif context.get("cli") == "typer":
            context["dependencies"].append("typer>=0.15.4")
