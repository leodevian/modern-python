---
icon: lucide/house
---

# python-package-template

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
![Latest release](https://img.shields.io/github/v/release/sztal/python-package-template)
[![CI](https://img.shields.io/github/actions/workflow/status/sztal/python-package-template/ci.yaml?branch=main&logo=github&label=CI)](https://github.com/sztal/python-package-template/actions/workflows/ci.yaml)
[![License](https://img.shields.io/github/license/sztal/python-package-template)](https://github.com/sztal/python-package-template/blob/main/LICENSE)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

[Copier](https://copier.readthedocs.io/) template for modern Python packages.

!!! note "Prerequisites"

    This Copier template requires:

    - [Git](https://git-scm.com/) version 2.
    - [Python](https://www.python.org/) 3.10 or more.
    - [Copier](https://copier.readthedocs.io/) version 9.6 or more.
    - [Copier Template-Extensions](https://github.com/copier-org/copier-template-extensions) version 0.3.2 or more.

    To install Git, [download and install it from git-scm.com](https://git-scm.com/downloads).

    To install Python, [download and install it from python.org](https://www.python.org/downloads/),
    or [install uv](https://docs.astral.sh/uv/getting-started/installation/) to install it.

To install Copier and Copier Template-Extensions, use [uv](https://docs.astral.sh/uv/)
or [pipx](https://pipx.pypa.io/):

=== "uv"

    ```bash
    uv tool install copier --with copier-template-extensions
    ```

=== "pipx"

    ```bash
    pipx install copier
    pipx inject copier copier-template-extensions
    ```

## Usage

Run `copier copy` to generate your Python package:

=== "HTTPS"

    ```bash
    copier copy --trust gh:sztal/python-package-template ./path/to/directory
    ```

=== "SSH"

    ```bash
    copier copy --trust git@github.com:sztal/python-package-template ./path/to/directory
    ```

Run `copier update` to update your Python package to the latest version:

```bash
copier update --trust
```
