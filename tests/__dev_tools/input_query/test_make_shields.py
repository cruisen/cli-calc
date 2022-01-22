# -*- coding: utf-8 -*-
"""Test input parsing and eval functions with pytest."""

import os

import pytest  # pylint: disable=E0401

from dev_tools.meters.make_shields import Shield  # pylint: disable=E0401


@pytest.mark.parametrize(  # noqa: WPS317
    ("expected"),
    [
        ("cli-calc"),
    ],
)
class TestMakeShields:  # pylint: disable=R0903
    """Test make Shield."""

    @staticmethod
    def test_provide_work_dir(  # noqa: WPS602
        expected: str,
    ):
        """A pwd test."""
        file_name: str = Shield.provide_work_dir()
        file_name = os.path.basename(file_name)
        assert file_name == expected
