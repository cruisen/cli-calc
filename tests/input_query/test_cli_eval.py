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

from cli_calc.cli_eval import Eval  # pylint: disable=E0401
from cli_calc.config import Config  # pylint: disable=E0401
from cli_calc.memory import Memory  # pylint: disable=E0401

Config.init(Memory.value_dict)


@given(floats(allow_nan=False))
def test_eval_floats(test_float):
    """Find float edge cases with hypothesis."""
    string_from_float = str(test_float)
    assert Eval.eval_string(string_from_float) == test_float


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string", "expected"),
    [
        ("math.nan", math.nan),
        ("nan", math.nan),
        ("nan", float("NaN")),
        ('float("nan")', math.nan),
        ('float("NaN")', math.nan),
        # ("NaN", math.nan), see test_read_line_parser_nan.py
    ],
)
def test_eval_nan(  # noqa: WPS602
    in_string: str,
    expected: float,
):
    """Input to Output test for NaN."""
    assert math.isnan(Eval.eval_string(in_string)) and math.isnan(expected)  # noqa: S101


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string", "expected"),
    [
        (None, None),
        ("", None),
        ("help(math)", None),
        ("0", 0),
        ("-0", -0.0),  # noqa: WPS358
        ("-0.", -0.0),  # noqa: WPS358
        ("cos(3.141592653589793/2)", 6.123233995736766e-17),
        ("sin(radians(45))-(sqrt(2)/2)", -1.1102230246251565e-16),
        ("sin(1/2)", 0.479425538604203),
        ("sic(1/2)", None),  # raises NameError ("sic" function is not in math)
        ("2*(3+1", None),  # raises SyntaxError (Missing ")")
        (
            "2.0^2",
            None,
        ),  # raises TypeError ("^" is XOR, does not work on Float)  # noqa: E501
    ],
)
def test_eval_string(  # noqa: WPS602
    in_string: Optional[str],
    expected: Optional[Union[int, float]],
):
    """Input to Output test."""
    assert Eval.eval_string(in_string) == expected  # noqa: S101


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string"),
    [
        ("sys.exit(42)"),
    ],
)
def test_eval_string_sys_exit(  # noqa: WPS602
    in_string: Optional[str],
):
    """Input to sys.exit() test."""
    with does_not_raise(SystemExit):
        Eval.eval_string(in_string)
