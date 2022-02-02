#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Print next Version for given Bump Rule."""

import os
import sys

import semver  # pylint disable=E0401


def usage() -> None:
    """Usage."""
    print("Prints next Version for given Bump Rule")  # noqa: WPS421
    print('Usage: get_ver_for_rule.py: "defaults to patch"')  # noqa: WPS421
    print("   Or: get_ver_for_rule.py patch")  # noqa: WPS421
    print("   Or: get_ver_for_rule.py minor")  # noqa: WPS421
    print("   Or: get_ver_for_rule.py major")  # noqa: WPS421
    sys.exit()


rule: str

number_of_args: int = len(sys.argv)

if number_of_args > 2:
    usage()

if number_of_args == 1:
    rule = "patch"
else:
    rule = sys.argv[1]


stream = os.popen("poetry version --short")  # noqa: S605, S607
output: str = stream.read().strip()

ver: str = semver.VersionInfo.parse(output)
if not ver.isvalid:  # type: ignore
    print(f"Error: {output} is not a valid semver version string.")  # noqa: WPS421
    usage()

rules = {
    "major": ver.bump_major,  # type: ignore
    "minor": ver.bump_minor,  # type: ignore
    "patch": ver.bump_patch,  # type: ignore
    "prerelease": ver.bump_prerelease,  # type: ignore
    "build": ver.bump_build,  # type: ignore
}

if rule not in rules:
    usage()

print(rules[rule]())  # noqa: WPS421
