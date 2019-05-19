# tox - a developer frontend

## What?

The name of the [tox automation project](https://pypi.python.org/pypi/tox) derives from "testing out of the box". It aims to "automate and standardize testing in Python". Conceptually it is one level above pytest and serves as a command line frontend for running tests and automate all kinds of tasks around the project. It also acts as a frontend for [Continuous Integration Systems](https://en.wikipedia.org/wiki/Continuous_integration) to unify what you do locally and what happens in e.g. Jenkins or Travis CI.

## How?

tox can build the package under test, create virtual environments for different Python interpreters, install dependencies and does whatever else is needed for test preparation. After setting the stage it runs the tests and outputs the results. This way you can also run the same tests for different interpreters if you support different version of Python like 2.7 and 3.4, etc.

In this project we use it to run the tests and for building, developing and deploying the documentation.

## tox generated "developer documentation"

Since tox 2.7 you can also add descriptions to the different environments to provide a custom "developer documentation" - to get this you type `tox -av` in the e.g. in mau-mau project and the output would be like:

```text
using tox.ini: /home/ob/do/mau-mau/tox.ini (pid 5314)
using tox-3.9.0 from /usr/lib/python3.7/site-packages/tox/__init__.py (pid 5314)
default environments:
lint              -> run fixers and linters
test              -> run automatic tests using pytest

additional environments:
dev               -> create dev env at /home/ob/do/mau-mau/.tox/dev
docs-dev          -> run local server that serves and rebuilds documentation
docs-deploy       -> deploy documentation to github hosting
docs-deploy-force -> delete documentation online and deploy completely fresh
docs-clean        -> remove the generated documentation
```

If you want to work on the documentation you type `tox -e docs-dev` and off you go :)

## Examples for running tests

Run static code analysis:

```bash
$ cd </path/to/your/clone>
$ tox -e lint
```

The output is like:

```text
lint develop-inst-noop: /home/ob/do/mau-mau
lint installed: appdirs==1.4.3,attrs==19.1.0,black==19.3b0,Click==7.0,entrypoints==0.3,fire==0.1.3,flake8==3.7.7,-e git+git@github.com:obestwalter/mau-mau.git@820747869d434e578e33dedeb3d417da339fc7fd#egg=mau_mau,mccabe==0.6.1,pycodestyle==2.5.0,pyflakes==2.1.1,six==1.12.0,toml==0.10.0
lint run-test-pre: PYTHONHASHSEED='2918481120'
lint run-test: commands[0] | black -l 79 /home/ob/do/mau-mau
All done! ✨ 🍰 ✨
18 files left unchanged.
lint run-test: commands[1] | flake8 /home/ob/do/mau-mau/mau_mau /home/ob/do/mau-mau/tests --show-source
```

Command line usage:

```bash
$ cd </path/to/your/clone>
$ tox -e test
```

The output is like:

```text
GLOB sdist-make: /home/ob/do/mau-mau/setup.py
test inst-nodeps: /home/ob/do/mau-mau/.tox/.tmp/package/1/mau-mau-4.0.2.dev66+g8207478.d20190519.zip
test installed: atomicwrites==1.3.0,attrs==19.1.0,fire==0.1.3,mau-mau==4.0.2.dev66+g8207478.d20190519,more-itertools==7.0.0,pluggy==0.11.0,py==1.8.0,pytest==4.5.0,six==1.12.0,wcwidth==0.1.7
test run-test-pre: PYTHONHASHSEED='3568010355'
test run-test: commands[0] | pytest /home/ob/do/mau-mau/tests
=============================================================== test session starts ===============================================================
platform linux -- Python 3.7.3, pytest-4.5.0, py-1.8.0, pluggy-0.11.0
cachedir: .tox/test/.pytest_cache
rootdir: /home/ob/do/mau-mau, inifile: tox.ini
collected 35 items                                                                                                                                

tests/test_concepts.py ...................                                                                                                  [ 54%]
tests/test_objects.py .....                                                                                                                 [ 68%]
tests/test_player.py ...                                                                                                                    [ 77%]
tests/test_rules.py ...                                                                                                                     [ 85%]
tests/test_sim.py .....                                                                                                                     [100%]

============================================================ 35 passed in 0.05 seconds ============================================================
_____________________________________________________________________ summary _____________________________________________________________________
  test: commands succeeded
  congratulations :)
```

This is a very simple setup. There are many more [configuration options](https://tox.readthedocs.org/en/latest/config.html)

!!! note
    Just running `tox` without parameters runs all the environments defined in envlist.
