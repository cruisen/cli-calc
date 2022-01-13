# -*- coding: utf-8 -*-
"""Memory."""

from typing import Dict, Union


class Memory:  # pylint: disable=R0903
    """
    Memory.

    * Provide memory for the math result.
    """

    value_dict: Dict[str, Union[int, float]] = {
        "int": 0,
        "float": 0.0,  # noqa: WPS358
    }
