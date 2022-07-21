##############
## SET
export SHELL:=/usr/bin/env bash
export SHELLOPTS:=$(if $(SHELLOPTS),$(SHELLOPTS):)pipefail:errexit
# from: https://stackoverflow.com/questions/28597794/how-can-i-clean-up-after-an-error-in-a-makefile
$(eval CURRENT = $(shell poetry version --short))


##############
## LINT
.PHONY: lint
lint:
	@poetry version
	poetry run nitpick check
	poetry run pre-commit run --all-files
	poetry run isort .
	poetry run black .
	poetry run mypy cli_calc dev_tools/*/*.py tests/**/*.py
	poetry run flake8 .
	poetry run doc8 -q docs


##############
## ALL
.PHONY: all
all: lint check-package git-status unit html
	@#gh browse


.PHONY: allWithErrorHandling
allWithErrorHandling:
	@# From: https://stackoverflow.com/questions/21118020/can-gnu-make-execute-a-rule-whenever-an-error-occurs
	@$(MAKE) all || $(MAKE) withError


.PHONY: withError
withError:
	@cd -


##############
## check-package
.PHONY: check-package
check-package:
	poetry check
	poetry run pip check
	@# NvK
	@#	poetry run safety check --full-report
	poetry run safety check --bare


.PHONY: build
build: git-fail check-package
	git pull
	poetry build


##############
## GIT
.PHONY: git-status
git-status:
	@gh pr list
	@gh issue list --label 1-Now-Important
	@poetry run git status


.PHONY: git-fail
git-fail: git-status
	@status=$$(git status --porcelain); \
	if [ ! -z "$${status}" ]; \
	then \
		echo "Error - working directory is dirty. Commit those changes!"; \
		exit 1; \
	fi


##############
## TEST
.PHONY: test
test: lint check-package unit


.PHONY: unit
unit:
	poetry run pytest


##############
## BUMP
.PHONY: bump
bump: git-fail
	poetry run dev_tools/meters/make_shields.py
	git pull
	git add .
	poetry version patch
	git add .
	git commit --no-verify -m "Update to $$(poetry version --short)."
	git push
	git push --tags
	gh release create "v$$(poetry version --short)" --generate-notes
	git pull
	git push
	git pull
	poetry run open "https://pypi.org/project/cli-calc/"


.PHONY: bump_minor
bump_minor: git-fail
	@$(eval MINOR = $(shell dev_tools/sem_ver/get_ver_for_rule.py minor))
	@$(eval MINOR_NUM = $(shell gh listMilestones | jq '.data.repository.milestones.nodes[]' | jq '. | select(.title | contains("$(MINOR)"))' | jq -c '.number'))
	@$(eval MINOR_ISSUES = $(shell gh viewMilestone $(MINOR_NUM) | jq '.data.repository.milestone.issues.nodes[]' | jq -c '[.state, .number, .title, .url]' | sort))
	@echo $(MINOR)
	@echo $(MINOR_ISSUES)
	@# TODO add user OK
	poetry run dev_tools/meters/make_shields.py
	git pull
	poetry version minor
	git add .
	git commit --no-verify -m "Update to $$(poetry version --short)."
	git push --tags
	gh release create "v$$(poetry version --short)" --generate-notes --notes "$(MINOR): $(MINOR_ISSUES)"
	git pull
	git push
	@echo "Consider to link Milestone to tag."


.PHONY: bump_major
bump_major:
	@$(eval MAJOR = $(shell dev_tools/sem_ver/get_ver_for_rule.py major))
	@$(eval MAJOR_NUM = $(shell gh listMilestones | jq '.data.repository.milestones.nodes[]' | jq '. | select(.title | contains("$(MAJOR)"))' | jq -c '.number'))
	@$(eval MAJOR_ISSUES = $(shell gh viewMilestone $(MAJOR_NUM) | jq '.data.repository.milestone.issues.nodes[]' | jq -c '[.state, .number, .title, .url]' | sort))
	@echo $(MAJOR)
	@echo $(MAJOR_ISSUES)
	@# TODO add user OK


##############
## PUBLISH
.PHONY: publish-test
publish-test:
	poetry publish --repository testpypi --build
	@open "https://test.pypi.org/project/cli-calc/"


.PHONY: publish
publish: bump
	poetry publish --build


##############
## DEFAULT (e.g. -> docs/Makefile html)
.DEFAULT:
	@cd docs && $(MAKE) $@
