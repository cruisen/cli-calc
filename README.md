![Logo](https://raw.githubusercontent.com/cruisen/cli-calc/4986df3abb3f1871d6669dec27d5e37aba0d11a3/assets/images/Cli-Calc.png)

# cli-calc

[![test](https://github.com/cruisen/cli-calc/actions/workflows/test.yml/badge.svg)](https://github.com/cruisen/cli-calc/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cruisen/cli-calc/branch/main/graph/badge.svg?token=i9nYZL3MM3)](https://codecov.io/gh/cruisen/cli-calc)
[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)

[![pypi](https://img.shields.io/pypi/v/cli-calc)](https://pypi.org/project/cli-calc/)
[![github release](https://img.shields.io/github/release-date/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/releases)
[![pypi downloads](https://img.shields.io/pypi/dm/cli-calc?label=pypi%20downloads)](https://pypistats.org/packages/cli-calc)

[![DEV](https://img.shields.io/badge/about-dev-green)](https://github.com/cruisen/cli-calc/blob/main/docs/extras/develop.md)

Powerful yet easy command line calculator.

## Introduction

Please note: Using plain python at the command line already does provide a pretty decent calculator:

```
$ python
Python 3.8.5 (default, Aug  2 2020, 16:00:15)
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2**10
1024
>>> _ / 10
102.4
>>> import math
>>> math.pi
3.141592653589793
>>> math.sin(math.pi / 2)
1.0
>>> exit()
```

[
Read more about
[Python as a Calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator).
]

But not all is straight forward.
For example, if you want to calculate ```sin(pi/2)```:
* First you need to ```import math```,
* and then use it with ```math.sin( math.pi / 2 )```.

But
[there must be a better way!](https://www.youtube.com/watch?v=UANN2Eu6ZnM)
And there is...


### cli-calc

```
$ cli-calc
hex, int, float, : INPUT
0x0, 0, 0.0, : 2**10
2**10
0x400, 1024, 1024.0, : _ / 10
1024.0/10
0x66, 102, 102.4, : pi
pi
0x3, 3, 3.141592653589793, : sin(pi / 2)
sin(pi/2)
0x1, 1, 1.0, : q
$
```

[Batteries included](https://www.python.org/dev/peps/pep-0206/#batteries-included-philosophy):

* ```cli-calc``` adds the standard
[math](https://docs.python.org/3/library/math.html)
library to the mix, as well as cmath and others.
* Provides convenience functions for formatted output, like
[fractions](https://docs.python.org/3.6/library/fractions.html)
and
[IEEE 754](https://en.wikipedia.org/wiki/IEEE_754).
* Supports line input from files and Unix pipes.
* And some more... :-)


## More examples

```
$ cli-calc
hex, int, float, : INPUT
0x0, 0, 0.0, : cos(pi/2)
cos(pi/2)
0x0, 0, 6.123233995736766e-17, : 0xFF ^ 0b10
0xFF^0b10
0xfd, 253, 253.0, : 2**8-1
2**8-1
0xff, 255, 255.0, : log(e)
log(e)
0x1, 1, 1.0, : comb(49,6)
comb(49,6)
0xd56048, 13983816, 13983816.0, : factorial(42)
factorial(42)
0x3c1581d491b28f523c23abdf35b689c908000000000, 1405006117752879898543142606244511569936384000000000, 1.40500611775288e+51, : random()
random()
0x0, 0, 0.24958817003921918, : cmath.phase(complex(-1.0, 0.0))
cmath.phase(complex(-1.0,0.0))
0x3, 3, 3.141592653589793, : q
$
```

## Included Math Libraries

Ready to use out of the box:

- [standard operators](https://www.w3schools.com/python/python_operators.asp)
  ``` -, >>, ...```
- [standard math library](https://docs.python.org/3/library/math.html)
  ```cd, log, sin, sinh, gamma, pi, e, tau, inf, nan...```

- [cmath](https://docs.python.org/3/library/cmath.html)
  ```phase(complex(-1.0, 0.0)), and then most of the above with complex numbers.```
- [random](https://docs.python.org/3/library/random.html#examples)
  ```random, choice(['win', 'lose', 'draw']), mean, ...```

- [built in functions](https://docs.python.org/3/library/functions.html)
  ```max, help, sum, ...```


# Installation

```bash
pip install cli-calc
```

- [pypi cli-calc](https://pypi.org/project/cli-calc/)

## Configuration

For convenience, add a shell script in ```~/bin```:

```bash
cd ~/bin
vi cli-calc
```

with the following lines:

*Note*: Please adjust the path!

```bash
path=~/path/to/your/cli-calc/
cd $path
python3 -m cli_calc
```

Make it executable:

```bash
chmod a+x cli-calc
```

then use it anywhere. :-)

```bash
echo "7+8" | cli-calc
cat foo.bar | cli-calc
cli-calc
```

## Help

```bash
cli-calc
h
--------------------------------------------------
INPUT:
    "q" for quit, "h" for help

    "_" for last float value
    "_int_" for last int value

    "sin(pi/2)" for sinus, ...

    "pi", "tau" and "e" for pi, tau and Euler

    "+f" to add display for fraction, "-f" to suppress display for fraction
        Other letters are:
        he(x), (o)ctal, (b)inary, (i)nteger,
        (f)raction, (t)ruth, i(e)ee, ieee_bi(n), f(r)om_ieee
        "float" is always visible

    See https://docs.python.org/3/library/math.html, use without "math."
        https://www.w3schools.com/python/python_operators.asp

    Try "cos(pi/2)", "0xFF ^ 0b10", "2**8-1", "factorial(42)", "help(math)"
--------------------------------------------------
hex, int, float, : INPUT
```

* Permalink to this document as a
[github page](https://cruisen.github.io/cli-calc/)

## Warning

- Use of [```eval```](https://docs.python.org/3/library/functions.html#eval) is evil.
  However precautions are taken.


# Pull Request

PR's are Welcome!

* Please read more about
  [Contributing](https://github.com/cruisen/cli-calc/blob/main/CONTRIBUTING.md)
* and our
  [development](https://github.com/cruisen/cli-calc/blob/main/docs/extras/develop.md)
  environment and tool set.
* Or just simply raise an [issue](https://github.com/cruisen/cli-calc/issues/new/choose).

# License

[MIT](https://github.com/cruisen/cli-calc/blob/master/LICENSE)

## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [d06993f12e3ffad79652a2aec86189dee92d94dd](https://github.com/wemake-services/wemake-python-package/tree/d06993f12e3ffad79652a2aec86189dee92d94dd). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/d06993f12e3ffad79652a2aec86189dee92d94dd...master) since then.
