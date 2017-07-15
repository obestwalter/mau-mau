# Tox - a developer frontend

## What?

The name of the [tox automation project](https://pypi.python.org/pypi/tox) derives from "testing out of the box". It aims to "automate and standardize testing in Python". Conceptually it is one level above pytest and serves as a command line frontend for running tests and automate all kinds of tasks around the project. It also acts as a frontend for [Continuous Integration Systems](https://en.wikipedia.org/wiki/Continuous_integration) to unify what you do locally and what happens in e.g. Jenkins or Travis CI.

## How?

Tox can build the package under test, create virtual environments for different Python interpreters, install dependencies and does whatever else is needed for test preparation. After setting the stage it runs the tests and outputs the results. This way you can also run the same tests for different interpreters if you support different version of Python like 2.7 and 3.4, etc.

In this project we use it to run the tests and for building, developing and deploying the documentation.

## Tox generated "developer documentation"

Since tox 2.7 you can also add descriptions to the different environments to provide a custom "developer documentation" - to get this you type `tox -av` in the e.g. in mau-mau project and the output would be like:

```text
using tox.ini: /home/oliver/learn/mau-mau/tox.ini
using tox-2.7.0 from /home/oliver/.virtualenvs/mau-mau/lib/python3.6/site-packages/tox/__init__.py
default environments:
static            -> run static tests using flake8
tests             -> run automatic tests using pytest

additional environments:
docs-auto         -> run local server that serves and rebuilds documentation
docs-clean        -> remove the generated documentation
docs-deploy       -> deploy documentation to github hosting
docs-deploy-force -> delete documentation online and deploy completely fresh
```

If you want to work on the documentation you type `tox -e docs-auto` and off you go :)

## Examples for running tests

Run static code analysis:

```bash
$ cd </path/to/your/clone>
$ tox -e static
```

The output is like:

```text
static create: </path/to/your/clone>/.tox/static
static installdeps: flake8
static develop-inst: </path/to/your/clone>
static installed: flake8==2.5.4,-e git+git@github.com:obestwalter/mau-mau.git@46669a6073d233b8a27eee4995c63f03a4aec7a3#egg=mau_mau,mccabe==0.4.0,pep8==1.7.0,pyflakes==1.0.0
static runtests: PYTHONHASHSEED='3703953266'
static runtests: commands[0] | flake8 </path/to/your/clone>/mau_mau </path/to/your/clone>/tests --show-source
```

Command line usage:

```bash
$ cd </path/to/your/clone>
$ tox -e tests
```

The output is like:

```text
tests develop-inst-nodeps: </path/to/your/clone>
tests installed: -e git+git@github.com:obestwalter/mau-mau.git@46669a6073d233b8a27eee4995c63f03a4aec7a3#egg=mau_mau,py==1.4.31,pytest==2.9.1
tests runtests: PYTHONHASHSEED='2804594378'
tests runtests: commands[0] | pytest </path/to/your/clone>/tests
============================= test session starts =============================
platform linux -- Python 3.4.4, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: </path/to/your/clone>, inifile: tox.ini
collected 35 items 

tests/test_concepts.py ...................
tests/test_objects.py .....
tests/test_player.py ...
tests/test_rules.py ...
tests/test_sim.py .....

========================== 35 passed in 0.04 seconds ==========================
___________________________________ summary ___________________________________
  tests: commands succeeded
  congratulations :)
```

This is a very simple setup. There are many more [configuration options](https://tox.readthedocs.org/en/latest/config.html)

!!! note
    Just running `tox` without parameters runs all the environments defined in envlist.
