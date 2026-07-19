# Agent Instructions - {{ project_name }}

This file is a starting point for repository-specific agent guidance. The first
agent working in a newly generated repository must inspect the project and
replace the placeholders and assumptions below with verified facts.

## First-run checklist

1. Inspect the complete repository tree, excluding generated caches and build output.
2. Verify the package layout: `{{ package_path }}`.
3. Read `pyproject.toml`, `README.md`, `Makefile`, and `noxfile.py`.
4. Replace this file's placeholder architecture and workflow notes with facts from the source.
5. Review every skill under `.github/skills/` and update stale paths or commands.
6. Run the documented checks and record the commands that actually pass.

## Project overview

- Distribution: `{{ distribution_name }}`
- Import package: `{{ package_name }}`
- Layout: `{{ package_layout }}`
- Python support: 3.10 through 3.14
- Build: `uv build`
- Tests: `pytest` through Nox

## Repository rules

- Keep runtime code, tests, documentation, and scripts in their existing areas.
- Do not treat generated caches, build artifacts, or virtual environments as source.
- Keep tests focused on observable behavior and add regression coverage for bug fixes.
- Verify package metadata and import paths after changing the package layout.
- Update this file and the skills when architecture or workflow commands change.

## Commands

```text
make install
make test
make lint
make build
```

Use `nox -s tests`, `nox -s lint`, and `nox -s typecheck` for focused checks.

## Architecture notes

Replace this section during the first agent-context update with the package's
actual modules, public API boundaries, data flow, and important invariants.
Avoid copying assumptions from another project into this repository.
