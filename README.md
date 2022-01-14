# cli-calc

[![test](https://github.com/cruisen/cli-calc/actions/workflows/test.yml/badge.svg)](https://github.com/cruisen/cli-calc/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cruisen/cli-calc/branch/main/graph/badge.svg?token=i9nYZL3MM3)](https://codecov.io/gh/cruisen/cli-calc)
[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Powerful yet easy command line calculator.


## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)


## Installation

```bash
pip install cli-calc
```

See [cli-calc](https://pypi.org/project/cli-calc/).

In order to run it from anywhere: Add a symbolic link in ~/bin

```bash
cd ~/bin
ln -s ~/path/to/your/install/cli_calc/warpper.sh calc
```

Then use it anywhere. :-)

```bash
calc
```

## Help

```bash
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

    Try "cos(_pi_/2)", XOR: "0xFF ^ 0b10", "2**8-1", "factorial(42)",
        "help(math)"
```

## Example

Try:

```
cos(_pi_/2)
0xFF ^ 0b10
2**8-1
factorial(42)
```

## License

[MIT](https://github.com/cruisen/cli-calc/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [d06993f12e3ffad79652a2aec86189dee92d94dd](https://github.com/wemake-services/wemake-python-package/tree/d06993f12e3ffad79652a2aec86189dee92d94dd). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/d06993f12e3ffad79652a2aec86189dee92d94dd...master) since then.
