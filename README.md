# cli-calc

[![Build Status](https://github.com/nikolai.krusenstiern.de/cli-calc/workflows/test/badge.svg?branch=master&event=push)](https://github.com/nikolai.krusenstiern.de/cli-calc/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/nikolai.krusenstiern.de/cli-calc/branch/master/graph/badge.svg)](https://codecov.io/gh/nikolai.krusenstiern.de/cli-calc)
[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Powerful yet easy command line calculator.


## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)


## Installation

```bash
pip install cli-calc
```

In order to run it from anywhere: Add a symbolic link in ~/bin

```bash
cd ~/bin
ln -s ~/path/to/your/install/cli_calc/warpper.sh calc
```

Then use it anywhere. :-)

```bash
calc
```

## Example

Try:

```
sin(pi/2)
```

## License

[MIT](https://github.com/nikolai.krusenstiern.de/cli-calc/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [d06993f12e3ffad79652a2aec86189dee92d94dd](https://github.com/wemake-services/wemake-python-package/tree/d06993f12e3ffad79652a2aec86189dee92d94dd). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/d06993f12e3ffad79652a2aec86189dee92d94dd...master) since then.
