install:
	poetry install

test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=algorithms --cov-report xml tests

lint:
	poetry run flake8 algorithms

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
