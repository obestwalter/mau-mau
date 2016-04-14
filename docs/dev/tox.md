# Tox - a developer frontend

[Tox](https://pypi.python.org/pypi/tox) is one abstraction level up from py.test and serves as a command line frontend for different kinds of tests and also acts a a frontend for external test runners as part of [CI](https://en.wikipedia.org/wiki/Continuous_integration). It automatically creates an environment for the tests, installs dependencies, does whatever else is needed for test preparation and outputs the results.

 It can also be (ab)used to act as a frontend for other tasks developers have to do as part of their work. In this project we also use it for building and developing the documentation.

Run static code analysis:

    $ cd </path/to/your/clone>
    $ tox -e static

output like: 

    static create: </path/to/your/clone>/.tox/static
    static installdeps: flake8
    static develop-inst: </path/to/your/clone>
    static installed: flake8==2.5.4,-e git+git@github.com:obestwalter/mau-mau.git@46669a6073d233b8a27eee4995c63f03a4aec7a3#egg=mau_mau,mccabe==0.4.0,pep8==1.7.0,pyflakes==1.0.0
    static runtests: PYTHONHASHSEED='3703953266'
    static runtests: commands[0] | flake8 </path/to/your/clone>/mau_mau </path/to/your/clone>/tests --show-source

command line usage:

    $ cd </path/to/your/clone>
    $ tox -e tests
    
output like: 

    tests develop-inst-nodeps: </path/to/your/clone>
    tests installed: -e git+git@github.com:obestwalter/mau-mau.git@46669a6073d233b8a27eee4995c63f03a4aec7a3#egg=mau_mau,py==1.4.31,pytest==2.9.1
    tests runtests: PYTHONHASHSEED='2804594378'
    tests runtests: commands[0] | py.test </path/to/your/clone>/tests
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

This is a very simple setup. There are many more [configuration options](https://tox.readthedocs.org/en/latest/config.html)

**BTW:** just running `tox` without parameters runs all the environments defined in envlist.
