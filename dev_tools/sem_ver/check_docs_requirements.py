#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check docs/requirement.txt."""

import os
import re
import sys


def usage() -> None:
    """Usage."""
    print("Prints next Version for given Bump Rule")  # noqa: WPS421
    print("Usage: check_docs_requirements.py")  # noqa: WPS421
    sys.exit()


print("checking: docs/requirements.txt")  # noqa: WPS421

cmd_dev = os.popen(  # noqa: S605,S607
    "poetry export --without-hashes --dev --format requirements.txt | cut -d';' -f1",
)  # noqa: S605, S607
dev: str = cmd_dev.read().strip()

cmd_doc = os.popen(  # noqa: S605,S607
    'cd $(git rev-parse --show-toplevel) ; cat docs/requirements.txt | grep -v "^$" | grep -v "^#" | sed "s/#.*//" | sort',  # noqa: E501
)
doc = cmd_doc.readlines()


for line_nl in doc:  # noqa: C901
    line = line_nl.strip()
    package = re.split("=|<|>", line)[0]

    found = 0
    for dev_line in dev.split("\n"):
        if package not in dev_line:
            continue

        found += 1
        match_line = dev_line.strip()
        match = re.split("=|<|>", match_line)[0]

        if match != package:
            continue

        if match_line != line:
            print(match_line)  # noqa: WPS421
            print(line)  # noqa: WPS421

    if not found:
        print(f"In doc only: {line}")  # noqa: WPS421
