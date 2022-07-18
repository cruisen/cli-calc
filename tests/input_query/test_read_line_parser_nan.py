# -*- coding: utf-8 -*-
"""
Test input parsing and eval functions with pytest.
"""

import math
from contextlib import nullcontext as does_not_raise
from typing import Optional, Union

import pytest  # pylint: disable=E0401
from hypothesis import given
from hypothesis.strategies import floats

from cli_calc.config import Config  # pylint: disable=E0401
from cli_calc.memory import Memory  # pylint: disable=E0401
from cli_calc.read_line_parser import ReadLineParser  # pylint: disable=E0401

Config.init(Memory.value_dict)


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string", "expected"),
    [("NaN", math.nan)],
)
def test_handle_input_nan(  # noqa: WPS602
    in_string: str,
    expected: float,
):
    """Input to Output test for NaN."""
    assert math.isnan(ReadLineParser.handle_input(in_string)) and math.isnan(
        expected
    )  # noqa: S101
