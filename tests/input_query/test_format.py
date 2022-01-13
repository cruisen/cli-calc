# -*- coding: utf-8 -*-
"""Test input parsing and eval functions with pytest."""


import pytest  # pylint: disable=E0401

from cli_calc.config import Config  # pylint: disable=E0401
from cli_calc.format import Format  # pylint: disable=E0401
from cli_calc.memory import Memory  # pylint: disable=E0401

Config.init(Memory.value_dict)


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_float", "expected"),
    [
        (1 / 3, "1/3"),
        (1 / 9, "1/9"),
        (-7 / 12, "-7/12"),
    ],
)
def test_get_fraction(  # noqa: WPS602
    in_float: float,
    expected: str,
):
    """Input for fraction format test."""
    assert Format.get_fraction(in_float) == expected  # noqa: S101
