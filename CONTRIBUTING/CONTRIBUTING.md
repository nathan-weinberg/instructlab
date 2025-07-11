# Contributing to the InstructLab CLI

👍🎉 First off, thank you for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing. These are just guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request. Please read the [community contribution guide](https://github.com/instructlab/community/blob/main/CONTRIBUTING.md) first for general practices for the 🐶 InstructLab community.

> [!IMPORTANT]
> InstructLab is a fast-paced project under rapid development. Please expect the codebase to undergo significant changes from release to release. If you don't have
> prior experience contributing to an early-stage open source project, you might want to consider [contributing skills and knowledge to the model](https://docs.instructlab.ai/adding-data-to-model/creating_new_knowledge_or_skills/) instead.

## What Should I Know Before I Get Started?

### Code of Conduct

This project adheres to the [InstructLab - Code of Conduct and Covenant](https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

### How Do I Start Contributing?

The below workflow is designed to help you begin your first contribution journey. It will guide you through creating and picking up issues, working through them, having your work reviewed, and then merging.

Help on open source projects is always welcome and there is always something that can be improved. For example, documentation (like the text you are reading now) can always use improvement, code can always be clarified, variables or functions can always be renamed or commented on, and there is always a need for more test coverage. If you see something that you think should be fixed, take ownership! Here is how you get started:

## How Can I Contribute?

When contributing, it's useful to start by looking at [issues](https://github.com/instructlab/instructlab/issues). After picking up an issue, writing code, or updating a document, make a pull request and your work will be reviewed and merged. If you're adding a new feature or find a bug, it's best to [write an issue](https://github.com/instructlab/instructlab/issues/new?assignees=&labels=&template=feature_request.md&title=) first to discuss it with maintainers.

To contribute to this repository, you'll use the Fork and Pull model common in many open source repositories. For details on this process, check out [The GitHub Workflow
Guide](https://github.com/kubernetes/community/blob/master/contributors/guide/github-workflow.md)
from Kubernetes.

When your contribution is ready, you can create a pull request. Pull requests are often referred to as "PR". In general, we follow the standard [GitHub pull request](https://help.github.com/en/articles/about-pull-requests) process. Follow the template to provide details about your pull request to the maintainers.

Before sending pull requests, make sure your changes pass formatting, linting and unit tests.

### Continuous Integration

Pull requests are tested using [Continuous Integration](../docs/maintainers/ci.md) pipelines implemented by [GitHub Actions](https://docs.github.com/actions). Be sure to correct any issue reported by these pipelines.

If your change has a dependency on other Pull Requests use [the depends-on mechanism](../docs/maintainers/ci.md#dependency-on-external-pull-requests).

### Code Review

Once you've [created a pull request](#how-can-i-contribute), maintainers will review your code and may make suggestions to fix before merging. It will be easier for your pull request to receive reviews if you consider the criteria the reviewers follow while working. Remember to:

- Run tests locally and ensure they pass
- Follow the project coding conventions
- Write detailed commit messages
- Break large changes into a logical series of smaller patches, which are easy to understand individually and combine to solve a broader issue

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report ✏️, reproduce the behavior 💻, and find related reports 🔎.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues using the Bug Report template](https://github.com/instructlab/instructlab/issues/new?assignees=&labels=&template=bug_report.md&title=). Create an issue on that and provide the information suggested in the bug report issue template.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features, tools, and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion ✏️ and find related suggestions 🔎

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues using the Feature Request template](https://github.com/instructlab/instructlab/issues/new?assignees=&labels=&template=feature_request.md&title=). Create an issue and provide the information suggested in the feature requests or user story issue template.

#### How Do I Submit A (Good) Improvement Item?

Improvements to existing functionality are tracked as [GitHub issues using the User Story template](https://github.com/instructlab/instructlab/issues/new?assignees=&labels=&template=user_story.md&title=). Create an issue and provide the information suggested in the feature requests or user story issue template.

## Development

### Set up your dev environment

The following tools are required:

- [`git`](https://git-scm.com)
- [`python`](https://www.python.org) (v3.11)
- [`pip`](https://pypi.org/project/pip/) (v23.0+)
- [`expect`](https://core.tcl-lang.org/expect/index) (for functional tests)
- [`coreutils`](https://www.gnu.org/software/coreutils/) (for functional tests)
- [`bash`](https://www.gnu.org/software/bash/) (v5+, for functional tests)

You can setup your dev environment using [`tox`](https://tox.wiki/en/latest/), an environment orchestrator which allows for setting up environments for and invoking builds, unit tests, formatting, linting, etc. Install tox with:

```shell
pip install -r requirements-dev.txt
```

Install project requirements with:

```shell
pip install -r requirements.txt
```

If you want to test the `ilab` binary, you can install `ilab` and all dependencies with:

```shell
pip install .[cpu]
```

### Testing

Before pushing changes to GitHub, you need to run the tests as shown below. They can be run individually as shown in each sub-section
or can be run with the one command (use `-v` for more detailed output):

```shell
tox
```

If you need to configure a proxy or a trusted host for pip while using tox, add the `PIP_PROXY` and `PIP_TRUSTED_HOST` environment variables in the `setenv` directive within the `[testenv]` section of `tox.ini`, for example:

```shell
[testenv]
setenv =
    PIP_PROXY = http://proxy.example.com:3128
    PIP_TRUSTED_HOST = pypi.org download.pytorch.org
```

#### Tools Overview

| **Purpose**           | **Tool name**                                 | **Description**                                                | **Example command**         |
|----------------------|------------------------------------------------|----------------------------------------------------------------|-----------------------------|
| Unit tests           | [`pytest`](https://docs.pytest.org/)            | Runs unit tests for the project                                | `tox -e py3-unit`           |
| Functional tests     | Custom Functional Tests Script                  | Executes functional tests defined in the project               | `tox -e py3-functional`     |
| Code style           | [`ruff`](https://github.com/charliermarsh/ruff), [`black`](https://github.com/psf/black), [`isort`](https://pycqa.github.io/isort/) | Enforces [`pep8`](https://peps.python.org/pep-0008/) coding style, checks for unused imports, complexity, and other code quality issues | `tox -e ruff`               |
|                      | [`pylint`](https://pylint.org) | `pylint` performs static code analysis | `tox -e lint`               |
| Type Checking        | [`mypy`](https://mypy.readthedocs.io/en/stable/) | Performs static type analysis across the project to catch bugs  | `tox -e mypy`               |
| Documentation        | [`Sphinx`](https://docs.readthedocs.io/en/stable/intro/sphinx.html) | Generates HTML documentation for the project                   | `tox -e docs`               |
| TOML File Linting    | Custom `Makefile` process                      | Lints and formats the `pyproject.toml` file                    | `tox -e tomllint`           |

By default, all tests found within the `tests` directory are run. However, specific unit tests can run by passing filenames, classes and/or methods to `pytest` using tox positional arguments.  The following example invokes a single test method `test_diff_invalid_base` within the `TestLabDiff` class that is declared in the `tests/test_lab_diff.py` file:

```shell
tox -e py3-unit -- tests/test_lab_diff.py:::TestLabDiff::test_diff_invalid_base
```

Additionally, tools like `ruff`, `mypy`, and `lint` can also be used with `--` followed by a single file:

```shell
tox -e ruff -- code_file.py
tox -e mypy -- code_file.py
tox -e lint -- code_file.py
```

### Debug

Use the `--debug-params` and `--debug-params-json` flags to list options that display diagnostic information about parameters, including their names and values. It also reveals the type of each value and its origin (command line, env vars, default, map), e.g.:

```shell
ilab model chat --debug-params
ilab model chat --debug-params-json
```

## Your First Code Contribution

Unsure where to begin contributing? You can start by looking through these issues:

- Issues with the [`good first issue` label](https://github.com/instructlab/instructlab/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) - these should only require a few lines of code and are good targets if you're just starting contributing.
- Issues with the [`help wanted` label](https://github.com/instructlab/instructlab/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) - these range from simple to more complex, but are generally things we want but can't get to in a short time frame.

## Developer Certificate of Origin

When you make a contribution to InstructLab, you implicitly agree to the Developer Certificate of Origin terms as set in `DCO.txt` at the root of this repository.
