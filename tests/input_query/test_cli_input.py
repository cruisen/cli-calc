# -*- coding: utf-8 -*-
"""Test input parsing and eval functions with pytest."""

import math  # pylint: disable=E0401
from contextlib import nullcontext as does_not_raise
from typing import Optional, Union

import pytest  # pylint: disable=E0401

from cli_calc.cli_eval import Eval  # pylint: disable=E0401
from cli_calc.cli_input import Input  # pylint: disable=E0401
from cli_calc.config import Config  # pylint: disable=E0401
from cli_calc.memory import Memory  # pylint: disable=E0401

Config.init(Memory.value_dict)


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string", "expected"),
    [
        ("0", 0),
        ("nan", math.nan),
        ("pi * pi", 9.869604401089358),
        ("cos(pi / 2)", 6.123233995736766e-17),
        ("0xFF ^ 0b10", 253),
        ("2**8-1", 255),
        ("factorial(42)", 1405006117752879898543142606244511569936384000000000),
        ("1/3", 0.3333333333333333),
    ],
)
class TestInput:
    """Test Input Queries."""

    @staticmethod
    def test_handle_input(  # noqa: WPS602
        in_string: str,
        expected: Union[int, float],
    ):
        """Input to Output test."""
        assert Input.handle_input(in_string) == pytest.approx(  # noqa: S101, E501
            expected,
            nan_ok=True,
        )

    @staticmethod
    def test_save_result(  # noqa: WPS602
        in_string: str,
        expected: float,
    ):
        """Input to value_dict test."""
        Input.save_result(in_string)

        val_int: int = Memory.value_dict[Config.ValueNS.int]  # type: ignore  # pylint: disable=E1101  # noqa: E501
        val_float: float = Memory.value_dict[Config.ValueNS.float]  # type: ignore  # pylint: disable=E1101  # noqa: E501

        if isinstance(expected, int):
            assert val_int == expected  # noqa: S101
        else:
            assert pytest.approx(val_float, nan_ok=True) == expected  # noqa: S101, E501


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
