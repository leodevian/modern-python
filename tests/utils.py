"""This module contains helper functions for tests."""

from __future__ import annotations

import os
import shutil
import stat
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

    from _typeshed import StrOrBytesPath, StrPath


def remove_read_only(func: Callable[..., Any], path: str, _: Any) -> None:
    """Clear the read-only bit and reattempt the removal.

    See https://docs.python.org/3/library/shutil.html#rmtree-example.
    """
    os.chmod(path, stat.S_IWRITE)  # noqa: PTH101
    func(path)


def force_remove_directory(dir_path: StrOrBytesPath) -> None:
    """Force remove a directory."""
    if sys.version_info < (3, 12):
        shutil.rmtree(dir_path, onerror=remove_read_only)
    else:
        shutil.rmtree(dir_path, onexc=remove_read_only)


def make_directory(dir_path: StrPath, dir_name: str) -> Path:
    """Make a new directory in the given directory."""
    new_dir_path = Path(dir_path, dir_name)
    new_dir_path.mkdir(parents=True, exist_ok=True)
    return new_dir_path
