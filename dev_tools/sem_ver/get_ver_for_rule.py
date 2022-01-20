#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bump Current version."""

import os
import sys

import semver  # pylint disable=E0401


def usage():
    """Usage."""
    print('Usage: get_ver_for_rule.py for "patch"')  # noqa: WPS421
    print("   Or: get_ver_for_rule.py minor")  # noqa: WPS421
    print("   Or: get_ver_for_rule.py major")  # noqa: WPS421
    sys.exit()


number_of_args = len(sys.argv)

if number_of_args > 2:
    usage()

if number_of_args == 1:
    rule = "patch"
else:
    rule = sys.argv[1]


stream = os.popen("poetry version --short")  # noqa: S605, S607
output = stream.read().strip()

ver = semver.VersionInfo.parse(output)
if not ver.isvalid:
    print(f"Error: {output} is not a valid semver version string.")  # noqa: WPS421
    usage()

rules = {
    "major": ver.bump_major,
    "minor": ver.bump_minor,
    "patch": ver.bump_patch,
    "prerelease": ver.bump_prerelease,
    "build": ver.bump_build,
}

if rule not in rules:
    usage()

print(rules[rule]())  # noqa: WPS421
