# -*- coding: utf-8 -*-
"""Test input parsing and eval functions with pytest."""

import pytest  # pylint: disable=E0401

from cli_calc.cli_input import Input  # pylint: disable=E0401
from cli_calc.config import Config  # pylint: disable=E0401
from cli_calc.memory import Memory  # pylint: disable=E0401

Config.init(Memory.value_dict)


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string", "name", "expected"),
    [
        ("+x", Config.Row.hex, True),  # type: ignore
        ("-x", Config.Row.hex, False),  # type: ignore
        ("+b", Config.Row.bin, True),  # type: ignore
        ("-b", Config.Row.bin, False),  # type: ignore
        ("+o", Config.Row.oct, True),  # type: ignore
        ("-o", Config.Row.oct, False),  # type: ignore
        ("+i", Config.Row.int, True),  # type: ignore
        ("-i", Config.Row.int, False),  # type: ignore
        ("+f", Config.Row.fraction, True),  # type: ignore
        ("-f", Config.Row.fraction, False),  # type: ignore
        ("+t", Config.Row.truth, True),  # type: ignore
        ("-t", Config.Row.truth, False),  # type: ignore
        ("-e", Config.Row.to_ieee, False),  # type: ignore
        ("+e", Config.Row.to_ieee, True),  # type: ignore
        ("-n", Config.Row.to_ieee_bin, False),  # type: ignore
        ("+n", Config.Row.to_ieee_bin, True),  # type: ignore
        ("-r", Config.Row.from_ieee, False),  # type: ignore
        ("+r", Config.Row.from_ieee, True),  # type: ignore
    ],
)
def test_handle_input(  # noqa: WPS602
    in_string: str,
    name: str,
    expected: float,
):
    """Input to Output test."""
    Input.handle_input(in_string)

    status: bool = Config.get_item(
        name,
        Config.Column.print_it.name,  # type: ignore  # pylint: disable=E1101
    )
    assert status == expected  # noqa: S101


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string", "expected"),
    [
        ("h", None),
        ("x", "x"),
        ("xx", "xx"),
    ],
)
def test_parse_argumnents(  # noqa: WPS602
    in_string: str,
    expected: str,
):
    """Input to Output test."""
    assert Input.parse_argumnents(in_string) == expected  # noqa: S101


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string"),
    [
        ("q"),
    ],
)
def test_parse_argumnents_for_quit(  # noqa: WPS602
    in_string: str,
):
    """Input to sys.exit() test."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        Input.parse_argumnents(in_string)
    assert pytest_wrapped_e.type == SystemExit  # noqa: S101, WPS441
    assert pytest_wrapped_e.value.code == 1  # noqa: S101, WPS441


@pytest.mark.parametrize(  # noqa: WPS317
    ("in_string", "expected"),
    [
        (None, None),
        ("1", "1"),
        ("12", "12"),
        ("123", "123"),
        ("x", "x"),
        ("xx", "xx"),
        ("xxx", "xxx"),
        ("-+", "-+"),
        ("+-", "+-"),
        ("++", "++"),
        ("--", "--"),
        ("a-", "a-"),
        ("+a", "+a"),
    ],
)
def test_parse_display(  # noqa: WPS602
    in_string: str,
    expected: str,
):
    """Input to Output test."""
    assert Input.parse_display(in_string) == expected  # noqa: S101
