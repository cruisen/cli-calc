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

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # noqa: WPS221 # pragma: no cover


from cli_calc.cli_output import Output  # pylint: disable=C0413  # noqa: E402
from cli_calc.config import Config  # pylint: disable=C0413  # noqa: E402
from cli_calc.input import Input  # pylint: disable=C0413  # noqa: E402
from cli_calc.memory import Memory  # pylint: disable=C0413  # noqa: E402


class Main:
    """Main."""

    @staticmethod
    def io_loop() -> None:  # pragma: no cover  # noqa: WPS602, WPS605
        """
        Main IO Loop.

        Handle CTRL-C.
        """
        try:
            while True:  # noqa: WPS457
                Input.get_line()
                Output.print_line()
        except KeyboardInterrupt:
            sys.exit(0)

    @staticmethod
    def main() -> None:  # pragma: no cover  # noqa: WPS602, WPS605
        """Main."""
        Config.init(Memory.value_dict)
        Input.init_output()
        Main.io_loop()


if __name__ == "__main__":  # pragma: no cover
    Main.main()
