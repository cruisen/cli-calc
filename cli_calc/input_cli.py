# -*- coding: utf-8 -*-
"""Read input from user at Terminal."""

from cli_calc.read_line_parser import ReadLineParser


class InputCli:  # pylint: disable=R0903
    """Read input from user at Terminal."""

    @staticmethod
    def input_cli() -> None:  # pragma: no cover  # noqa: WPS602, WPS605
        """Get user input."""
        ReadLineParser.save_result(input(": "))  # noqa: WPS421
