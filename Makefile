.PHONY: install test lint format format-check run

install:
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

format-check:
	ruff format --check .

run:
	uvicorn semiconductor_ai_platform.api.main:app --reload
