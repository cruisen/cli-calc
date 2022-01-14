SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
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
.PHONY: lint2
lint2:
	poetry run isort .
	poetry run black .
	poetry run git status


.PHONY: build
build: git-status build2

.PHONY: git-status
git-status:
	git status
	@status=$$(git status --porcelain); \
	if [ ! -z "$${status}" ]; \
	then \
		echo "Error - working directory is dirty. Commit those changes!"; \
		exit 1; \
	fi

.PHONY: build2
build2:
	git pull
	poetry build

.PHONY: all
all: lint2 lint package unit


