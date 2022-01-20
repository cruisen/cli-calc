#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculate LOC and update Shield JSON."""

import json
import os
from typing import List, Optional

dirs: List[str] = [
    "cli_calc",
    "tests",
    "dev_tools",
]

cloc_sink: str = "dev_tools/meters"

pre_cmd: str = "cd $(git rev-parse --show-toplevel)"
work_dir_cmd: str = f"{pre_cmd} ; pwd"

stream: os._wrap_close = os.popen(work_dir_cmd)  # pylint: disable=W0212  # noqa: S605, WPS437
work_dir: str = stream.read().strip()

cloc_cmd: str = "cloc"
cloc_arg: str = "--include-lang Python --quiet --json --report-file"

ext: str = "json"
shield_str: str = "shields"

cmd: str = ""
cloc_in: str
cloc_out: str
shield_out: str
cloc: str
shield_data: Optional[str]
new_loc: str

for sub_dir in dirs:
    cloc_in = f"{work_dir}/{sub_dir}"
    cloc_out = f"{work_dir}/{cloc_sink}/{sub_dir}.{ext}"
    shield_out = f"{work_dir}/{cloc_sink}/{sub_dir}_{shield_str}.{ext}"  # noqa: WPS221

    cmd = f"{cloc_cmd} {cloc_arg}={cloc_out} {cloc_in}"
    cmd = f"{pre_cmd} ; {cmd}"

    os.system(cmd)  # noqa: S605

    with open(cloc_out, "r") as read_cloc:
        cloc = json.load(read_cloc)
        new_loc = str(cloc["Python"]["code"])  # type: ignore  # pylint: disable=C0103

    try:
        with open(shield_out, "r") as read_shield:
            shield_data = json.load(read_shield)
            shield_data["message"] = str(new_loc)  # type: ignore
    except FileNotFoundError:
        print(f"{shield_out}")  # noqa: WPS421
        print("Error: File not found. Create one ...")  # noqa: WPS421
        shield_data = None  # pylint: disable=C0103

    if shield_data:
        with open(shield_out, "w") as write_shield:
            json.dump(shield_data, write_shield)

print("LOC updated.")  # noqa: WPS421
