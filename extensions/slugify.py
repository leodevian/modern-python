"""An extension to create slugs from strings."""

from __future__ import annotations

import re
import unicodedata
from typing import TYPE_CHECKING

from jinja2.ext import Extension

if TYPE_CHECKING:
    from jinja2.environment import Environment


def slugify(string: str, separator: str = "-") -> str:
    """Create a slug from the given string."""
    string = (
        unicodedata.normalize("NFKD", string).encode("ascii", "ignore").decode("ascii")
    )
    string = re.sub(r"[^\w\s-]", "", string.lower())
    return re.sub(r"[-_\s]+", separator, string).strip("-_")


class SlugifyExtension(Extension):
    """An extension to create slugs from strings."""

    def __init__(self, environment: Environment) -> None:
        """Initialize the extension."""
        super().__init__(environment)
        environment.filters["slugify"] = slugify
