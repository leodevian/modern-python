# Python style guide

Follow the configured Ruff rules in `pyproject.toml`. This document specifies
the project conventions that complement those rules.

## Code and documentation

- Use double quotes for all strings.
- Add type hints to all code.
- Use NumPy-style docstrings only.
- Thoroughly document public classes and methods.
- Private classes, methods, globals, and similar implementation details may
  have brief documentation or none when their purpose is clear from context.
- Make errors and warnings concise and informative. Avoid multi-sentence
  messages unless a single sentence would sacrifice clarity.

## Design

- Prefer legible, concise, minimal code.
- Avoid unnecessary abstractions and large collections of private helpers.
- Inline very short helpers.
- Do not extract simple logic merely because it appears once or twice. Keep
  such logic at its call sites when it is likely to need independent changes.

## Tests

- Keep test suites DRY and concise.
- Use pytest fixtures, parametrization, and mocks where they make tests more
  readable or remove duplication.
