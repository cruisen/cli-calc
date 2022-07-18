# -*- coding: utf-8 -*-
"""Test input parsing and eval functions with pytest."""

import math

import pytest  # pylint: disable=E0401

from cli_calc.config import Config  # pylint: disable=E0401
from cli_calc.memory import Memory  # pylint: disable=E0401
from cli_calc.read_line_parser import ReadLineParser  # pylint: disable=E0401

Config.init(Memory.value_dict)


@pytest.mark.parametrize(  # noqa: WPS317
    ("last_value", "in_string", "expected"),
    [
        ("2", "_*2", 4),
        ("1", "math.pi/_", math.pi),
    ],
)
def test_handle_input_last_input(  # noqa: WPS602
    last_value: str,
    in_string: str,
    expected: float,
):
    """
    Input to Output test.

    Mock last value first.
    """
    ReadLineParser.save_result(last_value)
    assert ReadLineParser.handle_input(in_string) == expected  # noqa: S101
