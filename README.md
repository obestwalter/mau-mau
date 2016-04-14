# Mau Mau [![Documentation Status](https://readthedocs.org/projects/mau-mau/badge/?version=latest)](http://mau-mau.readthedocs.org/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/obestwalter/mau-mau.svg?branch=master)](https://travis-ci.org/obestwalter/mau-mau) [![Code Issues](https://www.quantifiedcode.com/api/v1/project/663c550f107844aa842b4ce5e02883c4/badge.svg)](https://www.quantifiedcode.com/app/project/663c550f107844aa842b4ce5e02883c4)

Command line implementation of a german card game called [Mau Mau](https://goo.gl/Am29SF).

**Part of the [Python Exploration Toolkit](https://github.com/obestwalter/pet)**

A simple application that uses all my favorite bells and whistles of the OSS/Python ecosystem.

## Documentation

... is still in the experimentation phase. Looks like mkdocs is winning atm.

* **[Generated with MkDocs, hosted on github.io](http://obestwalter.github.io/mau-mau/)** 
* ([Generated with sphinx, hosted on readthedocs](http://mau-mau.readthedocs.org/en/doc-with-sphinx/)) (killer feature (source links) not working atm - see [issue 2139](https://github.com/rtfd/readthedocs.org/issues/2139))

## Try it

### Examples for command line use

    $ pip install https://github.com/obestwalter/mau-mau/zipball/master
    $ mau-mau
    $ mau-mau winner_distribution
    $ mau-mau human  # Control+C to stop

## Development

### install local clone as editable for development

    $ git clone <url of your fork>
    $ cd mau-mau
    $ pip install -e '.[all]'

### Run the tests:

    cd </path/to/your/clone>
    $ tox
    
### Autobuild and serve the documentation locally 

    $ cd </path/to/your/clone>
    $ tox -e docs-auto  # Control+C to stop autobuild process

Can be accessed in your browser at ([http://localhost:8000](http://localhost:8000)).
    
## Licenses and Acknowledgements

### Licenses

Code is under MIT license and content is CC BY-NC-SA 4.0

[![code license](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/License_icon-mit-2.svg/32px-License_icon-mit-2.svg.png)](http://opensource.org/licenses/mit-license.php) [![content license](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

### Acknowledgements

A visual profiler is handy to demonstrate execution behaviour and timing. [PyVmMonitor](http://pyvmmonitor.com) is being used for that.
