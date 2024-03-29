# Mau Mau

> Play is the highest form of research

> -- [Probably not Albert Einstein](http://quoteinvestigator.com/2014/08/21/play-research/)

This project aims to be a learning tool, but this is a real application - not a toy example. The important difference to a "real" program is that the nasty details that usually screw with the nice and simple design and make the code grow tentacles and other cruft are kept at a minimum to enable you to [explore the code](implementation/explore.md#explore-the-repository) as a nice little completely non-linear story. It came to life in a non-linear fashion and should also be read that way.

Emphasis is put on [pythonic](https://nedbatchelder.com/blog/201011/pythonic.html) ways to code and on using the power of the Open Source ecosystem.

## Features

### The game

* Complete [rules of Mau Mau](guide/rules.md)
* Two different [strategies](implementation/explore.md#strategiespy-how-to-play):
    * Simple random strategy for a computer player
    * Strategy that adds interactivity so a human can play against the computer

### Implementation and tools

* [installable](guide/installation.md#installation) as [command line tool](https://github.com/obestwalter/mau-mau/blob/bf208857b67b36311dc057ed9f988ef6c153d12a/setup.py#L20)
* [runnable from the command line](https://github.com/obestwalter/mau-mau/blob/13fb4be7e511c41853a736f0dd8171a65a0ca198/setup.py#L29-L30) (created with [fire](https://github.com/google/python-fire))
* [simulation helpers](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/stats.py) to run multiple games and collect stats
* use of [magic methods](implementation/remarks.md#magic-methods-protocols) to create custom classes which behave like inbuilt data types
* logging with stdlib [logging module](https://docs.python.org/3/library/logging.html)
* developer task automation with [tox](https://github.com/obestwalter/mau-mau/blob/master/tox.ini) orchestrating:
    * automatic code formatting with [black](https://black.readthedocs.io/)
    * Static code analysis with [flake8](http://flake8.pycqa.org/en/latest/)
    * running [tests](https://github.com/obestwalter/mau-mau/blob/master/tests/) with [pytest](https://pytest.org)
    * generation and deployment of documentation with [MkDocs](https://github.com/obestwalter/mau-mau/blob/master/mkdocs.yml)
    * unifying running these locally and on CI with [Travis](https://github.com/obestwalter/mau-mau/blob/master/.travis.yml) and [Appveyor](https://github.com/obestwalter/mau-mau/blob/master/appveyor.yml)
* [version handling from source control](https://github.com/obestwalter/mau-mau/blob/master/setup.py#L19) with [setuptools scm](https://github.com/pypa/setuptools_scm)
* included Linux and Windows development environments via [vagrant](https://vagrantup.com).
