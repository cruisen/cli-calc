# -*- coding: utf-8 -*-
"""IEEE handling."""

import math
import struct
from functools import partialmethod
from typing import Callable, Optional


class IEEE:
    """
    IEEE handling.

    * Provide float, int to ieee (hex, bin).
    * Provide ieee(hex) to float, int.
    * Provide padding.
    * Provide convenient functions via partialmethod.
    """

    HEX_IEEE_LENGTH: int = 8  # noqa: WPS115
    BIN_IEEE_LENGTH: int = 32  # noqa: WPS115

    @staticmethod
    def bin_or_hex_pad(  # pragma: no cover  # noqa: WPS210, C901, WPS602
        val_int: int,
        as_bin: Optional[bool] = None,
        length: Optional[int] = None,
        upper: Optional[bool] = None,
    ) -> str:
        """Cast Integer to Binary or Hex with padded zeroes."""
        pre: str
        out: str
        cut: int = 2
        minus: str = ""

        if isinstance(val_int, float):  # pragma: no cover
            return "NaN"

        if as_bin is None:  # type: ignore  # pragma: no cover
            as_bin = False

        if length is None:  # pragma: no cover
            length = 0

        pre = "0b" if as_bin else "0x"

        # Negative value?
        if val_int < 0:  # pragma: no cover
            cut = 3
            minus = "-"

        if as_bin:  # pragma: no cover
            out = bin(val_int)[cut:]
        else:
            out = hex(val_int)[cut:]
            if upper:  # pragma: no cover
                out = out.upper()

        out = out.zfill(length)
        out = f"{minus}{pre}{out}"

        return out  # noqa: WPS331

    bin_pad: Callable = partialmethod(bin_or_hex_pad, as_bin=True)  # type: ignore  # noqa: E501
    hex_pad: Callable = partialmethod(bin_or_hex_pad, as_bin=False)  # type: ignore  # noqa: E501
    hex_pad_upper: Callable = partialmethod(hex_pad, upper=True)  # type: ignore  # noqa: E501

    hex_pad_ieee: Callable = partialmethod(hex_pad_upper, length=HEX_IEEE_LENGTH)  # type: ignore  # pylint: disable=C0301  # noqa: E501
    bin_pad_ieee: Callable = partialmethod(bin_pad, length=BIN_IEEE_LENGTH)  # type: ignore  # pylint: disable=C0301  # noqa: E501

    @staticmethod
    def ieee_to_float(val_int: int) -> float:  # noqa: WPS602
        """
        Convert IEEE HEX to float.

        See: https://docs.python.org/3/library/struct.html
        """
        try:
            out: float = struct.unpack("f", struct.pack("I", val_int))[0]
        except struct.error:  # pragma: no cover
            out = math.nan
        return out

    @staticmethod
    def float_to_ieee(  # noqa: WPS602
        val_float: float,
        as_bin: Optional[bool] = None,
    ) -> str:
        """
        Convert float to IEEE Value.

        struct.unpack based on: https://tinyurl.com/54m63uvs
        See also: https://www.h-schmidt.net/FloatConverter/IEEE754.html

        Edge Cases INT Representation = Float :-):
        https://stackoverflow.com/a/45185154/9085290
        - float: 1318926965 (0x4E9D3A75)
        - handled in pytest
        """
        if as_bin is None:  # pragma: no cover
            as_bin = False

        ieee_int: int

        try:
            ieee_int = struct.unpack("!I", struct.pack("!f", val_float))[0]
        except OverflowError as err:
            print(f"{type(err).__name__}: {err}")  # noqa: WPS237, WPS421
            ieee_int = math.nan  # type: ignore

        hex_str: str = IEEE.hex_pad_ieee(ieee_int)
        bin_str: str = IEEE.bin_pad_ieee(ieee_int)

        if as_bin:  # pragma: no cover
            return bin_str

        return hex_str

    float_to_ieee_hex: Callable = partialmethod(float_to_ieee, as_bin=False)  # type: ignore  # pylint: disable=C0301  # noqa: E501
    float_to_ieee_bin: Callable = partialmethod(float_to_ieee, as_bin=True)  # type: ignore  # pylint: disable=C0301  # noqa: E501
