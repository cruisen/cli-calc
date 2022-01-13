# -*- coding: utf-8 -*-
"""Test IEEE functions with pytest."""

import pytest  # pylint: disable=E0401

from cli_calc.ieee import IEEE  # pylint: disable=E0401


@pytest.mark.parametrize(  # noqa: WPS317
    ("expected", "val_float"),
    [
        ("0x00000000", -0),  # -0 as INT is 0.0 as float
        ("0x00000000", 0),
        ("0x00000000", 0.0),  # noqa: WPS358
        ("0x80000000", -0.0),  # noqa: WPS358
        ("0x40000000", 2),
        ("0x40000000", 2.0),
        ("0xC0000000", -2),
        ("0xC0000000", -2.0),
        ("0x40400000", 3),
        ("0xC0400000", -3),
        ("0x4E9D3A75", 1318926965),
        ("0x4E9D3A75", 1318926965.0),
        ("0xCE46E46E", -834214802),
        ("0xCE46E46E", -834214802.0),
        ("0x20000000", 1.08420217249e-19),
        ("0x00800000", 1.17549435082e-38),
        ("0x7F000000", 1.7014118346e38),
        ("0xFF000000", -1.7014118346e38),
        ("0x7F7FFFFF", 3.40282346639e38),
        ("0xFF7FFFFF", -3.40282346639e38),
        ("0x3FFFFFFF", 1.99999988079),
        ("0xBFFFFFFF", -1.99999988079),
        ("NaN", 1.40500611775288e51),
    ],
)
class TestParametrizedFloatToIeee:
    """Test parametrized Float to IEEE functions."""

    @staticmethod
    def test_float_to_ieee(  # noqa: WPS602
        val_float: float,
        expected: str,
    ):
        """Float to IEEE Hex test Values.

        See: https://www.h-schmidt.net/FloatConverter/IEEE754.html
        """
        as_bin = False
        assert IEEE.float_to_ieee(val_float, as_bin) == expected  # noqa: S101

    @staticmethod
    def test_float_to_ieee_hex(  # noqa: WPS602
        val_float: float,
        expected: str,
    ):
        """Float to IEEE Hex test Values."""
        assert IEEE.float_to_ieee_hex(val_float) == expected  # noqa: S101

    @staticmethod
    def test_ieee_to_float(  # noqa: WPS602
        val_float: float,
        expected: str,
    ):
        """
        IEEE Hex to Float test Values.

        Note: Using the parametrized set 'backwards'.
        """
        val_int: int
        if expected == "NaN":
            return

        val_int = int(expected, base=16)
        assert IEEE.ieee_to_float(val_int) == pytest.approx(  # noqa: S101
            val_float,
            1,
        )
