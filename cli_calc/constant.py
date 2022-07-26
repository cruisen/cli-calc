# -*- coding: utf-8 -*-
"""Configure config argparse."""

import os
from importlib_metadata import distribution, metadata


class Constant:

        _module = os.path.basename(os.getcwd())
        _dist = distribution(_module)

        SCRIPT_NAME: str = _dist.metadata["Name"]
        SCRIPT_VERSION: str = _dist.metadata["Version"]
        SCRIPT_AUTHOR: str = _dist.metadata["Author"]
        SCRIPT_URL: str = _dist.metadata["Home-page"]
        SCRIPT_LICENSE: str = _dist.metadata["License"]
        SCRIPT_SUMMARY: str = _dist.metadata["Summary"]


        def show_meta_data():
            for meta in list(metadata(Constant._module)):
                if "Description" in meta or "Classifier" in meta:
                    continue
                print(f"{meta}: {Constant._dist.metadata[meta]}")




