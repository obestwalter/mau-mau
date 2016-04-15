# Mau Mau

> Play is the highest form of research

> -- [Probably not Albert Einstein](http://quoteinvestigator.com/2014/08/21/play-research/)

The goal of this project is to have a real Python application with good documentation about the internal workings and the tools being used.

# Features of the implementation

game:

* Complete [rules of Mau Mau](guide/rules.md)
* two different strategies:
    * simple random strategy for a computer player
    * strategy that adds interactivity so a human can play against the computer
* Functions to run multiple games and collect stats
* Flexible [command line interface](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/cli.py) (add new functions without adjusting code)
* [automatic tests](https://github.com/obestwalter/mau-mau/blob/master/tests/) with py.test, tox and Travis CI

Infrastructure:

* Use of [magic methods (protocols)](implementation/remarks.md#magic-methods-protocols) to create custom classes which behave like inbuilt data types
* Installable as command line tool
* Automatic generation and deployment of documentation with MkDocs
* Quality Assurance: flake8, QuantifiedCode, py.test, doctests, Travis CI
* Logging with stdlib [logging module](https://docs.python.org/3/library/logging.html)
* Task automation: tox
