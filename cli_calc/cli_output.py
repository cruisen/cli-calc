# -*- coding: utf-8 -*-
"""CLI Output."""


from typing import Callable, Union

from cli_calc.config import Config
from cli_calc.memory import Memory


class Output:
    """
    CLI Output.

    * Print help
    * Print header (type hints like: int, float, hex, ...)
    * Print value / result
    """

    @staticmethod
    def print_help() -> None:  # pragma: no cover  # noqa: WPS213, WPS602, WPS605
        """Print Help lines."""
        if not Config.option[Config.Option.print_help]:  # type: ignore  # pylint: disable=E1101
            return

        out: str = """Input:
    "q" for quit, "h" for help

    "_float_" and/or "_int_" for last value
    "pi", "tau" and "e" for pi, tau and Euler

    "+f" to add display for fraction, "-f" to suppress display for fraction
        Other letters are:
        he(x), (o)ctal, (b)inary, (i)nteger,
        (f)raction, (t)ruth, i(e)ee, ieee_bi(n), f(r)om_ieee
        "float" is always visible

    See https://docs.python.org/3/library/math.html, use without "math."
        https://www.w3schools.com/python/python_operators.asp

    Try "cos(pi/2)", XOR: "0xFF ^ 0b10", "2**8-1", "factorial(42)",
        "help(math)" """

        print("-" * Config.DIVIDER_LINE_LENGTH)  # noqa: WPS421
        print(out)  # noqa: WPS421
        print("-" * Config.DIVIDER_LINE_LENGTH)  # noqa: WPS421
        Output.print_header()

    @staticmethod
    def print_header() -> None:  # noqa: WPS602, WPS605
        """Print header of configured types."""
        if not Config.option[  # noqa: WPS337
            Config.Option.print_header  # type: ignore  # pylint: disable=E1101
        ]:
            return  # pragma: no cover

        for function in Config.row_list:
            if not Config.get_item(  # noqa: WPS337
                function,
                Config.Column.print_it.name,  # pylint: disable=E1101
            ):
                continue

            name: str = Config.get_item(  # type: ignore
                function,
                Config.Column.Name.name,  # pylint: disable=E1101
            )
            print(name, end=", ")  # noqa: WPS421
        print()  # noqa: WPS421

    @staticmethod
    def echo_input(in_string: str) -> None:  # pragma: no cover  # noqa: WPS602, WPS605
        """Print value in configured types."""
        pre: str = ""
        end: str = "\n"

        if Config.option[Config.Option.is_pipe]:  # type: ignore  # pylint: disable=E1101
            pre = "\n"
            end = " = "

        if Config.option[Config.Option.echo_in]:  # type: ignore  # pylint: disable=E1101
            print(f"{pre}{in_string}", end=end)  # noqa: WPS421

    @staticmethod
    def print_line() -> None:  # pragma: no cover  # noqa: WPS602, WPS605
        """Print value in configured types."""
        in_val: Union[int, float]
        val_int: int = Memory.value_dict[Config.ValueNS.int]  # type: ignore  # pylint: disable=E1101 # noqa: E501
        val_float: float = Memory.value_dict[Config.ValueNS.float]  # type: ignore  # pylint: disable=E1101  # noqa: E501

        if not isinstance(val_int, int):
            return  # type: ignore

        if Config.option[Config.Option.was_noop]:  # type: ignore  # pylint: disable=E1101
            Config.option[Config.Option.was_noop] = False  # type: ignore  # pylint: disable=E1101
            if Config.option[Config.Option.is_pipe]:  # type: ignore  # pylint: disable=E1101
                return

        for function in Config.row_list:
            if not Config.get_item(  # noqa: WPS337
                function,
                Config.Column.print_it.name,  # pylint: disable=E1101
            ):
                continue

            func: Callable = Config.get_item(  # type: ignore
                function,
                Config.Column.Function.name,  # pylint: disable=E1101
            )

            in_val = (
                val_float
                if Config.get_item(  # noqa: WPS337
                    function,
                    Config.Column.is_float.name,  # pylint: disable=E1101
                )
                else val_int
            )
            print(func(in_val), end=", ")  # noqa: WPS421
