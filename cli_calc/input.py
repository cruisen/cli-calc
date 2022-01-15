# -*- coding: utf-8 -*-
"""Input handler."""

from cli_calc.cli_output import Output
from cli_calc.config import Config
from cli_calc.input_cli import InputCli
from cli_calc.input_from_pipe import InputPipe


class Input:  # pylint: disable=R0903
    """Read input from user at Terminal or Pipe (STDIN)."""

    @staticmethod
    def init_output() -> None:  # pragma: no cover  # noqa: WPS602, WPS605, WPS463, E501
        """Init user output."""
        if not InputPipe.is_pipe():
            Config.option[Config.Option.is_pipe] = False  # type: ignore  # pylint: disable=E1101
            Output.print_help()
            Output.print_line()
            return

        Config.option[Config.Option.print_help] = False  # type: ignore  # pylint: disable=E1101
        Config.option[Config.Option.print_header] = False  # type: ignore  # pylint: disable=E1101
        Config.option[Config.Option.echo_in] = True  # type: ignore  # pylint: disable=E1101
        Config.option[Config.Option.is_pipe] = True  # type: ignore  # pylint: disable=E1101

    @staticmethod
    def get_line() -> None:  # pragma: no cover  # noqa: WPS602, WPS605, WPS463
        """Get user input."""
        if InputPipe.is_pipe():
            InputPipe.input_pipe()
        else:
            InputCli.input_cli()
