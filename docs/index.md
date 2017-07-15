# Mau Mau

> Play is the highest form of research

> -- [Probably not Albert Einstein](http://quoteinvestigator.com/2014/08/21/play-research/)

This project aims to be a learning tool, but this is a real application - not a toy example. The important difference to a "real" program is that the nasty details that usually screw with the nice and simple design and make the code grow tentacles and other cruft are kept at a minimum to enable you to [explore the code](implementation/explore.md#explore-the-repository) as a nice little completely non-linear story. It came to life in a non-linear fashion and should also be read that way.

Emphasis is put on [pythonic](https://gist.github.com/JeffPaine/6213790) ways to code and on using the power of the Open Source ecosystem.

## Features

### The game

* Complete [rules of Mau Mau](guide/rules.md)
* Two different [strategies](implementation/explore.md#strategypy-how-to-play):
    * Simple random strategy for a computer player
    * Strategy that adds interactivity so a human can play against the computer

### Implementation and tools

* [Installable](guide/installation.md#installation) as [command line tool](https://github.com/obestwalter/mau-mau/blob/master/setup.py#L25)
* [Functions](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/statistics.py) to run multiple games and collect stats
* Use of [magic methods](implementation/remarks.md#magic-methods-protocols) to create custom classes which behave like inbuilt data types
* Logging with stdlib [logging module](https://docs.python.org/3/library/logging.html)
* Flexible [command line interface](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/cli.py) (add new functions without adjusting code)
* [Automatic tests](https://github.com/obestwalter/mau-mau/blob/master/tests/) with pytest, tox and Travis CI
* [Static code analysis](https://en.wikipedia.org/wiki/Static_program_analysis): flake8, [QuantifiedCode](https://www.quantifiedcode.com/app/project/663c550f107844aa842b4ce5e02883c4), [pytest](https://docs.pytest.org/en/latest/), Travis CI and Appveyor
* [Version handling from source control](https://github.com/obestwalter/mau-mau/blob/master/setup.py#L19) with [setuptools scm](https://github.com/pypa/setuptools_scm)
* Automatic generation and deployment of documentation with [MkDocs](https://github.com/obestwalter/mau-mau/blob/master/mkdocs.yml)
* Developer task automation with [tox](https://github.com/obestwalter/mau-mau/blob/master/tox.ini) (run tests, build and deploy documentation)
* Included Linux and Windows development environments via [vagrant](https://vagrantup.com).
