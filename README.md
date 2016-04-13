# Mau Mau [![Documentation Status](https://readthedocs.org/projects/mau-mau/badge/?version=latest)](http://mau-mau.readthedocs.org/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/obestwalter/mau-mau.svg?branch=master)](https://travis-ci.org/obestwalter/mau-mau) [![Code Issues](https://www.quantifiedcode.com/api/v1/project/663c550f107844aa842b4ce5e02883c4/badge.svg)](https://www.quantifiedcode.com/app/project/663c550f107844aa842b4ce5e02883c4)

**Part of the [Python Exploration Toolkit](https://github.com/obestwalter/pet)**

A simple application that uses all the bells and whistles of the OSS/Python ecosystem.

**[Documentation on Readthedocs](http://mau-mau.readthedocs.org/en/latest/)**

## Try it
 
    $ pip install https://github.com/obestwalter/mau-mau/zipball/master
    $ sim
    $ sim winner_distribution
    $ sim human  # Control+C to stop

## Development

    $ git clone <url of your fork>
    $ cd mau-mau
    $ pip install -e '.[all]'

run tests:

    cd </path/to/your/clone>
    $ tox
    
autobuild and serve docs on http://localhost:8000:

    $ cd </path/to/your/clone>
    $ cd docs
    $ make autohtml
    
## Licenses and Acknowledgements

### Licenses

Code is under MIT license and content is CC BY-NC-SA 4.0

[![code license](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/License_icon-mit-2.svg/32px-License_icon-mit-2.svg.png)](http://opensource.org/licenses/mit-license.php) [![content license](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

### Acknowledgements

A visual profiler is handy to demonstrate execution behaviour and timing. [PyVmMonitor](http://pyvmmonitor.com) is being used for that.
