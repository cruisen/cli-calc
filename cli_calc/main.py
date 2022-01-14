#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CLI Calculator.

* Provide the python math library
  as well as standard math parsing / eval to CLI.
* Setup and Main loop.
"""


import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # noqa: WPS221


from cli_calc.cli_output import Output  # pylint: disable=C0413  # noqa: E402
from cli_calc.config import Config  # pylint: disable=C0413  # noqa: E402
from cli_calc.memory import Memory  # pylint: disable=C0413  # noqa: E402
from cli_calc.read_line_parser import (  # pylint: disable=C0413  # noqa: E402
    ReadLineParser,
)


def cli_start() -> None:  # pragma: no cover
    """Prepare the CLI."""
    Output.print_help()
    Output.print_line()


def io_loop() -> None:  # pragma: no cover
    """
    Main IO Loop.

    Handle CTRL-C.
    """
    try:
        while True:  # noqa: WPS457
            ReadLineParser.input_cli()
            Output.print_line()
    except KeyboardInterrupt:
        sys.exit(0)


def main() -> None:  # pragma: no cover
    """Main."""
    Config.init(Memory.value_dict)
    cli_start()
    io_loop()


if __name__ == "__main__":  # pragma: no cover
    main()
