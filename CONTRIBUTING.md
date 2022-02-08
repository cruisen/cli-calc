# Pull Request

* PR's are welcome. Thank you for considering the effort :-)
* Or just simply raise an [issue](https://github.com/cruisen/cli-calc/issues/new/choose).

# TLDR
In summary, if you want to contribute to cli-calc, the simplest way is to:

1. Find cli-calc at [github](https://github.com/cruisen/cli-calc)
1. Fork it
1. Clone it to your local system
1. Make a new branch
1. Make your changes
1. Push it back to your repo
1. Click the Compare & pull request button
1. Click Create pull request to open a new pull request
1. If the reviewers ask for changes, repeat steps 5 and 6 to add more commits to your pull request.

Happy coding!

[
From [How to create a pull request in GitHub](https://opensource.com/article/19/7/create-pull-request-github).
]

## Overview

This is a quick run down on how our development process is meant to be run.

Also have a look at our detailed list describing all
[development](https://github.com/cruisen/cli-calc/blob/main/docs/extras/develop.md)
tools and more.


## Dependancies

We use [poetry](https://github.com/python-poetry/poetry) to manage the dependencies.

To install them you would need to run the `install` command:

```bash
poetry install
```

To activate your `virtualenv` run `poetry shell`.


## One magic command

Run `make` to run everything we have!


## Tests

We use `pytest` and `flake8` for quality control.
We also use [wemake_python_styleguide](https://github.com/wemake-services/wemake-python-styleguide) to enforce the code quality.

To run all tests:

```bash
pytest
```

To run linting:

```bash
flake8 .
```
Keep in mind: default virtual environment folder excluded by flake8 style checking is `.venv`.
If you want to customize this parameter, you should do this in `setup.cfg`.
These steps are mandatory during the CI.


## Type checks

We use `mypy` to run type checks on our code.
To use it:

```bash
mypy cli_calc tests/**/*.py
```

This step is mandatory during the CI.


## Submitting your code

We use [trunk based](https://trunkbaseddevelopment.com/)
development (we also sometimes call it `wemake-git-flow`).

What the point of this method?

1. We use protected `master` branch,
   so the only way to push your code is via pull request
2. We use issue branches: to implement a new feature or to fix a bug
   create a new branch named `issue-$TASKNUMBER`
3. Then create a pull request to `master` branch
4. We use `git tag`s to make releases, so we can track what has changed
   since the latest release

So, this way we achieve an easy and scalable development process
which frees us from merging hell and long-living branches.

In this method, the latest version of the app is always in the `master` branch.

### Before submitting

Before submitting your code please do the following steps:

1. Run `pytest` to make sure everything was working before
2. Add any changes you want
3. Add tests for the new changes
4. Edit documentation if you have changed something significant
5. Update `CHANGELOG.md` with a quick summary of your changes
6. Run `pytest` again to make sure it is still working
7. Run `mypy` to ensure that types are correct
8. Run `flake8` to ensure that style is correct
9. Run `doc8` to ensure that docs are correct


## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
