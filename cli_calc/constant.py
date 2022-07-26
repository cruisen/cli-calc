# -*- coding: utf-8 -*-
"""Configure config argparse."""

import os

from importlib_metadata import distribution, metadata
from python_git_wrapper import Repository


class Constant:
    """Constants."""

    MODULE_PATH = os.path.basename(os.getcwd())  # noqa: WPS115
    MODULE = distribution(MODULE_PATH)  # type: ignore # noqa: WPS115

    SCRIPT_NAME: str = MODULE.metadata["Name"]  # noqa: WPS115
    SCRIPT_VERSION: str = MODULE.metadata["Version"]  # noqa: WPS115
    SCRIPT_AUTHOR: str = MODULE.metadata["Author"]  # noqa: WPS115
    SCRIPT_URL: str = MODULE.metadata["Home-page"]  # noqa: WPS115
    SCRIPT_LICENSE: str = MODULE.metadata["License"]  # noqa: WPS115
    SCRIPT_SUMMARY: str = MODULE.metadata["Summary"]  # noqa: WPS115

    repository = Repository(".")
    COMMIT_LAST_DATE = (  # noqa: WPS115
        repository.execute("show --no-patch --no-notes --pretty='%as'").strip().replace("'", "")
    )
    COMMIT_FIRST_DATE = (  # noqa: WPS115
        repository.execute("log --no-patch --no-notes --pretty='%as' --reverse")
        .strip()
        .replace("'", "")
        .split("\n", 1)[0]
    )

    COMMIT_LAST = COMMIT_LAST_DATE.split("-", 1)[0]  # noqa: WPS115
    COMMIT_FIRST = COMMIT_FIRST_DATE.split("-", 1)[0]  # noqa: WPS115

    @staticmethod
    def show_meta_data() -> None:  # noqa: WPS602, WPS605  # pragma: no cover
        """Show META data."""
        for meta in list(metadata(Constant.MODULE_PATH)):
            if "Description" in meta or "Classifier" in meta:
                continue
            print(f"{meta}: {Constant.MODULE.metadata[meta]}")  # noqa: WPS421, WPS237
