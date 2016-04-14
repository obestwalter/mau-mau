# Travis CI

[Travis CI](https://travis-ci.org/) is a webservice that connects to your Github account and runs your tests for you. The configuration is in [.travis.yml](https://github.com/obestwalter/mau-mau/tree/master/.travis.yml) ([YAML](https://en.wikipedia.org/wiki/YAML) format).

As we're using tox already the integration with ci is very simple: just install run `tox` and we're done.

The badge on top of the [project `README`](https://github.com/obestwalter/mau-mau/blob/master/README.md) shows the [build status from Travis CI](https://travis-ci.org/obestwalter/mau-mau).

This is a very simple setup. There are many more [configuration options](https://docs.travis-ci.com/user/languages/python).
