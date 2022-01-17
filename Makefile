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

.PHONY: git-status
git-status:
	git status
	@status=$$(git status --porcelain); \
	if [ ! -z "$${status}" ]; \
	then \
		echo "Error - working directory is dirty. Commit those changes!"; \
		exit 1; \
	fi

.PHONY: build
build: git-status
	git pull
	poetry build

.PHONY: bump
bump: git-status
	dev_tools/meters/make_shields.ksh
	git pull
	poetry version patch
	gh release create "v$$(poetry version --short)" --generate-notes
	git add .
	git commit -m "Update to $$(poetry version --short)."
	git push --tags
	git push

.PHONY: publish
publish: bump
	poetry publish --build

.PHONY: requirements
requirements: bump
	poetry export -f requirements.txt --output requirements.txt

.PHONY: all
all: lint2 lint package unit

.PHONY: allWithErrorHandling
allWithErrorHandling:
	$(MAKE) all || $(MAKE) withError

.PHONY: withError
withError:
	cd -

