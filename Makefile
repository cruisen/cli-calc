export SHELL:=/usr/bin/env bash
export SHELLOPTS:=$(if $(SHELLOPTS),$(SHELLOPTS):)pipefail:errexit
# from: https://stackoverflow.com/questions/28597794/how-can-i-clean-up-after-an-error-in-a-makefile

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
	dev_tools/meters/make_shields.py
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
	# From: https://stackoverflow.com/questions/21118020/can-gnu-make-execute-a-rule-whenever-an-error-occurs
	$(MAKE) all || $(MAKE) withError

.PHONY: withError
withError:
	cd -

.DEFAULT:
	@cd docs && $(MAKE) $@

