![Logo](https://raw.githubusercontent.com/cruisen/cli-calc/4986df3abb3f1871d6669dec27d5e37aba0d11a3/assets/images/Cli-Calc.png)

# cli-calc

[![test](https://github.com/cruisen/cli-calc/actions/workflows/test.yml/badge.svg)](https://github.com/cruisen/cli-calc/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cruisen/cli-calc/branch/main/graph/badge.svg?token=i9nYZL3MM3)](https://codecov.io/gh/cruisen/cli-calc)
[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)

[![pypi](https://img.shields.io/pypi/v/cli-calc)](https://pypi.org/project/cli-calc/)
[![github release](https://img.shields.io/github/release-date/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/releases)
[![pypi downloads](https://img.shields.io/pypi/dm/cli-calc?label=pypi%20downloads)](https://pypistats.org/packages/cli-calc)

Powerful yet easy command line calculator.

## Introduction

Just using python at the command line provides a pretty decent calculator:

```bash
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

Read more about
[Python as a Calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator).

But it is a little cumbersome,
if you want to use a ```sin()``` function or the like.
Typing ```import math```,
and then ```math.sin( math.pi )``` is not straight forward.

But:
[There must be a better way!](https://www.youtube.com/watch?v=UANN2Eu6ZnM)
And there is...


### cli-calc

```bash
$ cli-calc
hex, int, float,
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

```bash
$ cli-calc
hex, int, float,
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

```bash
path=~/path/to/your/cli-calc/cli_calc
cd $path
./main.py
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
calc
h
Input:
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

    Try "cos(pi/2)", XOR: "0xFF ^ 0b10", "2**8-1", "factorial(42)",
        "help(math)"
```

* Permalink to this document as a
[github page](https://cruisen.github.io/cli-calc/)

## Warning

- Use of [```eval```](https://docs.python.org/3/library/functions.html#eval) is evil.
  However precautions are taken.


# Development

## Pull Request

PR's are Welcome! See
[PULL_REQUEST_TEMPLATE](https://github.com/cruisen/cli-calc/blob/main/PULL_REQUEST_TEMPLATE.md)
and
[CONTRIBUTING](https://github.com/cruisen/cli-calc/blob/main/CONTRIBUTING.md).

## Metric Dashboard

[![test](https://github.com/cruisen/cli-calc/actions/workflows/test.yml/badge.svg)](https://github.com/cruisen/cli-calc/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cruisen/cli-calc/branch/main/graph/badge.svg?token=i9nYZL3MM3)](https://codecov.io/gh/cruisen/cli-calc)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cruisen/cli-calc/main.svg)](https://results.pre-commit.ci/latest/github/cruisen/cli-calc/main)
[![Documentation Status](https://readthedocs.org/projects/cli-calc/badge/?version=latest)](https://readthedocs.org/projects/cli-calc/builds/)
[![made-with-sphinx-doc](https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/cruisen/cli-calc/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/cruisen/cli-calc/?branch=main)
[![CodeQL](https://github.com/cruisen/cli-calc/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/cruisen/cli-calc/actions/workflows/codeql-analysis.yml)
[![Requirements Status](https://requires.io/github/cruisen/cli-calc/requirements.svg?branch=main)](https://requires.io/github/cruisen/cli-calc/requirements/?branch=main)
[![Dependencies](https://img.shields.io/librariesio/release/github/cruisen/cli-calc)](https://libraries.io/github/cruisen/cli-calc)

[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/cli-calc)](https://realpython.com/cpython-source-code-guide/)
[![Python Lang](https://img.shields.io/github/languages/top/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/search?l=python)
[![Languages](https://img.shields.io/github/languages/count/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/search?l=python)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

[![SLOC](https://img.shields.io/endpoint?color=blue&url=https://raw.githubusercontent.com/cruisen/cli-calc/main/dev_tools/meters/cli_calc_shields.json)](https://github.com/cruisen/cli-calc/tree/main/cli_calc)
[![SLOC Tests](https://img.shields.io/endpoint?color=blue&url=https://raw.githubusercontent.com/cruisen/cli-calc/main/dev_tools/meters/tests_shields.json)](https://github.com/cruisen/cli-calc/tree/main/tests)
[![SLOC Dev](https://img.shields.io/endpoint?color=blue&url=https://raw.githubusercontent.com/cruisen/cli-calc/main/dev_tools/meters/dev_tools_shields.json)](https://github.com/cruisen/cli-calc/tree/main/dev_tools)
[![code size](https://img.shields.io/github/languages/code-size/cruisen/cli-calc)](https://github.com/cruisen/cli-calc.git)

[![Maintenance](https://img.shields.io/badge/Maintained-yes-green)](https://GitHub.com/cruisen/cli-calc/graphs/commit-activity)
[![MIT](https://img.shields.io/pypi/l/cli-calc)](https://github.com/cruisen/cli-calc/blob/main/LICENSE)
[![pypi status](https://img.shields.io/pypi/status/cli-calc)](https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification)
[![github stars](https://img.shields.io/github/stars/cruisen/cli-calc?style=social)](https://github.com/cruisen/cli-calc/stargazers)

[![pypi](https://img.shields.io/pypi/v/cli-calc)](https://pypi.org/project/cli-calc/)
[![github release](https://img.shields.io/github/release-date/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/releases)
[![pypi wheel](https://img.shields.io/pypi/wheel/cli-calc)](https://pypi.org/project/cli-calc/#files)
[![pypi downloads](https://img.shields.io/pypi/dm/cli-calc?label=pypi%20downloads)](https://pypistats.org/packages/cli-calc)

[![last commit](https://img.shields.io/github/last-commit/cruisen/cli-calc)](https://github.com/cruisen/cli-calc/commits/main)
[![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/cruisen/cli-calc/latest?sort=semver)](https://github.com/cruisen/cli-calc/releases/latest)
[![github commits since](https://img.shields.io/github/commits-since/cruisen/cli-calc/v0.1.1)](https://github.com/cruisen/cli-calc/commits/main)
[![github commits rate](https://img.shields.io/github/commit-activity/m/cruisen/cli-calc?label=commits)](https://github.com/cruisen/cli-calc/commits/main)

[![github issues next milestone](https://img.shields.io/github/milestones/progress-percent/cruisen/cli-calc/6)](https://github.com/cruisen/cli-calc/milestone/6)
[![github bugs open](https://img.shields.io/github/issues-raw/cruisen/cli-calc/is_Bug?color=red&label=bugs)](https://github.com/cruisen/cli-calc/issues?q=is%3Aopen+is%3Aissue+label%3Ais_Bug)
[![github bugs closed](https://img.shields.io/github/issues-closed-raw/cruisen/cli-calc/is_Bug?color=green&label=closed)](https://github.com/cruisen/cli-calc/issues?q=is%3Aissue+is%3Aclosed+label%3Ais_Bug)
[![github issues open](https://img.shields.io/github/issues-raw/cruisen/cli-calc?color=blue)](https://github.com/cruisen/cli-calc/issues)
[![github now](https://img.shields.io/github/issues-raw/cruisen/cli-calc/1-Now-Important?color=yellow&label=queued)](https://github.com/cruisen/cli-calc/issues?q=is%3Aopen+is%3Aissue+label%3A1-Now-Important)
[![github issues closed](https://img.shields.io/github/issues-closed-raw/cruisen/cli-calc?color=green&label=closed)](https://github.com/cruisen/cli-calc/issues?q=is%3Aissue+is%3Aclosed)
[![github help open](https://img.shields.io/github/issues-raw/cruisen/cli-calc/needs_Help?color=yellow&label=need%20help)](https://github.com/cruisen/cli-calc/issues?q=is%3Aopen+is%3Aissue+label%3Aneeds_Help)

[![Pull Requests open](https://img.shields.io/github/issues-pr-raw/cruisen/cli-calc?label=PR)](https://github.com/cruisen/cli-calc/pulls)
[![Pull Requests merged](https://img.shields.io/github/issues-pr-closed-raw/cruisen/cli-calc?label=merged&color=green)](https://github.com/cruisen/cli-calc/pulls?q=is%3Apr+is%3Aclosed)
[![Relative date](https://img.shields.io/date/1642071600?label=first%20commit)](https://github.com/cruisen/cli-calc/commit/ac96ed51041c26195840186de1f1fd60375c0736)
[![github downloads](https://img.shields.io/github/downloads/cruisen/cli-calc/total?label=github%20downloads)](https://github.com/cruisen/cli-calc)

### Note on Shields

[![Dependencies](https://img.shields.io/librariesio/release/github/cruisen/cli-calc)](https://libraries.io/github/cruisen/cli-calc)

1. [flake8-commas](https://github.com/PyCQA/flake8-commas),
   one of the development plugins of the
   [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide)
   is marked as *No Maintenance Intended*.
   See this
   [Issue](https://github.com/wemake-services/wemake-python-styleguide/issues/2276).
   Most probable *wemake* will replace this dependency with a fork.

1. [python 3.7](https://www.python.org/dev/peps/pep-0537/#and-beyond-schedule)
   is deprecated.
   However some dev tools are still dependant.

## Features

* Fully [typed with annotations](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
* Checked with [mypy](https://mypy.readthedocs.io/en/stable/)
* Packaging [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)


## Tools

### Python Packages
* [pypi.org ](https://pypi.org/) Python Package Index
  * [pythonrepo.com](https://pythonrepo.com/catalog/popular/) Popular Python Libraries
* [poetry add](https://python-poetry.org/docs/cli/#add)
* [poetry update](https://python-poetry.org/docs/cli/#update)

### Style and type annotations
* [pylint](https://pylint.pycqa.org/en/latest/) vim linter
* [isort](https://pycqa.github.io/isort/) sort imports
* [black](https://black.readthedocs.io/en/stable/) opinionated code formatter
  * [wemake](https://wemake-python-stylegui.de/en/latest/) strictest and most opinionated Python linter
* [mypy](https://mypy.readthedocs.io/en/stable/) static type checker
* [flake8](https://flake8.pycqa.org/en/latest/) Style Guide Enforcement
  * [nitpick](https://nitpick.readthedocs.io/en/latest/) enforce the same settings across configuration files

### Testing
* [pytest](https://docs.pytest.org/) test framework
  * [The Magic Tricks of Testing by Sandi Metz (Talk)](https://www.youtube.com/watch?v=URSWYvyc42M) on what to test, and what not

### Continuous Testing & Integration (CT & CI)
Integration as in: Deployment and Integration testing.

* [crontab](https://linux.die.net/man/5/crontab)

* [github actions](https://github.com/features/actions)
  * [pytest & coverage (yml)](https://github.com/cypress-io/github-action/blob/master/.github/workflows/example-basic.yml)
    pytest @ python-version: ['3.7', '3.8', '3.9', '3.10']
  * [misspell (yml)](https://github.com/reviewdog/action-misspell)
  * [codeql-analysis (yml)](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-the-codeql-workflow-for-compiled-languages)

* Alternatives to github actions
  * [tox](https://tox.wiki/en/latest/) test and deploy
  * [travis](https://www.travis-ci.com/) test and deploy
  * [coveralls.io](https://coveralls.io/) coverage

### Build and publish to pypi
* [make Makefile](https://www.gnu.org/software/make/manual/make.html) automate above
  * [Managing Projects with GNU Make, 3rd Edition](https://www.oreilly.com/library/view/managing-projects-with/0596006101/ch01.html)
* [poetry version bump](https://python-poetry.org/docs/cli/#version) bump version
* [poetry build](https://python-poetry.org/docs/cli/#build) wheel
* [poetry publish](https://python-poetry.org/docs/cli/#publish) to pypi

### Following Semantic Versioning
* [Semantic Versioning](https://semver.org/)
  * [semver](https://pypi.org/project/semver/) Python Package

### Development Environment
* [poetry](https://python-poetry.org/) python packaging and dependency management
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) creates projects from project templates
* [venv](https://docs.python.org/3/library/venv.html) creates projects from project templates

### Version and Issue Management
* [git](https://git-scm.com/) distributed version control system
* [github](https://github.com/) online collaborative version control
  * [gh](https://github.com/cli/cli) GitHub on the command line
    * [gh Milestones](https://gist.github.com/doi-t/5735f9f0f7f8b7664aa6739bc810a2cc)
* [tickgit](https://github.com/augmentable-dev/tickgit) Not used, but collects TODO from source code

### IDE
* [vi](https://www.vim.org/about.php) advanced text editor
* [VS Code](https://code.visualstudio.com/) source-code editor

### Shell
* [oh-my-zsh](https://ohmyz.sh/)
  * [zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH#how-to-install-zsh-on-many-platforms)
  * [MAC config](https://chiamakaikeanyi.dev/how-to-configure-your-macos-terminal-with-zsh-like-a-pro/)

### Documentation
* [Markdown](https://www.markdownguide.org/basic-syntax/) lightweight markup language
  * [Markdown to PDF (online)](https://dillinger.io/)
* [sphinx](https://www.sphinx-doc.org/en/master/) Python documentation Generator
* [doc8](https://github.com/pycqa/doc8) opinionated style checker for rst
* [readthedocs](https://readthedocs.org/) document style and service

### Metric
* [shields](https://shields.io/) for Shields and Badges
  * [issuehub.pro](http://issuehub.pro/label-guide) Label Guide
    * [List of Badges](https://naereen.github.io/badges/)
  * [cloc](https://github.com/AlDanial/cloc) for SLOC

### Jason Query for Makefile and Shields
* [jq](https://stedolan.github.io/jq/)
  * [Syntax](https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-key)

## Teaching Python Development
* [Teaching](https://github.com/cruisen/cli-calc/blob/main/docs/extras/teaching.md)

### cli-calc Examples
* [github actions (cli-calc)](https://github.com/cruisen/cli-calc/actions)
  * [pytest & coverage (yml) (cli-calc)](https://github.com/cruisen/cli-calc/blob/main/.github/workflows/test.yml)
  * [codeql-analysis (yml) (cli-calc)](https://github.com/cruisen/cli-calc/blob/main/.github/workflows/codeql-analysis.yml)
  * [misspell (yml) (cli-calc)](https://github.com/cruisen/cli-calc/blob/main/.github/workflows/misspell.yml)
* [make Makefile (cli-calc)](https://github.com/cruisen/cli-calc/blob/main/Makefile) automate above
* [cli-calc](https://cli-calc.readthedocs.io/en/latest/?badge=latest#)

### NvK Tools
* [make_shields.py (dev_tool)](https://github.com/cruisen/cli-calc/blob/main/dev_tools/meters/make_shields.py) for SLOC
* [get_ver_for_rule (dev_tool)](https://github.com/cruisen/cli-calc/blob/main/dev_tools/sem_ver/get_ver_for_rule.py)
* [Tips](https://github.com/cruisen/cli-calc/blob/main/docs/extras/zsh.md)

# License

[MIT](https://github.com/cruisen/cli-calc/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [d06993f12e3ffad79652a2aec86189dee92d94dd](https://github.com/wemake-services/wemake-python-package/tree/d06993f12e3ffad79652a2aec86189dee92d94dd). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/d06993f12e3ffad79652a2aec86189dee92d94dd...master) since then.
