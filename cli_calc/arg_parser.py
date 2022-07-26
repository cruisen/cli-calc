# -*- coding: utf-8 -*-
"""Configure config argparse."""

import configargparse

p = configargparse.ArgParser(default_config_files=["~/.my_settings"])

class Parser:

    def init():
        from importlib_metadata import distribution
        dist = distribution("cli-calc")
        print(__name__)
        print(dist.version)
        print(dist.name)


    def add_arguments():
        p.add("-c", "--my-config", required=True, is_config_file=True, help="config file path")
        p.add("--genome", required=True, help="path to genome file")
        p.add("-v", help="verbose", action="store_true")
        p.add("-d", "--dbsnp", help="known variants .vcf", env_var="DBSNP_PATH")
        p.add("vcf", nargs="+", help="variant file(s)")

    def test():
        options = p.parse_args()

        print(options)
        print("----------")
        print(p.format_help())
        print("----------")
        print(p.format_values())
