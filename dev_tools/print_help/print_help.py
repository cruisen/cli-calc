#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CLI Calculator.

* print help
"""

import os
import sys
from contextlib import redirect_stdout
from shutil import move
from tempfile import NamedTemporaryFile

from cli_calc.cli_output import Output  # pylint: disable=C0413  # noqa: E402
from cli_calc.config import Config  # pylint: disable=C0413  # noqa: E402
from cli_calc.memory import Memory  # pylint: disable=C0413  # noqa: E402

ROOT_DIR = sys.path[-1]
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


help_file_path: str = f"{SCRIPT_DIR}/help.txt"
prompt_file_path: str = f"{SCRIPT_DIR}/prompt.txt"

readme_file_path: str = f"{ROOT_DIR}/README.md"

temp_file_path: str = NamedTemporaryFile("w", dir=".", delete=False).name

prompt_old: str = "hex, int, float,"

help_old_start = ["```bash", "cli-calc", "h", "INPUT:"]
help_old_len = len(help_old_start)
help_old_end = "```"


def handle_files() -> None:  # noqa: WPS210, C901, WPS231
    """Handle stdout and files."""
    signature: int = 0
    signature_line: int = 0
    replace: bool = False

    # Get Help from app
    with open(help_file_path, "w") as help_file_handle:
        with redirect_stdout(help_file_handle):
            Output.print_help()

    # Save Help from app
    with open(help_file_path, "r") as help_file_handle:  # noqa: WPS440
        last_line: str = help_file_handle.readlines()[-1]

    # Save Prompt from app
    with open(prompt_file_path, "w") as prompt_file_handle:
        prompt_file_handle.writelines(last_line)

    # Get Readme.md, replace lines and save in temp file
    with open(readme_file_path, "r") as readme_file_handle:
        lines = readme_file_handle.readlines()
        size_old = len(lines)

        with open(temp_file_path, "w") as temp_file_handle:
            for number, line in enumerate(lines):
                if prompt_old in line:
                    line = last_line  # noqa: WPS440

                for test_line in help_old_start:
                    if test_line.lower() == line.strip("\n").lower():
                        if signature == 0 or signature_line + 1 == number:  # noqa: WPS220
                            signature += 1
                            signature_line = number  # noqa: WPS220
                        else:
                            signature = 0  # noqa: WPS220

                if signature >= help_old_len:
                    replace = True
                    signature = 0
                    with open(help_file_path, "r") as help_file_handle:  # noqa: WPS440
                        help_lines = help_file_handle.readlines()  # noqa: WPS220
                        for help_line in help_lines:  # noqa: WPS220
                            temp_file_handle.write(help_line)  # noqa: WPS220

                if help_old_end == line.strip("\n"):
                    replace = False

                if not replace:
                    temp_file_handle.write(line)

    # Get temp file for size
    with open(temp_file_path, "r") as temp_file_handle:  # noqa: WPS440
        lines = temp_file_handle.readlines()
        size_new = len(lines)

    # only replace if changes in number of lines are minimal
    if abs(size_old - size_new) <= 2:
        move(temp_file_path, readme_file_path)
    else:
        raise ResourceWarning(
            f"{temp_file_path} is too differnt from {readme_file_path}. Please check.",
        )


def main() -> None:  # pragma: no cover
    """Main."""
    Config.init(Memory.value_dict)
    handle_files()


if __name__ == "__main__":  # pragma: no cover
    main()
