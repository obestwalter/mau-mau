# Development

To work on the code 
* [fork](https://guides.github.com/activities/forking/) the code 
* [clone](http://rogerdudler.github.io/git-guide/) the repository to `<path/to/your/clone>` (wherever that is).
* install the code as editable in a [virtualenv](https://docs.python.org/3/tutorial/venv.html)

    $ <activate your virtualenv>
    $ cd <path/to/your/clone>
    $ pip install -e '.[all]'

output like:

    Obtaining file:///</path/to/your/clone>
    Installing collected packages: mau-mau
      Running setup.py develop for mau-mau
    Successfully installed mau-mau

## Testing, testing, testing 

### Static code analysis

**TODO**

#### Flake8

run flake8:
    
    $ cd <path/to/your/clone>
    $ tox -e flake8
    

#### Quantified Code

Quantified Code offers static code analysis that is even different from flake8. Definitely [worth a look](https://www.quantifiedcode.com/app/project/663c550f107844aa842b4ce5e02883c4).

### Automatic tests

#### Executable documentation with doctests

**TODO**

see [concepts.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/concepts.py)

#### [tests/](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/tests/): testing with [py.test](http://pytest.org)

The ability to write simple functions to test your code cannot be developed early enough, so why not start this right away as well? The examples are dead simple and not covering much yet, but show that it's not rocket science to write automatic tests for your code. Pytest makes it possible to use the inbuilt `assert` for writing tests.

#### Testing on the command line

**NOTE:** Make sure, you installed the package as editable.

    $ cd </path/to/your/clone>
    $ py.test
    
output like:

    ============================= test session starts =============================
    platform linux -- Python 3.4.3, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    rootdir: /path/to/your/clone/mau-mau, inifile: tox.ini
    collected 13 items 
    tests/test_pile.py .....
    tests/test_player.py ...
    tests/test_sim.py .....
    ========================== 13 passed in 0.03 seconds ==========================

If you want to take this one step further and have the tests being run automatically every time the code changes, you can:

    $ pip install pytest-watch
    $ cd </path/to/your/clone>
    $ ptw --onfail 'notify-send --urgency=critical "FAIL"' --onpass 'notify-send "PASSED"'
    
`notify-send` is the way how I can send desktop notifications from the commandline in my os ([Linux](https://wiki.archlinux.org/index.php/Desktop_notifications)). There are lots of ways to do this on every os - even [Windows](https://github.com/nels-o/toaster) and [Mac](https://github.com/julienXX/terminal-notifier).

#### Testing in PyCharm

##### Preparation

The default testrunner in PyCharm is Unittest. You have to switch to py.test like so: 
* **Find Action: [default testrunner](https://www.jetbrains.com/help/pycharm/2016.1/testing-frameworks.html)**: set to py.test 
* accept offer to install it in your project virtualenv or do it yourself with `pip install pytest`

##### Running tests

Depending on where you are, you can run all tests are part of them. The magic action is [`run context configuration`](https://www.jetbrains.com/help/pycharm/2016.1/creating-and-saving-temporary-run-debug-configurations.html). It runs what is sensible in the context. If your focus is in a normal script it runs the script and if the focus is in a module defining tests it will run the configured testrunner with the tests. Running the context configuration with ...

* focus in the editor, inside a specific test
* focus in the editor on the line defining a class containing tests
* focus in the **Project Tool Window**, choose the `tests/` folder and 

... all yields different results as which tests are run (and they are what you would intuitively expect).

#### [tox.ini](tox.ini): testing with tox [tox](tox.readthedocs.org)

Tox is one level up from py.test and can serve as an easy testrunner for different kinds of local tests and also acts a a frontend for external test runners as part of [CI](https://en.wikipedia.org/wiki/Continuous_integration). It automatically creates an environment for the tests, installs the dependencies and the package under tests and outputs the results.

command line usage:

    $ cd </path/to/your/clone>
    $ tox
    
output like: 

    flake8 develop-inst-nodeps: </path/to/your/clone>
    flake8 installed: flake8==2.5.4,mccabe==0.4.0,-e git+git@github.com:obestwalter/mau-mau.git@ba0af5660852415dc8cd44a499ad0a67958119be#egg=OOOMMM-master,pep8==1.7.0,py==1.4.31,pyflakes==1.0.0,pytest==2.9.1,wheel==0.24.0
    flake8 runtests: PYTHONHASHSEED='2381292392'
    flake8 runtests: commands[0] | flake8 </path/to/your/clone>/mau_mau </path/to/your/clone>/tests --show-source
    tests develop-inst-nodeps: </path/to/your/clone>
    tests installed: flake8==2.5.4,mccabe==0.4.0,-e git+git@github.com:obestwalter/mau-mau.git@ba0af5660852415dc8cd44a499ad0a67958119be#egg=OOOMMM-master,pep8==1.7.0,py==1.4.31,pyflakes==1.0.0,pytest==2.9.1,wheel==0.24.0
    tests runtests: PYTHONHASHSEED='2381292392'
    tests runtests: commands[0] | py.test </path/to/your/clone>/tests
    ============================= test session starts =============================
    platform linux -- Python 3.4.3, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    rootdir: </path/to/your/clone>/tests, inifile: tox.ini
    collected 13 items 
    
    tests/test_pile.py .....
    tests/test_player.py ...
    tests/test_sim.py .....
    
    ========================== 13 passed in 0.03 seconds ==========================
    ___________________________________ summary ___________________________________
      flake8: commands succeeded
      tests: commands succeeded
      congratulations :)

This is a very simple setup. There are many more [configuration options](https://tox.readthedocs.org/en/latest/config.html)

### [.travis.yml](.travis.yml): integrate with [Travis CI](https://travis-ci.org/)

The badge on top of this `README` shows the [build status from Travis CI](https://travis-ci.org/obestwalter/mau-mau). 

This is a very simple setup. There are many more [configuration options](https://docs.travis-ci.com/user/languages/python).

# Updating the documentation

The documentation is generated with [MkDocs](http://www.mkdocs.org/) and the means to build it live in `docs`.

### Building the documentation

When you work on the documentation you can start a local server:

    $ cd <path/to/your/clone>
    $ tox -e docs-auto
    
results are in `<path/to/your/clone>/docs/_build`
