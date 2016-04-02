# Mau Mau (Part of the [Python Exploration Toolkit](https://github.com/obestwalter/pet))

Simple card game simulation to showcase a "real" Python application.

This implementation is only using the basic rules of the game. [Mau Mau](https://goo.gl/r7D63W) can have a lot of special rules, which might be implemented in later versions.

The players have no strategies yet either, they just play the first playable card they find in their hand and play it.

## Things to point out

### Logging

Python has a simple to use and convenient [logging module](https://docs.python.org/3.5/library/logging.html) included. There is no reason why beginners shouldn't learn using that right away in their programs instead of cluttering the code with calls to `print`. One immediate advantage is the possibility to use different [log levels](https://docs.python.org/3.5/library/logging.html) in the program and adjust the output when debugging problems (e.g. `logging.DEBUG` to see the full story while debugging and `logging.WARNING` when running thousands of simulations, where logging would slow us down).

We use a simple format and the [convenience function](https://docs.python.org/3.5/library/logging.html#logging.basicConfig) to initialize the logger to write to the terminal with a certain level.


## Tests

The ability to write simple functions to test your code cannot be developed early enough, so why not start this right away as well? The examples are dead simple and not covering much yet, but show that it's not rocket science to write automatic tests for your code.

We are using [py.test](http://pytest.org). The default testrunner in PyCharm is Unittest. **Find Action: default testrunner**: set to py.test and accept offer to install it

### Special attribute names

those `__something__()` thingies might look scary for the uninitiated, but you will live them, once you got the principle. They are one of the things that make up some of the Python superpowers and it's never to early to learn about them. Some of them are used in the model classes to create pythonic behaviour and good representations.

* [Python docs](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#special-method-names)

#### Object representation (`__repr__`)

> If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value

> -- [Python docs](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#object.__repr__): 

In our simple simulation this is actually possible for all object, so why not do it? You can copy object representations from the log, for example, and recreate them in the REPL. If done right this works correctly when using inheritance as well (see `Stock` and `Waste`).

`__name__` is an example for a special attribute of a module object. We use it for two purposes in the program:

1. Set the name of the logger object to get information from where the log was written
1. If a module is started directly it has the special name '__main__' - this we use to only execute certain code if the module was started directly. This is the [canonic way](https://docs.python.org/3/library/__main__.html) to do this. 

**further information**

* [reprlib helps making better representations](https://docs.python.org/3.5/library/reprlib.html)

### Parameter passing by object sharing

The `play_turn` function could als be a method of `Game`. Vice versa the `next_turn` method could just as well be a function. This works without having to return the objects which are changed in the functions, because only their contents are modified. This way parameters work in Python is very specific in Python, so it is important, that you are aware of it and understand it. 

Changing the state of an object that is not returned explicitly is called a [side effect](https://goo.gl/3n4nXW) it is not automatically a BadThing and the discussion around when and how to use them is a huge topic. For now I just want to make you aware here, that our functions have side effects, meaning that not all changes to the state of the program are done by returning values. Raising exceptions are als side effects and they are used a lot in Python.
