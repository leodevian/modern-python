# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This project uses [*towncrier*](https://towncrier.readthedocs.io/).

<!-- towncrier release notes start -->

## [4.6.0](https://github.com/leodevian/modern-python/tree/v4.6.0)

### Changed

- Update pre-commit hooks.


## [4.5.0](https://github.com/leodevian/modern-python/tree/v4.5.0)

### Changed

- Add `.gitignore` to the package root to ignore `VERSION.txt`.
- Bump the lower version boundary for Coverage.py to 7.11.0.
- Edit docstring in `scripts/release.py`.

### Fixed

- Fix command in Nox session `typecheck`.


## [4.4.0](https://github.com/leodevian/modern-python/tree/v4.4.0)

### Changed

- Rename dependency group `tests` into `test`.


## [4.3.0](https://github.com/leodevian/modern-python/tree/v4.3.0)

### Added

- Run tests under Python 3.14.

### Changed

- Drop support for Python 3.9 and add support for Python 3.14.


## [4.2.0](https://github.com/leodevian/modern-python/tree/v4.2.0)

### Changed

- Make Nox raise an error on missing interpreters in CI.
- Use the default cache dependency glob for `astral-sh/setup-uv`.


## [4.1.3](https://github.com/leodevian/modern-python/tree/v4.1.3)

### Fixed

- Remove an unused `noqa` directive in `scripts/release.py` when the project version is provided dynamically.


## [4.1.2](https://github.com/leodevian/modern-python/tree/v4.1.2)

### Fixed

- Remove an unused import in `scripts/release.py` when the project version is provided dynamically.


## [4.1.1](https://github.com/leodevian/modern-python/tree/v4.1.1)

### Fixed

- Add the project description to `README.md`.


## [4.1.0](https://github.com/leodevian/modern-python/tree/v4.1.0)

### Changed

- Rename the `print_error` function to `print_err` in `scripts/release.py`.


## [4.0.0](https://github.com/leodevian/modern-python/tree/v4.0.0)

### Security

- Set a lower version boundary for uv to create Nox sessions and tox environments.

### Removed

- Stop checking package distributions.

### Changed

- Bump the lower version boundary for uv-build to 0.8.6.
- Change the default build backend to uv-build.
- Create a function to install dependencies with `uv sync` in `noxfile.py`.
- In Nox sessions, set `COVERAGE_FILE` if it is not set yet.
- Refactor typechecking tasks into one task.
- Rename local variable in `scripts/release.py`.
- Use command-line options to install dependency groups.

### Fixed

- Install the package in editable mode to build the documentation.


## [3.1.1](https://github.com/leodevian/modern-python/tree/v3.1.1)

### Changed

- Sort version flags for Cyclopts CLIs.


## [3.1.0](https://github.com/leodevian/modern-python/tree/v3.1.0)

### Changed

- Add minor changes to `README.md` and update the documentation homepage with the contents of `README.md`.
- Update the release script `scripts/release.py`.


## [3.0.0](https://github.com/leodevian/modern-python/tree/v3.0.0)

### Added

- Add badges to `README.md`.

### Changed

- Allow Ruff to add `from __future__ import annotations` to enable the deferred evaluation of annotations.
- Import the extension loader from `copier_template_extensions` instead of `copier_templates_extensions`.


## [2.4.0](https://github.com/leodevian/modern-python/tree/v2.4.0)

### Added

- Add the description to `README.md`.

### Changed

- Shorten URLs.


## [2.3.0](https://github.com/leodevian/modern-python/tree/v2.3.0)

### Added

- Add badges to `README.md`.
- Add badges to the documentation homepage.

### Changed

- Bump actions/checkout from 4 to 5.
- Bump actions/download-artifact from 4 to 5.
- Bump astral-sh/setup-uv from 5 to 6.
- Update pre-commit hooks.


## [2.2.0](https://github.com/leodevian/modern-python/tree/v2.2.0)

### Changed

- Capitalize `Project-URL` labels in `pyproject.toml`.


## [2.1.0](https://github.com/leodevian/modern-python/tree/v2.1.0)

### Security

- Bump the lower version boundary for uv to 0.8.6.

### Added

- Add license and requirements to the documentation.
- Start a new dynamic coverage context for each test function.

### Changed

- Edit descriptions in `tox.toml` and `noxfile.py`.
- Update pre-commit hooks to their latest versions.


## [2.0.0](https://github.com/leodevian/modern-python/tree/v2.0.0)

### Added

- Add an option to use Cyclopts.

### Changed

- Bump the lower version boundary for Typer to 0.16.
- Require Copier Template-Extensions to generate projects.
- Rewrite the quick setup and usage guide.
- Sort CLI options in source code and tests.


## [1.5.0](https://github.com/leodevian/modern-python/tree/v1.5.0)

### Changed

- Add Git user information to globals during generation.
- Stop creating reports for test runs.
- Stop using pytest-cov and require Coverage.py 7.10 or more.

### Fixed

- Always install uv to run Nox sessions.


## [1.4.0](https://github.com/leodevian/modern-python/tree/v1.4.0)

### Added

- Add `towncrier` to the `release` dependency group.

### Changed

- Use `pre-commit` instead of `pre-commit-uv`.


## [1.3.0](https://github.com/leodevian/modern-python/tree/v1.3.0)

### Changed

- Drop the legacy alias for Ruff's lint hook.
- Manage `scripts/release.py` using inline metadata.
- Remove the upper version boundary for uv-build.
- Update pre-commit hooks.


## [1.2.1](https://github.com/leodevian/modern-python/tree/v1.2.1)

### Fixed

- Prevent coverage warnings for unclosed SQLite connections being raised as errors.


## [1.2.0](https://github.com/leodevian/modern-python/tree/v1.2.0)

### Added

- Print log records with `INFO` or higher level to the console during testing.

### Changed

- Stop setting the log level to `INFO` during testing.


## [1.1.1](https://github.com/leodevian/modern-python/tree/v1.1.1)

### Fixed

- Fix the extension of the version test.


## [1.1.0](https://github.com/leodevian/modern-python/tree/v1.1.0)

### Changed

- Add hatch-vcs to default Hatch plugins.
- In pytest options, write the minimum log message level that should be captured for logging capture in uppercase.
- Parse the target version as an argument in `scripts/release.py`.
- Remove `mkdocs.yaml` from the watch list.
- Remove unnecessary pytest option for coverage (see <https://pytest-cov.readthedocs.io/en/latest/xdist.html>).
- Rename `build_backend` to `backend`.
- Update pre-commit hooks to their latest versions.
- Use our own settings for code coverage.
- Use single quotes in commands.

### Fixed

- Add missing comma in `noxfile.py`.
- Fix sources to measure coverage for.
- Fix variable name in `noxfile.py`.
- Removed unused import in `noxfile.py`: `from nox.command import CommandFailed`.


## [1.0.0](https://github.com/leodevian/modern-python/tree/v1.0.0)

### Added

- Initial release.
