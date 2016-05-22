# Continuous integration

## Travis CI

[Travis CI](https://travis-ci.org/) is a webservice that connects to your Github account and runs your tests for you. The configuration is in [.travis.yml](https://github.com/obestwalter/mau-mau/tree/master/.travis.yml) ([YAML](https://en.wikipedia.org/wiki/YAML) format).

As we're using tox already the integration with ci is very simple: just install and run `tox` on the build machine and we're done.

The badge on top of the projects [README.md](https://github.com/obestwalter/mau-mau/blob/4.0.1/README.md) shows the [build status from Travis CI](https://travis-ci.org/obestwalter/mau-mau).

This is a very simple setup. There are many more [configuration options](https://docs.travis-ci.com/user/languages/python).

## Appveyor

[Appveyor](https://www.appveyor.com/) is the pendant to run tests on Windows osses.

The same as for Travis Ci applies to appveyor. The configuration is slightly different but the principle is the same: [.appveyor.yml](https://github.com/obestwalter/mau-mau/tree/master/.appveyor.yml) ([YAML](https://en.wikipedia.org/wiki/YAML) format)

The badge on top of the projects [README.md](https://github.com/obestwalter/mau-mau/blob/4.0.1/README.md) shows the [build status from Travis CI](https://ci.appveyor.com/project/obestwalter/mau-mau).
