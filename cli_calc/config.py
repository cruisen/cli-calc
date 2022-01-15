# -*- coding: utf-8 -*-


"""Configuration.

ToDo: add Jason or like
"""

from enum import Enum, auto
from typing import Callable, Dict, List, Union

from cli_calc.format import Format
from cli_calc.ieee import IEEE


class EnumAuto(Enum):  # noqa: WPS431  # noqa: WPS431
    """
    Enum class for Headings.

    Configured to start with 0 (Zero), instead of 1.
    """

    def _generate_next_value_(  # pylint: disable=E0213  # noqa: WPS120
        name,  # noqa: N805
        start,  # pylint: disable=W0613
        count,  # pylint: disable=W0613
        last_values,  # pylint: disable=W0613
    ):
        return count


class Config:  # noqa: WPS214
    """
    Configuration.

    * Handle Configuration
    * Provide Enums and Class Name Spaces to avoid test attribute typos.
       * Dynamically create these based and standard config data.
    """

    DIVIDER_LINE_LENGTH = 50  # noqa: WPS115

    class Column(EnumAuto):  # noqa: WPS431  # noqa: WPS431
        """Enum for Column Headings."""

        Name = auto()  # noqa: WPS115
        Function = auto()  # noqa: WPS115
        Short = auto()  # noqa: WPS115
        print_it = auto()
        is_float = auto()

    table: List[List[Union[str, Callable, bool]]] = [  # type: ignore  # noqa: WPS234, E501
        ["hex", hex, "x", True, False],
        ["oct", oct, "o", False, False],
        ["bin", bin, "b", False, False],
        ["int", int, "i", True, False],
        ["float", float, "", True, True],
        ["fraction", float, "f", False, True],
        ["truth", bool, "t", False, False],
        ["to_ieee", float, "e", False, True],
        ["to_ieee_bin", float, "n", False, True],
        ["from_ieee", float, "r", False, False],
    ]

    option: Dict[str, bool] = {  # noqa: WPS234, E501
        "print_help": True,
        "print_header": True,
        "echo_in": True,
        "is_pipe": False,
        "was_noop": False,
    }

    row_list: List[str] = []
    option_list: List[str] = []
    arg_dict: Dict[str, str] = {}

    class Row:  # pylint: disable=R0903  # noqa: WPS431
        """
        Namespace for Row Headers.

        To avoid typos.
        Auto generate on Config.init().
        """

    class Option:  # pylint: disable=R0903  # noqa: WPS431
        """
        Namespace for Option Headers.

        To avoid typos.
        Auto generate on Config.init().
        """

    class ValueNS:  # pylint: disable=R0903  # noqa: WPS431
        """
        Namespace for Value Types.

        To avoid typos.
        Auto generate on Config.init().
        """

    @staticmethod
    def create_value_namespace(  # noqa: WPS602
        value_dict: Dict[str, Union[int, float]],
    ) -> None:  # noqa: WPS602, WPS605
        """Create a List for Value Name mapping."""
        for val_row in value_dict:
            setattr(Config.ValueNS, val_row, val_row)

    @staticmethod
    def create_option_namespace() -> None:  # noqa: WPS602, WPS605
        """Create a Simple Namespace for Option Name mapping."""
        for option in Config.option:
            setattr(Config.Option, option, option)

    @staticmethod
    def create_row_list() -> None:  # noqa: WPS602, WPS605, WPS602
        """Create a List for Row Name mapping."""
        for list_row in Config.table:
            Config.row_list.append(str(list_row[0]))

    @staticmethod
    def create_row_namespace() -> None:  # noqa: WPS602, WPS605
        """Create a Simple Namespace for Row Header Name mapping."""
        for row in Config.row_list:
            setattr(Config.Row, row, row)

    @staticmethod
    def create_arg_dict() -> None:  # noqa: WPS602, WPS605
        """Create a Dict for Argument Name mapping."""
        name: str
        short: str
        for function in Config.row_list:
            name = Config.get_item(
                function,
                Config.Column.Name.name,  # type: ignore  # pylint: disable=E1101  # noqa: E501
            )
            short = Config.get_item(
                function,
                Config.Column.Short.name,  # type: ignore  # pylint: disable=E1101  # noqa: E501
            )
            if short:
                Config.arg_dict[short] = name

    @staticmethod
    def get_col_number(col: str) -> int:  # noqa: WPS602, WPS605
        """Get Column Number for given string."""
        return Config.Column[col].value

    @staticmethod
    def get_row_number(row: str) -> int:  # noqa: WPS602, WPS605
        """Get Row Number for given string."""
        return Config.row_list.index(row)

    @staticmethod
    def get_item(  # noqa: WPS602, WPS605, WPS615
        row: str,
        col: str,
    ) -> Union[Callable, str, bool]:  # type: ignore
        """Get List Item for given row and column names."""
        return Config.table[Config.get_row_number(row)][Config.get_col_number(col)]  # noqa: E501

    @staticmethod
    def set_item(  # noqa: WPS602, WPS605, WPS615
        row: str,
        col: str,
        set_value: Union[Callable, str, bool],  # type: ignore
    ) -> None:
        """Set List Item for given row and column names."""
        Config.table[Config.get_row_number(row)][
            Config.get_col_number(col)
        ] = set_value  # noqa: E501

    @staticmethod
    def init(  # noqa: WPS602, WPS213
        value_dict: Dict[str, Union[int, float]],
    ) -> None:  # noqa: WPS213, WPS602, WPS605
        """Init globals."""
        Config.create_row_list()

        Config.create_value_namespace(value_dict)
        Config.create_row_namespace()
        Config.create_option_namespace()

        Config.create_arg_dict()

        Config.set_item(
            Config.Row.fraction,  # type: ignore  # pylint: disable=E1101
            Config.Column.Function.name,  # pylint: disable=E1101
            Format.get_fraction,
        )
        Config.set_item(
            Config.Row.to_ieee,  # type: ignore  # pylint: disable=E1101
            Config.Column.Function.name,  # pylint: disable=E1101
            IEEE.float_to_ieee_hex,
        )
        Config.set_item(
            Config.Row.to_ieee_bin,  # type: ignore  # pylint: disable=E1101
            Config.Column.Function.name,  # pylint: disable=E1101
            IEEE.float_to_ieee_bin,
        )
        Config.set_item(
            Config.Row.from_ieee,  # type: ignore  # pylint: disable=E1101
            Config.Column.Function.name,  # pylint: disable=E1101
            IEEE.ieee_to_float,
        )
