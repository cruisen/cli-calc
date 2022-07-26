# -*- coding: utf-8 -*-
"""Configure config argparse."""

import os

from importlib_metadata import distribution, metadata
from python_git_wrapper import Repository


class Constant:

    _module = os.path.basename(os.getcwd())
    _dist = distribution(_module)  # type: ignore

    SCRIPT_NAME: str = _dist.metadata["Name"]
    SCRIPT_VERSION: str = _dist.metadata["Version"]
    SCRIPT_AUTHOR: str = _dist.metadata["Author"]
    SCRIPT_URL: str = _dist.metadata["Home-page"]
    SCRIPT_LICENSE: str = _dist.metadata["License"]
    SCRIPT_SUMMARY: str = _dist.metadata["Summary"]

    repository = Repository(".")
    COMMIT_LAST_DATE = (
        repository.execute("show --no-patch --no-notes --pretty='%as'").strip().replace("'", "")
    )
    COMMIT_FIRST_DATE = (
        repository.execute("log --no-patch --no-notes --pretty='%as' --reverse")
        .strip()
        .replace("'", "")
        .split("\n", 1)[0]
    )

    COMMIT_LAST = COMMIT_LAST_DATE.split("-", 1)[0]
    COMMIT_FIRST = COMMIT_FIRST_DATE.split("-", 1)[0]

    def show_meta_data() -> None:
        for meta in list(metadata(Constant._module)):
            if "Description" in meta or "Classifier" in meta:
                continue
            print(f"{meta}: {Constant._dist.metadata[meta]}")
