# Development

## Features

* Fully [typed with annotations](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
* Checked with [mypy](https://mypy.readthedocs.io/en/stable/)
* Packaging [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)


## Tools

### Python Packages
* [pypi.org](https://pypi.org/) Python Package Index
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

### Version and Issue Management
* [git](https://git-scm.com/) distributed version control system
* [github](https://github.com/) online collaborative version control
  * [gh](https://github.com/cli/cli) GitHub on the command line
    * [gh Milestones](https://gist.github.com/doi-t/5735f9f0f7f8b7664aa6739bc810a2cc)
* [tickgit](https://github.com/augmentable-dev/tickgit) Not used, but collects TODO from source code

### IDE
* [vi](https://www.vim.org/about.php) advanced text editor
* [VS Code](https://code.visualstudio.com/) source-code editor

#### If needed
* [jupyter](https://jupyter.org/) for rapid prototyping only

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
* [jq](https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-keyhttps://stedolan.github.io/jq/)
  * [Syntax](https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-key)
