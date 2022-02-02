#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check docs/requirement.txt."""

import os
import sys

import semver  # pylint disable=E0401


def usage() -> None:
    """Usage."""
    print("Prints next Version for given Bump Rule")  # noqa: WPS421
    print("Usage: check_docs_requirements.py")  # noqa: WPS421
    sys.exit()

print("checking: docs/requirements.txt")

cmd_dev = os.popen(
    "poetry export --without-hashes --dev --format requirements.txt | cut -d';' -f1"
)  # noqa: S605, S607
dev: str = cmd_dev.read().strip()

cmd_doc = os.popen(
    'cd $(git rev-parse --show-toplevel) ; cat docs/requirements.txt | grep -v "^$" | grep -v "^#" | sort'
)  # noqa: S605, S607
doc: str = cmd_doc.readlines()


for line_nl in doc:
    line=line_nl.strip()
    package=line.split("=")[0]

    for item in dev.split("\n"):
        if package in item:
            match_line=item.strip()
            match=match_line.split("=")[0]

            if match == package:
                if match_line != line:
                    print(match_line)
                    print(line)


