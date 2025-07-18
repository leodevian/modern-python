# List recipes
default:
  @just --list

# Install pre-commit hooks and dependencies
[group('dev')]
install:
  uv sync
  @just install-hooks

# Install pre-commit hooks
[group('dev')]
install-hooks:
  uv run pre-commit install --install-hooks

# Uninstall pre-commit hooks
[group('dev')]
uninstall-hooks:
  uv run pre-commit uninstall
