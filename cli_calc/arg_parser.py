# -*- coding: utf-8 -*-
"""Configure config argparse."""


import configargparse

argparser = configargparse.ArgParser(default_config_files=["~/.my_settings"])


class Parser:
    """Parser for CLI."""

    @staticmethod
    def init() -> None:  # noqa: WPS602, WPS605
        """Init."""
        # Parser.add_arguments()  # noqa: E800
        # Parser.test()  # noqa: E800

    @staticmethod
    def add_arguments() -> None:  # noqa: WPS602, WPS605  # pragma: no cover
        """Add arguments."""
        argparser.add(
            "-c",
            "--my-config",
            required=True,
            is_config_file=True,
            help="config file path",
        )
        argparser.add("--genome", required=True, help="path to genome file")
        argparser.add("-v", help="verbose", action="store_true")
        argparser.add("-d", "--dbsnp", help="known variants .vcf", env_var="DBSNP_PATH")
        argparser.add("vcf", nargs="+", help="variant file(s)")

    @staticmethod
    def test() -> None:  # noqa: WPS602, WPS605  # pragma: no cover
        """Test."""
        options = argparser.parse_args()

        print(options)  # noqa: WPS421
        print("----------")  # noqa: WPS421
        print(argparser.format_help())  # noqa: WPS421
        print("----------")  # noqa: WPS421
        print(argparser.format_values())  # noqa: WPS421
