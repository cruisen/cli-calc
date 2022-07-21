#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CLI Calculator.

* print help
"""

import os
import sys
from contextlib import redirect_stdout

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # noqa: WPS221 # pragma: no cover


from cli_calc.cli_output import Output  # pylint: disable=C0413  # noqa: E402
from cli_calc.config import Config  # pylint: disable=C0413  # noqa: E402
from cli_calc.memory import Memory  # pylint: disable=C0413  # noqa: E402


def main() -> None:  # pragma: no cover
    """Main."""
    Config.init(Memory.value_dict)
    with open("help.txt", "w") as file_handle:
        with redirect_stdout(file_handle):
            Output.print_help()


if __name__ == "__main__":  # pragma: no cover
    main()
