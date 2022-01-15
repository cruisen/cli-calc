![](https://raw.githubusercontent.com/cruisen/cli-calc/4986df3abb3f1871d6669dec27d5e37aba0d11a3/assets/images/Cli-Calc.png)

# cli-calc

[![test](https://github.com/cruisen/cli-calc/actions/workflows/test.yml/badge.svg)](https://github.com/cruisen/cli-calc/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cruisen/cli-calc/branch/main/graph/badge.svg?token=i9nYZL3MM3)](https://codecov.io/gh/cruisen/cli-calc)
[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Powerful yet easy command line calculator.

## Example Usage

```
cos(pi/2)
0xFF ^ 0b10
2**8-1
log(2)
factorial(42)
```

# Installation

```bash
pip install cli-calc
```

[pypi cli-calc](https://pypi.org/project/cli-calc/).

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


# Development tools used

## Features

* Fully typed with annotations and checked with mypy.
* [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)

## Tools

### Style and type annotations
* [pylint](https://pylint.org/)
* [isort](https://pycqa.github.io/isort/)
* [black](https://black.readthedocs.io/en/stable/)
  * [wemake](https://wemake-python-stylegui.de/en/latest/)
* [flake8](https://flake8.pycqa.org/en/latest/)
  * [nitpick](https://nitpick.readthedocs.io/en/latest/)

### Testing and CT
* [pytest](https://docs.pytest.org/)

### Build and publish to pypi
* [git-bump.ksh](https://github.com/cruisen/cli-calc/blob/69430ce5e71bc2544390f36122a8d05756518199/dev-tools/git-bump.ksh)
  * [poetry build](https://python-poetry.org/docs/cli/#build)
  * [poetry publish](https://python-poetry.org/docs/cli/#publish)

### Development Environment
* [poetry](https://python-poetry.org/)
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html)
* [git](https://git-scm.com/)
* [github](https://github.com/)
  * [gh](https://github.com/cli/cli)
* [Markdown](https://www.markdownguide.org/basic-syntax/)

### Documentation
* [sphinx](https://www.sphinx-doc.org/en/master/)
* [doc8](https://github.com/pycqa/doc8)


# License

[MIT](https://github.com/cruisen/cli-calc/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [d06993f12e3ffad79652a2aec86189dee92d94dd](https://github.com/wemake-services/wemake-python-package/tree/d06993f12e3ffad79652a2aec86189dee92d94dd). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/d06993f12e3ffad79652a2aec86189dee92d94dd...master) since then.
