# -*- coding: utf-8 -*-
"""Format int of float."""

from fractions import Fraction


class Format:  # pylint: disable=R0903
    """Output Formats for int or float."""

    @staticmethod
    def get_fraction(val_float: float) -> str:  # noqa: WPS602
        """Format a fraction from a float."""
        return str(Fraction(val_float).limit_denominator())
