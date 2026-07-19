.PHONY: help clean build wheel install test coverage coverage-html lint format

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  help           Show this help message"
	@echo "  clean          Remove build artifacts and cache files"
	@echo "  build          Build source distribution and wheel"
	@echo "  wheel          Build wheel only"
	@echo "  install        Install the package with development dependencies"
	@echo "  test           Run the pytest suite"
	@echo "  coverage       Run tests with a terminal coverage report"
	@echo "  coverage-html  Run tests with an HTML coverage report"
	@echo "  lint           Run pre-commit checks"
	@echo "  format         Format Python files with Ruff"

clean:
	rm -rf dist/ build/ .nox/ .pytest_cache/ .ruff_cache/ htmlcov/
	find . -name "*.egg-info" -type d -prune -exec rm -rf {} +
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	find . -name "*.py[cod]" -delete
	find . -name ".coverage*" -delete

build:
	uv build

wheel:
	uv build --wheel

install:
	uv sync --group dev

test:
	nox -s tests

coverage:
	uv run coverage run -m pytest
	uv run coverage report

coverage-html:
	uv run coverage run -m pytest
	uv run coverage html

lint:
	nox -s lint

format:
	uv run ruff format .
