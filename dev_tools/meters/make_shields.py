#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculate LOC and update Shield JSON."""

import json
import os
from typing import List

cloc_sink: str = "dev_tools/meters"

pre_cmd: str = "cd $(git rev-parse --show-toplevel)"
work_dir_cmd: str = f"{pre_cmd} ; pwd"

stream: str = os.popen(work_dir_cmd)  # noqa: S605
work_dir: str = stream.read().strip()

cloc_cmd: str = "cloc"
cloc_arg: str = "--include-lang Python --quiet --json --report-file"

dirs: List[str] = [
    "cli_calc",
    "tests",
]

ext: str = "json"
shield_str: str = "shields"

cmd: str = ""
cloc_in: str
cloc_out: str
shield_out: str
cloc: str
shield: str
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
        new_loc = cloc["Python"]["code"]

    with open(shield_out, "r") as read_shield:
        shield = json.load(read_shield)
        shield["message"] = str(new_loc)

    if shield:
        with open(shield_out, "w") as write_shield:
            json.dump(shield, write_shield)

print("LOC updated.")  # noqa: WPS421
