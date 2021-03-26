install:
	poetry install

test:
	poetry run pytest algoritms tests

test-coverage:
	poetry run pytest --cov=algoritms --cov-report xml tests

lint:
	poetry run flake8 algoritms

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
