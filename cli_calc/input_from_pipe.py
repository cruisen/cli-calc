# -*- coding: utf-8 -*-
"""Read input pipe via STDIN."""

import sys
from os import isatty

from cli_calc.read_line_parser import ReadLineParser


class InputPipe:  # pylint: disable=R0903
    """Read input from user at Terminal."""

    @staticmethod
    def is_pipe() -> bool:  # pragma: no cover  # noqa: WPS602, WPS605
        """Check if input from pipe."""
        return not isatty(sys.stdin.fileno())

    @staticmethod
    def input_pipe() -> None:  # pragma: no cover  # noqa: WPS602, WPS605
        """Get user input."""
        try:
            ReadLineParser.save_result(input())  # noqa: WPS421
        except EOFError:
            sys.exit(0)
