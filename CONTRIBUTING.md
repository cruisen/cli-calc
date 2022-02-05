## How to contribute to cli-calc

#### **Did you find a bug?**

* **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/cruisen/cli-calc/issues).

* If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/cruisen/cli-calc/issues/new/choose). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

* If possible, use the provided bug report templates to create the issue.

#### **Did you write a patch that fixes a bug?**

* Open a new GitHub pull request with the patch.

* Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.

* Before submitting, please read the [develoment](https://github.com/cruisen/cli-calc/blob/main/docs/extras/develop.md) guide to know more about coding conventions and benchmarks.

#### **Did you fix whitespace, format code, or make a purely cosmetic patch?**

Changes that are cosmetic in nature and do not add anything substantial to the stability, functionality, or testability of cli-calc will generally not be accepted.

#### **Do you intend to add a new feature or change an existing one?**

* Suggest your change in the [feature request](https://github.com/cruisen/cli-calc/issues/new?assignees=cruisen&labels=is_enhancement%2C+is_Requirement%2C+need_Triage&template=feature_request.md&title=%5BFEATURE+REQUEST%5D+).

#### **Do you have questions about the source code?**

* Ask any question about how to use cli-calc by opening a [new discussion](https://github.com/cruisen/cli-calc/discussions/new).

#### **Do you want to contribute to the documentation?**

* Suggest your change in the [feature request](https://github.com/cruisen/cli-calc/issues/new?assignees=cruisen&labels=is_enhancement%2C+is_Requirement%2C+need_Triage&template=feature_request.md&title=%5BFEATURE+REQUEST%5D+).


cli-calc is a volunteer effort. We encourage you to pitch in and join [the team](https://github.com/cruisen/cli-calc/graphs/contributors)!

Thanks! :heart: :heart: :heart:

The (small) cli-calc Team


## Dependencies

We use [poetry](https://github.com/python-poetry/poetry) to manage the dependencies.

To install them you would need to run the `install` command:

```bash
poetry install
```

To activate your `virtualenv` run `poetry shell`.


## One magic command

Run `make test` to run everything we have!


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
