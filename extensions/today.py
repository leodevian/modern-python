"""An extension to add today's date to globals."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from jinja2.ext import Extension

if TYPE_CHECKING:
    from jinja2.environment import Environment


class TodayExtension(Extension):
    """An extension to add today's date to globals."""

    def __init__(self, environment: Environment) -> None:
        """Initialize the extension."""
        super().__init__(environment)
        environment.globals["today"] = date.today()  # noqa: DTZ011
