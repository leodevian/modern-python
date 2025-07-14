# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This project uses [*towncrier*](https://towncrier.readthedocs.io/).

<!-- towncrier release notes start -->

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
