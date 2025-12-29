# modern-python

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
![Latest release](https://img.shields.io/github/v/release/leodevian/modern-python)
[![CI](https://img.shields.io/github/actions/workflow/status/leodevian/modern-python/ci.yaml?branch=main&logo=github&label=CI)](https://github.com/leodevian/modern-python/actions/workflows/ci.yaml)
[![License](https://img.shields.io/github/license/leodevian/modern-python)](https://github.com/leodevian/modern-python/blob/main/LICENSE)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

[Copier](https://copier.readthedocs.io/) template for modern Python packages.

> [!NOTE]
> This Copier template requires:
>
> - [Git](https://git-scm.com/) version 2.
> - [Python](https://www.python.org/) 3.10 or more.
> - [Copier](https://copier.readthedocs.io/) version 9.6 or more.
> - [Copier Template-Extensions](https://github.com/copier-org/copier-template-extensions) version 0.3.2 or more.
>
> To install Git, [download and install it from git-scm.com](https://git-scm.com/downloads).
>
> To install Python, [download and install it from python.org](https://www.python.org/downloads/),
> or [install uv](https://docs.astral.sh/uv/getting-started/installation/) to install it.

To install Copier and Copier Template-Extensions, use [uv](https://docs.astral.sh/uv/)
or [pipx](https://pipx.pypa.io/):

```bash
# Use uv.
uv tool install copier --with copier-template-extensions
# Use pipx.
pipx install copier
pipx inject copier copier-template-extensions
```

## Usage

Run `copier copy` to generate your Python package:

```bash
# Use HTTPS.
copier copy --trust gh:leodevian/modern-python ./path/to/directory
# Use SSH.
copier copy --trust git@github.com:leodevian/modern-python ./path/to/directory
```

Run `copier update` to update your Python package to the latest version:

```bash
copier update --trust
```
