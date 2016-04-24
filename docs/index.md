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

* Installable as command line tool
* Functions to run multiple games and collect stats
* [Automatic tests](https://github.com/obestwalter/mau-mau/blob/master/tests/) with py.test, tox and Travis CI
* Flexible [command line interface](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/cli.py) (add new functions without adjusting code)
* Use of [magic methods](implementation/remarks.md#magic-methods-protocols) to create custom classes which behave like inbuilt data types
* Quality Assurance: flake8, QuantifiedCode, py.test, doctests, Travis CI
* Automatic generation and deployment of documentation with MkDocs
* Logging with stdlib [logging module](https://docs.python.org/3/library/logging.html)
* Developer task automation with tox (building and deploying docs, running tests)
