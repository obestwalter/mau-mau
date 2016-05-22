# Automatic tests

[py.test](http://pytest.org) is my tool of choice. There is also a [standard library solution](https://docs.python.org/3/library/unittest.html), which has too much API overhead for my taste. py.test does some very [clever things](https://pytest.org/latest/assert.html) to let you use the assertion statement directly and you get much better failure reports. This makes for much cleaner test code and less painful testing. 

!!! note 
    The sources of the test modules are here: [tests/](https://github.com/obestwalter/mau-mau/tree/4.0.1/tests)

The ability to write simple functions to test your code cannot be developed early enough, so why not start this right away as well? The examples are dead simple and not covering much yet, but show that it's not rocket science to write automatic tests for your code. Pytest makes it possible to use the inbuilt `assert` for writing tests.

## py.test (command line)

py.test looks for modules with the pattern `test_*.py` downwards from your [cwd](https://en.wikipedia.org/wiki/Working_directory). In those modules it looks for `def test_*` and `class Test*`. After collecting everything fitting those patterns it execute all test functions and reports back.

    $ cd </path/to/your/clone>
    $ py.test
    
Example for a successful run:

    ========================== test session starts ==========================
    platform linux -- Python 3.4.3, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    rootdir: </path/to/your/clone>, inifile: tox.ini
    collected 13 items 
    tests/test_pile.py .....
    tests/test_player.py ...
    tests/test_sim.py .....
    ======================= 13 passed in 0.03 seconds =======================

Example for a not so successful run:
    
    ======================= test session starts =============================
    platform linux -- Python 3.4.4, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    rootdir: </path/to/your/clone>, inifile: tox.ini
    collected 35 items 
    
    tests/test_concepts.py ...................
    tests/test_objects.py ..F..
    tests/test_player.py ...
    tests/test_rules.py ...
    tests/test_sim.py .....
    ======================== short test summary info ========================
    FAIL tests/test_objects.py::test_non_empty_stock
    
    =============================== FAILURES ================================
    _________________________ test_non_empty_stock __________________________
    
        def test_non_empty_stock():
    >       assert not Stock([0])
    E       assert not Stock([0])
    E        +  where Stock([0]) = Stock([0])
    
    tests/test_objects.py:17: AssertionError
    ==================== 1 failed, 34 passed in 0.21 seconds ================

This test failed not because the code is broken, but because I made a wrong assertion about the behaviour of the `Stock` class. If you pass a list when you create the class (like `Stock([Card('Queen', '♠'), Card('10', '♠')])`), you should not expect it to be empty afterwards.

### Automatically run tests on changes:

If you want to take this one step further and have the tests being run automatically every time the code changes, you can:

    $ pip install pytest-watch
    $ cd </path/to/your/clone>
    $ ptw --onfail 'notify-send --urgency=critical "FAIL"' --onpass 'notify-send "PASSED"'
    
`notify-send` is how I can send desktop notifications from the commandline in my os ([Linux](https://wiki.archlinux.org/index.php/Desktop_notifications)). There are lots of ways to do this on every os - even [Windows](https://github.com/nels-o/toaster) and [Mac](https://github.com/julienXX/terminal-notifier).

## py.test (PyCharm)

### Preparation

The default testrunner in PyCharm is Unittest. You have to switch to py.test like so: 
* **Find Action: [default testrunner](https://www.jetbrains.com/help/pycharm/2016.1/testing-frameworks.html)**: set to py.test 
* accept offer to install it in your project virtualenv or do it yourself with `pip install pytest`

### Running tests

Depending on where you are, you can run all tests or a part of them. The magic action is [`run context configuration`](https://www.jetbrains.com/help/pycharm/2016.1/creating-and-saving-temporary-run-debug-configurations.html). It runs what is sensible in the context. If your focus is in a normal script it runs the script and if the focus is in a module defining tests it will run the configured testrunner with the tests. Running the context configuration with ...

* Focus in the editor, inside a specific test
* Focus in the editor on the line defining a class containing tests
* Focus in the **Project Tool Window**, choose the `tests/` folder and 

... all yields different results as which tests are run (and they are what you would intuitively expect).

## Doctests

You can write simple examples that can double as tests directly in documentation strings. They are called [doctests](https://docs.python.org/3.5/library/doctest.html). You can [run them directly from PyCharm](https://www.jetbrains.com/help/pycharm/2016.1/run-debug-configuration-doctest.html) as well.

For an example in the code see [concepts.py](https://github.com/obestwalter/mau-mau/blob/4.0.1/mau_mau/concepts.py)
