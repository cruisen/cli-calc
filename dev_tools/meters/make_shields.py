#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculate LOC and update Shield JSON."""

import json
import os
from typing import List, Optional, Tuple


class Shield:  # pylint: disable=R0903
    """Calculate LOC and update Shield JSON."""

    pre_cmd: str = "cd $(git rev-parse --show-toplevel)"

    @staticmethod
    def provide_work_dir() -> str:  # pylint: disable=R0914  # noqa: WPS602, WPS605, WPS210
        """Get the root dir of the project."""
        work_dir_cmd: str = f"{Shield.pre_cmd} ; pwd"

        stream: os._wrap_close = os.popen(  # pylint: disable=W0212  # noqa: S605, WPS437
            work_dir_cmd,
        )
        return stream.read().strip()

    @staticmethod
    def compose_cmd_and_path(  # pylint: disable=R0914  # noqa: WPS602, WPS605, WPS210
        work_dir: str,
        sub_dir: str,
    ) -> Tuple[str, str, str]:
        """Compose cloc cmd."""
        ext: str = "json"

        cloc_sink: str = "dev_tools/meters"
        cloc_cmd: str = "cloc"

        cloc_in: str = f"{work_dir}/{sub_dir}"
        cloc_out: str = f"{work_dir}/{cloc_sink}/{sub_dir}.{ext}"  # noqa: WPS221

        cloc_arg: str = "--include-lang Python --quiet --json --report-file"

        shield_str: str = "shields"
        shield_out = f"{work_dir}/{cloc_sink}/{sub_dir}_{shield_str}.{ext}"  # pylint: disable=C0301  # noqa: WPS221, E501

        cmd: str = f"{cloc_cmd} {cloc_arg}={cloc_out} {cloc_in}"
        cmd = f"{Shield.pre_cmd} ; {cmd}"

        return cmd, cloc_out, shield_out

    @staticmethod
    def calculate_loc_and_write_to_json(  # pylint: disable=R0914  # noqa: WPS602, WPS605, WPS210
        cmd: str,
    ) -> None:
        """
        Retrieve LOC from source files.

        By using ```cloc```.
        """
        os.system(cmd)  # noqa: S605

    @staticmethod
    def read_loc_from_json(  # pylint: disable=R0914  # noqa: WPS602, WPS605, WPS210
        cloc_out: str,
    ) -> str:
        """Read LOC from JSON."""
        cloc: str

        with open(cloc_out, "r") as read_cloc:
            cloc = json.load(read_cloc)
            return str(cloc["Python"]["code"])  # type: ignore  # pylint: disable=C0103

    @staticmethod
    def update_loc_data(  # pylint: disable=R0914  # noqa: WPS602, WPS605, WPS210
        shield_out: str,
        new_loc: str,
    ) -> Optional[str]:
        """Update LOC in JSON data."""
        shield_data: Optional[str]

        try:
            with open(shield_out, "r") as read_shield:
                shield_data = json.load(read_shield)
                shield_data["message"] = str(new_loc)  # type: ignore
        except FileNotFoundError:
            print(f"{shield_out}")  # noqa: WPS421
            print("Error: File not found. Create one ...")  # noqa: WPS421
            shield_data = None  # pylint: disable=C0103

        return shield_data

    @staticmethod
    def write_loc_to_json(  # pylint: disable=R0914  # noqa: WPS602, WPS605, WPS210
        shield_out: str,
        shield_data: Optional[str],
    ) -> None:
        """Write LOC to JSON."""
        if shield_data:
            with open(shield_out, "w") as write_shield:
                json.dump(shield_data, write_shield)

    @staticmethod
    def run_pre_commit():  # pylint: disable=R0914  # noqa: WPS602, WPS605, WPS210
        stream = os.popen("poetry run git add . ; poetry run pre-commit ; poetry run git add . ; poetry run pre-commit")  # noqa: S605, S607
        output: str = stream.read().strip()

    @staticmethod
    def worker() -> None:  # pylint: disable=R0914  # noqa: WPS602, WPS605, WPS210
        """."""
        sub_dir: str

        cmd: str = ""
        cloc_out: str
        shield_out: str
        new_loc: str
        shield_data: Optional[str]

        dirs: List[str] = [
            "cli_calc",
            "tests",
            "dev_tools",
        ]

        work_dir: str = Shield.provide_work_dir()

        for sub_dir in dirs:
            cmd, cloc_out, shield_out = Shield.compose_cmd_and_path(work_dir, sub_dir)

            Shield.calculate_loc_and_write_to_json(cmd)

            new_loc = Shield.read_loc_from_json(cloc_out)
            shield_data = Shield.update_loc_data(shield_out, new_loc)
            Shield.write_loc_to_json(shield_out, shield_data)

        Shield.run_pre_commit()


def main() -> None:
    """Main function."""
    Shield.worker()
    print("LOC updated.")  # noqa: WPS421


if __name__ == "__main__":
    main()
