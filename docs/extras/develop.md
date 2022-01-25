# Development

## Features

* Fully [typed with annotations](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) 
* Checked with [mypy](https://mypy.readthedocs.io/en/stable/)
* Packaging [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)

## Tools

### Python Packages
* [pypi.org](https://pypi.org/) Python Package Index
  * [pythonrepo.com](https://pythonrepo.com/catalog/popular/) Popular Python Libraries

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

* [github actions](https://github.com/cruisen/cli-calc/actions)
  * [pytest & coverage (yml)](https://github.com/cruisen/cli-calc/blob/main/.github/workflows/test.yml) 
    pytest @ python-version: ['3.7', '3.8', '3.9', '3.10']
  * [misspell (yml)](https://github.com/cruisen/cli-calc/blob/main/.github/workflows/misspell.yml)
  * [codeql-analysis (yml)](https://github.com/cruisen/cli-calc/blob/main/.github/workflows/codeql-analysis.yml)
* Alternative to hithub actions
  * [tox](https://tox.wiki/en/latest/) test and deploy
  * [travis](https://www.travis-ci.com/) test and deploy
  * [coveralls.io](https://coveralls.io/) coverage

### Build and publish to pypi
* [poetry version bump](https://python-poetry.org/docs/cli/#version) bump version
* [poetry build](https://python-poetry.org/docs/cli/#build) wheel
* [poetry publish](https://python-poetry.org/docs/cli/#publish) to pypi
* [make Makefile](https://github.com/cruisen/cli-calc/blob/main/Makefile) automate above
  * [Managing Projects with GNU Make, 3rd Edition](https://www.oreilly.com/library/view/managing-projects-with/0596006101/ch01.html) 

### Following Semantic Versioning
* [Semantic Versioning](https://semver.org/) 
  * [semver](https://pypi.org/project/semver/) Python Package
  * [get_ver_for_rule (dev_tool)](https://github.com/cruisen/cli-calc/blob/main/dev_tools/sem_ver/get_ver_for_rule.py)

### Development Environment
* [poetry](https://python-poetry.org/) python packaging and dependency management
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) creates projects from project templates

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
  * [Tips](https://github.com/cruisen/cli-calc/blob/main/docs/extras/zsh.md)

### Documentation
* [Markdown](https://www.markdownguide.org/basic-syntax/) lightweight markup language
* [sphinx](https://www.sphinx-doc.org/en/master/) Python documentation Generator
* [doc8](https://github.com/pycqa/doc8) opinionated style checker for rst
* [readthedocs](https://readthedocs.org/) document style and service
  * [cli-calc](https://cli-calc.readthedocs.io/en/latest/?badge=latest#)

### Metric
* [shields](https://shields.io/) for Shields and Badges
  * [issuehub.pro](http://issuehub.pro/label-guide) Label Guide
    * [List of Badges](https://naereen.github.io/badges/)
  * [cloc](https://github.com/AlDanial/cloc) for SLOC
    * [make_shields.py (dev_tool)](https://github.com/cruisen/cli-calc/blob/main/dev_tools/meters/make_shields.py) for SLOC

### Jason Query for Makefile and Shields
* [jq](https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-keyhttps://stedolan.github.io/jq/) 
  * [Syntax](https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-key) 

### Teaching Python Development
* [Teaching](https://github.com/cruisen/cli-calc/blob/main/docs/extras/teaching.md) 


