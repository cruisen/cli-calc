# -*- coding: utf-8 -*-
"""CLI ReadLineParser."""


import sys
from typing import Optional, Union

from cli_calc.cli_eval import Eval
from cli_calc.cli_output import Output
from cli_calc.config import Config
from cli_calc.memory import Memory


class ReadLineParser:  # noqa: WPS214
    """
    CLI ReadLineParser.

    * Sanitize the input string
    * Apply parsing
    * Hand over to eval
    """

    @staticmethod
    def save_result(in_string: str) -> None:  # noqa: WPS602
        """Get and cast user input."""
        out_obj: Optional[
            Union[
                int,
                float,
            ]
        ] = ReadLineParser.handle_input(in_string)

        if isinstance(out_obj, (int, float)):  # pragma: no cover
            Memory.value_dict[Config.ValueNS.float] = float(out_obj)  # type: ignore  # pylint: disable=E1101  # noqa: E501
            try:
                Memory.value_dict[Config.ValueNS.int] = int(out_obj)  # type: ignore  # pylint: disable=E1101  # noqa: E501
            except ValueError as err:
                print(f"{type(err).__name__}: {err}")  # noqa: WPS237, WPS421

    @staticmethod
    def handle_input(  # noqa: WPS602
        in_string: str,
    ) -> Optional[Union[int, float]]:
        """
        Strip, parse_arguments, parse and evaluate user input.

        Consider to upgrade to pipelines:
        https://returns.readthedocs.io/en/latest/pages/pipeline.html
        """
        out_obj: Optional[Union[int, float]]

        (out_obj,) = (  # noqa: WPS460
            Eval.eval_string(
                ReadLineParser.parse_expression(
                    ReadLineParser.parse_display(
                        ReadLineParser.parse_argumnents(
                            ReadLineParser.strip(in_string),
                        ),
                    ),
                ),
            ),
        )

        return out_obj

    @staticmethod
    def strip(in_string: str) -> str:  # noqa: WPS602
        """Strip space from string."""
        return "".join(in_string.split())

    @staticmethod
    def parse_argumnents(in_string: str) -> Optional[str]:  # noqa: WPS602
        """Parse for help or exit."""
        if len(in_string) != 1:
            return in_string

        if "q" in in_string:
            sys.exit(1)

        elif "h" in in_string:
            Output.print_help()
            return None

        return in_string

    @staticmethod
    def find_plus_minus(  # noqa: WPS602
        in_string: Optional[str],
    ) -> bool:
        """Parse display arguments for plus and minus, if any."""
        if in_string is None or len(in_string) != 2:
            return False

        return "+" in in_string or "-" in in_string

    @staticmethod
    def set_output(  # noqa: WPS602
        in_string: str,
    ) -> bool:
        """Parse display arguments for plus or minus."""
        return "+" in in_string

    @staticmethod
    def check_display_char(  # noqa: WPS602
        display_char: Optional[str],
    ) -> bool:
        """Check display char for valid value."""
        if not display_char:
            return False

        return display_char in Config.arg_dict

    @staticmethod
    def set_display_configuration(  # noqa: WPS602
        display_char: str,
        show_output: bool,
    ) -> None:
        """Set Configuration."""
        name: str = str(Config.arg_dict[display_char])

        Config.set_item(
            name,
            Config.Column.print_it.name,  # pylint: disable=E1101
            show_output,
        )

        Config.option[Config.Option.was_noop] = True  # type: ignore  # pylint: disable=E1101

    @staticmethod
    def parse_display(  # noqa: WPS602, C901
        in_string: Optional[str],
    ) -> Optional[str]:
        """Parse display arguments, if any."""
        show_output: bool

        if not ReadLineParser.find_plus_minus(in_string):
            return in_string

        plus_minus: str = str(in_string)
        show_output = ReadLineParser.set_output(plus_minus)

        display_char: str = plus_minus.translate(
            {ord(char): None for char in "+-"},
        )

        if not ReadLineParser.check_display_char(display_char):
            return in_string

        ReadLineParser.set_display_configuration(display_char, show_output)

        Output.print_header()

        return None

    @staticmethod
    def parse_expression(  # noqa: WPS602
        in_string: Optional[str],
    ) -> Optional[str]:
        """Parse for last value."""
        if in_string is None:
            return None

        in_string = in_string.replace(
            "_float_",
            str(Memory.value_dict[Config.ValueNS.float]),  # type: ignore  # pylint: disable=E1101  # noqa: E501
        )
        in_string = in_string.replace(
            "!!",
            str(Memory.value_dict[Config.ValueNS.float]),  # type: ignore  # pylint: disable=E1101  # noqa: E501
        )
        in_string = in_string.replace(
            "_int_",
            str(Memory.value_dict[Config.ValueNS.int]),  # type: ignore  # pylint: disable=E1101  # noqa: E501
        )

        # Handle True/False
        in_string = in_string.replace("true", "True")
        in_string = in_string.replace("false", "False")

        return in_string  # noqa: WPS331
