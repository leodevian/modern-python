# modern-python

[Copier](https://copier.readthedocs.io/en/stable/) template for modern Python packages.

- GitHub repository: <https://github.com/leodevian/modern-python>
- License: MIT

## Requirements

This Copier template requires:

- [Git](https://git-scm.com/) version 2.
- [Python](https://www.python.org/) 3.9 or more.
- [Copier](https://copier.readthedocs.io/en/stable/) version 9.6 or more.
- [Copier Template-Extensions](https://github.com/copier-org/copier-template-extensions) version 0.3.2 or more.

To install Git, [download and install it from the official website](https://git-scm.com/downloads).

To install Python, [download and install it from the official website](https://www.python.org/downloads/),
or [install uv](https://docs.astral.sh/uv/getting-started/installation/) to install it.

To install Copier and Copier Template-Extensions, use [uv](https://docs.astral.sh/uv/):

```bash
uv tool install copier --with copier-template-extensions
```

## Quick usage

Run `copier copy` to generate your Python package:

```bash
copier copy --trust gh:leodevian/modern-python $PROJECT_DIR
```
