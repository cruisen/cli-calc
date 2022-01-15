# -*- coding: utf-8 -*-
"""CLI Eval."""


import cmath  # pylint: disable=W0611  # noqa: F401
import math  # pylint: disable=W0611  # noqa: F401
import random  # pylint: disable=W0611  # noqa: F401
from math import *  # pylint: disable=W0622, W0401, W0614 # noqa: F403, F401, WPS347, WPS458, E501
from random import *  # type: ignore  # pylint: disable=W0622, W0401, W0614 # noqa: F403, F401, WPS347, WPS458, E501, WPS440
from typing import Optional, Union

from cli_calc.cli_output import Output


class Eval:  # pylint: disable=R0903
    """
    CLI Eval.

    With "from math import *":
    This is the magic. Using "eval", so python does the heavy lifting.

    And "import math" for help(math).

    WARNING: using "eval" is *evil*, and dangerous.
    However all space is trimmed in calling script,
    so less easy to execute shell commands.
    """  # noqa: RST213

    @staticmethod
    def eval_string(  # noqa: WPS602
        in_string: Optional[str],
    ) -> Optional[Union[int, float]]:
        """
        Evaluate the input string.

        Note: eval is NOT safe. Use with care.
        """
        out_obj: Optional[Union[int, float]] = None

        if in_string is None or len(in_string) == 0:  # noqa: WPS507
            return None

        Output.echo_input(in_string)

        try:
            out_obj = eval(  # pylint: disable=W0123  # noqa: S307, WPS421
                in_string,
                globals(),  # noqa: WPS421
            )
        except (NameError, TypeError, SyntaxError) as err:
            print(f"{type(err).__name__}: {err}")  # noqa: WPS237, WPS421
            Output.print_help()
            return None

        # int: +0 == -0, but float +0 != -0
        if out_obj == 0 and in_string == "-0":
            out_obj = -0.0  # noqa: WPS358

        return out_obj
