SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	# NvK isort & black
	poetry run isort .
	poetry run black .
	poetry run git status
	# NvK continue
	poetry run mypy cli_calc tests/**/*.py
	poetry run flake8 .
	poetry run nitpick check
	poetry run doc8 -q docs

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	# NvK
	#	poetry run safety check --full-report
	poetry run safety check --bare

.PHONY: test
test: lint package unit

# NvK
.PHONY: all
all: lint package unit


