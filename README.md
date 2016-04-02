# Mau Mau (Part of the [Python Exploration Toolkit](https://github.com/obestwalter/pet))

Simple card game simulation to showcase a "real" Python application.

This implementation is only using the basic rules of the game. [Mau Mau](https://goo.gl/r7D63W) can have a lot of special rules, which might be implemented in later versions.

The players have no strategies yet either, they just play the first playable card they find in their hand and play it.

## Things to point out

### Logging

Python has a simple to use and convenient [logging module](https://docs.python.org/3.5/library/logging.html) included. There is no reason why beginners shouldn't learn using that right away in their programs instead of cluttering the code with calls to `print`. One immediate advantage is the possibility to use different [log levels](https://docs.python.org/3.5/library/logging.html) in the program and adjust the output when debugging problems (e.g. `logging.DEBUG` to see the full story while debugging and `logging.WARNING` when running thousands of simulations, where logging would slow us down).

We use a simple format and the [convenience function](https://docs.python.org/3.5/library/logging.html#logging.basicConfig) to initialize the logger to write to the terminal with a certain level.


### Automatic tests with [py.test](http://pytest.org)

The ability to write simple functions to test your code cannot be developed early enough, so why not start this right away as well? The examples are dead simple and not covering much yet, but show that it's not rocket science to write automatic tests for your code.

**Warning**: the default testrunner in PyCharm is Unittest. Switch to py.test like so: 
* **Find Action: default testrunner**: set to py.test 
* accept offer to install it in your project virtualenv or do it yourself with pip install pytest

### Use of custom [classes](https://docs.python.org/3.5/tutorial/classes.html)

Yes I know, you basically just learned about functions and variables inside of modules, but by having learned that you know almost everything already to start writing your own classes. The modelling problem we have here is a good fit to create your own data structures (which classes are), so here they are and they don't bite. 

### 'Magic' methods

Those `__something__()` thingies might look scary for the uninitiated, but you will love them, once you got the idea. These methods are a way to use the internal language mechanics of Python for your own classes. They make up some of the Python superpowers and it's never to early to learn about them (you should at least know that they exist and that they have special meaning). Some of them are used in the model classes to create pythonic behaviour of the objects (e.g. make them iterable and comparable) and good representations.

#### Object representation (`__repr__`)

> If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value

> -- [Python docs](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#object.__repr__): 

In our simple simulation this is actually possible for all object, so why not do it? You can copy object representations from the log, for example, and recreate them in the REPL. If done right this works correctly when using inheritance as well (see `Stock` and `Waste`).

#### Special module attribute (`__name__`)

`__name__` is an example for a special attribute of a module object. We use it for two purposes in the program:

1. Set the name of the logger object to get information from where the log was written
1. If a module is started directly it has the special name `__main__` - we use this to only execute certain code if the module was started directly (as opposed to being imported as a module). This is the [canonic way](https://docs.python.org/3/library/__main__.html) to do this. 

##### Further information

* [Python docs](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#special-method-names)
* [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)
* [reprlib helps making better representations](https://docs.python.org/3.5/library/reprlib.html)

### Parameter passing by object sharing

The `play_turn` function could als be a method of `Game`. Vice versa the `next_turn` method could just as well be a function. This works without having to return the objects which are changed in the functions, because only their contents are modified. This way parameters work in Python is very specific in Python, so it is important, that you are aware of it and understand it. 

Changing the state of an object that is not returned explicitly is called a [side effect](https://goo.gl/3n4nXW) it is not automatically a BadThing and the discussion around when and how to use them is a huge topic. For now I just want to make you aware here, that our functions have side effects, meaning that not all changes to the state of the program are done by returning values. Raising exceptions are als side effects and they are used a lot in Python.
