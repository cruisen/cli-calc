![Logo](https://raw.githubusercontent.com/cruisen/cli-calc/4986df3abb3f1871d6669dec27d5e37aba0d11a3/assets/images/Cli-Calc.png)

# cli-calc

[![test](https://github.com/cruisen/cli-calc/actions/workflows/test.yml/badge.svg)](https://github.com/cruisen/cli-calc/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cruisen/cli-calc/branch/main/graph/badge.svg?token=i9nYZL3MM3)](https://codecov.io/gh/cruisen/cli-calc)
[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)

[![pypi](https://img.shields.io/pypi/v/cli-calc)](https://pypi.org/project/cli-calc/)
[![github release](https://img.shields.io/github/release-date/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/releases)
[![pypi downloads](https://img.shields.io/pypi/dm/cli-calc?label=pypi%20downloads)](https://pypi.org/project/cli-calc/)

Powerful yet easy command line calculator.

## Example Usage

```
cos(pi/2)
0xFF ^ 0b10
2**8-1
log(2)
comb(49,6)
factorial(42)
random()
cmath.phase(complex(-1.0, 0.0))
```

## Math Libraries ready to use out of the box
- [standard operators](https://www.w3schools.com/python/python_operators.asp)
- [standard math library](https://docs.python.org/3/library/math.html)

- [cmath](https://docs.python.org/3/library/cmath.html)
- [random](https://docs.python.org/3/library/random.html#examples) 

- [built in functions](https://docs.python.org/3/library/functions.html) 


# Installation

```bash
pip install cli-calc
```

- [pypi cli-calc](https://pypi.org/project/cli-calc/).

## Configuration

In order to run it from anywhere: Add a symbolic link in ~/bin

```bash
cd ~/bin
ln -s ~/path/to/your/install/cli_calc/warpper.sh calc
```

Then use it anywhere. :-)

```bash
calc
echo "7+8" | calc
cat foo.bar | calc
```

## Help

```bash
calc
h
Input:
    "q" for quit, "h" for help

    "_float_" and/or "_int_" for last value
    "pi", "tau" and "e" for pi, tau and Euler

    "+f" to add display for fraction, "-f" to suppress display for fraction
        Other letters are:
        he(x), (o)ctal, (b)inary, (i)nteger,
        (f)raction, (t)ruth, i(e)ee, ieee_bi(n), f(r)om_ieee
        "float" is always visible

    See https://docs.python.org/3/library/math.html, use without "math."
        https://www.w3schools.com/python/python_operators.asp

    Try "cos(pi/2)", XOR: "0xFF ^ 0b10", "2**8-1", "factorial(42)",
        "help(math)"
```

## Warning

Use of [eval](https://docs.python.org/3/library/functions.html#eval) is evil.

However some precautions are taken.


# For developers only :-)

## Metric Dashboard

[![test](https://github.com/cruisen/cli-calc/actions/workflows/test.yml/badge.svg)](https://github.com/cruisen/cli-calc/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cruisen/cli-calc/branch/main/graph/badge.svg?token=i9nYZL3MM3)](https://codecov.io/gh/cruisen/cli-calc)
[![SLOC](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/cruisen/cli-calc/main/dev_tools/meters/cli_calc_shields.json)](https://github.com/cruisen/cli-calc/tree/main/cli_calc)
[![SLOC Tests](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/cruisen/cli-calc/main/dev_tools/meters/tests_shields.json)](https://github.com/cruisen/cli-calc/tree/main/tests)

[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)
[![Python Lang](https://img.shields.io/github/languages/top/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/search?l=python)
[![Languages](https://img.shields.io/github/languages/count/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/search?l=python)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/cruisen/cli-calc/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/cruisen/cli-calc/?branch=main)
[![Requirements Status](https://requires.io/github/cruisen/cli-calc/requirements.svg?branch=main)](https://requires.io/github/cruisen/cli-calc/requirements/?branch=main)
[![Dependencies](https://img.shields.io/librariesio/release/github/cruisen/cli-calc)](https://libraries.io/github/cruisen/cli-calc)

[![pypi](https://img.shields.io/pypi/v/cli-calc)](https://pypi.org/project/cli-calc/)
[![github release](https://img.shields.io/github/release-date/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/releases)
[![pypi downloads](https://img.shields.io/pypi/dm/cli-calc?label=pypi%20downloads)](https://pypi.org/project/cli-calc/)

[![last commit](https://img.shields.io/github/last-commit/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/commits/main)
[![github commits](https://img.shields.io/github/commit-activity/m/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/commits/main)
[![code size](https://img.shields.io/github/languages/code-size/cruisen/cli-calc)](https://github.com/cruisen/cli-calc.git)
[![github downloads](https://img.shields.io/github/downloads/cruisen/cli-calc/total?label=github%20downloads)](https://github.com/cruisen/cli-calc)

[![github help open](https://img.shields.io/github/issues-raw/cruisen/cli-calc/need_Help?color=yellow&label=need%20help)](https://github.com/cruisen/cli-calc/issues?q=is%3Aopen+is%3Aissue+label%3Aneed_Help)
[![github bugs open](https://img.shields.io/github/issues-raw/cruisen/cli-calc/is_Bug?color=red&label=bugs)](https://github.com/cruisen/cli-calc/issues?q=is%3Aopen+is%3Aissue+label%3Ais_Bug)
[![github bugs closed](https://img.shields.io/github/issues-closed-raw/cruisen/cli-calc/is_Bug?color=green&label=closed)](https://github.com/cruisen/cli-calc/issues?q=is%3Aissue+is%3Aclosed+label%3Ais_Bug)
[![github issues open](https://img.shields.io/github/issues-raw/cruisen/cli-calc?color=blue)](https://github.com/cruisen/cli-calc/issues)
[![github issues closed](https://img.shields.io/github/issues-closed-raw/cruisen/cli-calc?color=green&label=closed)](https://github.com/cruisen/cli-calc/issues?q=is%3Aissue+is%3Aclosed)



## Features

* Fully [typed with annotations](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) 
* and checked with [mypy](https://mypy.readthedocs.io/en/stable/)
* [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/) Packaging
* [PEP020](https://www.python.org/dev/peps/pep-0020/) Zen of Python

## Tools

### Style and type annotations
* [pylint](https://pylint.pycqa.org/en/latest/) vim linter
* [isort](https://pycqa.github.io/isort/) sort imports
* [black](https://black.readthedocs.io/en/stable/) opinionated code formatter
  * [wemake](https://wemake-python-stylegui.de/en/latest/) strictest and most opinionated Python linter
* [mypy](https://mypy.readthedocs.io/en/stable/) static type checker
* [flake8](https://flake8.pycqa.org/en/latest/) Style Guide Enforcement
  * [nitpick](https://nitpick.readthedocs.io/en/latest/) enforce the same settings across configuration files

### Testing and CT
* [pytest](https://docs.pytest.org/) test framework
  * [The Magic Tricks of Testing by Sandi Metz (video)](https://www.youtube.com/watch?v=URSWYvyc42M) on what to test, and what not.

### Build and publish to pypi
* [poetry version bump](https://python-poetry.org/docs/cli/#version) bump version
* [poetry build](https://python-poetry.org/docs/cli/#build) wheel
* [poetry publish](https://python-poetry.org/docs/cli/#publish) to pypi
* [make](https://github.com/cruisen/cli-calc/blob/main/Makefile) automate above

### Development Environment
* [poetry](https://python-poetry.org/) python packaging and dependency management
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) creates projects from project templates
* [git](https://git-scm.com/) distributed version control system
* [github](https://github.com/) online collaborative version control
  * [gh](https://github.com/cli/cli) GitHub on the command line
* [Markdown](https://www.markdownguide.org/basic-syntax/) lightweight markup language
* [vi](https://www.vim.org/about.php) advanced text editor
* [VS Code](https://code.visualstudio.com/) source-code editor 

### Documentation
* [sphinx](https://www.sphinx-doc.org/en/master/) Python documentation Generator
* [doc8](https://github.com/pycqa/doc8) opinionated style checker for rst

### Metric
* [shields](https://shields.io/) for Shields and Badges
* [cloc](https://github.com/AlDanial/cloc) for SLOC
  * [make_shields.py](https://github.com/cruisen/cli-calc/blob/main/dev_tools/meters/make_shields.py) for SLOC

# License

[MIT](https://github.com/cruisen/cli-calc/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [d06993f12e3ffad79652a2aec86189dee92d94dd](https://github.com/wemake-services/wemake-python-package/tree/d06993f12e3ffad79652a2aec86189dee92d94dd). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/d06993f12e3ffad79652a2aec86189dee92d94dd...master) since then.
