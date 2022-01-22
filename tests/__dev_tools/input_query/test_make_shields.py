# -*- coding: utf-8 -*-
"""Test input parsing and eval functions with pytest."""

import pytest  # pylint: disable=E0401

from dev_tools.meters.make_shields import Shield  # pylint: disable=E0401


@pytest.mark.parametrize(  # noqa: WPS317
    ("expected"),
    [
        ("/Users/nkrusens/esabox/Developer/python/cli-calc"),
    ],
)
class TestMakeShields:  # pylint: disable=R0903
    """Test make Shield."""

    @staticmethod
    def test_provide_work_dir(  # noqa: WPS602
        expected: str,
    ):
        """A pwd test."""
        assert Shield.provide_work_dir() == expected
