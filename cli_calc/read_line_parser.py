# -*- coding: utf-8 -*-
"""CLI ReadLineParser."""


import sys
from typing import Optional, Union

from cli_calc.cli_eval import Eval
from cli_calc.cli_output import Output
from cli_calc.config import Config
from cli_calc.memory import Memory


class ReadLineParser:
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
    def parse_display(  # noqa: WPS602, C901
        in_string: Optional[str],
    ) -> Optional[str]:
        """Parse display arguments, if any."""
        if in_string is None or len(in_string) != 2:
            return in_string

        if "+" not in in_string and "-" not in in_string:
            return in_string

        if "+" in in_string:
            new = True

        if "-" in in_string:
            new = False

        display_char: str = in_string.translate(
            {ord(char): None for char in "+-"},
        )

        if len(display_char) != 1:
            return in_string

        if display_char not in Config.arg_dict:
            return in_string

        name = Config.arg_dict[display_char]
        Config.set_item(
            name,
            Config.Column.print_it.name,  # pylint: disable=E1101
            new,
        )
        Config.option[Config.Option.was_noop] = True  # type: ignore  # pylint: disable=E1101
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
