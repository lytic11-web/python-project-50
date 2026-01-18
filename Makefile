install:
	uv pip install -e .[dev]

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml --cov-report=term

lint:
	uv run python -m ruff check

check: test lint

build:
	uv build

.PHONY: install run test test-coverage lint check build

format:
	uv run python -m ruff format .
	uv run python -m ruff check --fix .
