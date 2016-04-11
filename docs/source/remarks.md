## Things to point out

### Python does argument passing by assignment

> Remember that arguments are passed by assignment in Python. Since assignment just creates references to objects, there’s no alias between an argument name in the caller and callee, and so no call-by-reference per se.

> -- [How do I write a function with output parameters (call by reference)?](https://docs.python.org/3.5/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)

In our code the `play_turn` function could als be a method of the `Game` class. Vice versa the `next_turn` method could just as well be a function. This works without having to return the objects which are modified in the functions, because only their contents are modified. The way passing data to functions work in Python is [quite specific](https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/), so it is important, that you are aware of it and understand it. Walk through this example in the [tutor](http://goo.gl/MeBNPV) to visualize what is really happening when you pass mutable objects into functions and e.g. append elements to a list object that was passed into a function. In the example it is a list but this holds true for any object that contains references to other objects. To use an example in `play_turn`: the player object is passed in and it contains a reference to the players' `hand`. If the player plays a card it will taken from the hand and it is not necessary to either return the player object or in some way to communicate the update of the `hand`. 

Changing the state of an object that is not returned explicitly is called a [side effect](https://goo.gl/3n4nXW). Purists of certain programming paradigms would tell you that this style is messy and error prone. I won't argue with them, because I might loose. For now that's how we do it here, because than you really understand how it works. Real world programs have lots of side effects anyway so better just get used to it :) The discussion around when and how to use side effects is a huge topic. For now I just want to make you aware, that some of our functions and methods have side effects, meaning that not all changes to the state of the program are communicated purely by returning values. BTW: raising exceptions are also considered side effects and they are used a lot in Python.

### Assertions

> What can be asserted without evidence can be dismissed without evidence.

> -- Christopher Hitchens

To assert something means "to state or express positively". Assertions are regarded as important enough in Python, that [`assert` is a statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) (since Python 3 even `print` is not important enough to be a statement). `assert` evaluates an expression and raises an [`AssertionError`](https://docs.python.org/3/library/exceptions.html?highlight=assert#AssertionError) if the result of the evaluation is `False` (with a customizable message to provide more information about the problem). This can be a very simple check like making sure that an object is [truthy](https://docs.python.org/3/library/stdtypes.html#truth) if evaluated as [`bool`](https://docs.python.org/3/library/functions.html#bool). 

```Python
def spam(someObject):
    assert someObject, "Hey! %s is not what I want!" % (someObject)
    print(someObject)
    
spam([1, 2])
spam([])
```

The assert in the `spam` function makes sure, that the argument passed evaluates to `True` before moving on. The first call is o.k. but the second raises the exception and prints the message as part of the traceback.

This is a good way to make sure that your program crashes early if the preconditions are not what you expect them. Like making sure there is a chair under your bottom before you make an attempt to sit down. Used with good measure this can safe you a lot of trouble - finding the good measure for usage of the assert statement in your code is an art and not a science.

Look for uses of the assert statement in the code to get an idea how it might be used.

### Logging

Python has a simple to use and convenient [logging module](https://docs.python.org/3.5/library/logging.html) included. There is no reason why beginners shouldn't learn using that right away in their programs instead of cluttering the code with calls to `print`. One immediate advantage is the possibility to use different [log levels](https://docs.python.org/3.5/library/logging.html) in the program and adjust the output when debugging problems (e.g. `logging.DEBUG` to see the full story while debugging and `logging.WARNING` when running thousands of simulations, where logging would slow us down).

We use a [simple format](https://docs.python.org/3.5/library/logging.html#logrecord-attributes) and the [convenience function](https://docs.python.org/3.5/library/logging.html#logging.basicConfig) to initialize the logger to write to the terminal with a certain level.

### 'Magic' methods (protocols)

Those `__something__()` thingies might look scary for the uninitiated, but you will love them, once you got the idea. These methods are a way to use the internal language mechanics of Python for your own classes. They make up an important part of the Python superpowers and it's never too early to learn about them (you should at least know that they exist and that they have special meaning). Some of them are used in the model classes to create pythonic behaviour of the objects (e.g. make them iterable and comparable) and good representations.

#### Object representation (`__repr__`)

> If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value

> -- [Python docs](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#object.__repr__)

In our simple simulation this is actually possible for all objects, so why not do it? You can copy object representations from the log, for example, and recreate them in the REPL. If done right this works correctly when using inheritance as well (see `Stock` and `Waste`).

#### Special module attribute (`__name__`)

`__name__` is an example for a special attribute of a module object. We use it for two purposes in the program:

1. Set the name of the logger object to get information from where the log was written
1. If a module is started directly it has the special name `__main__` - we use this to only execute certain code if the module was started directly (as opposed to being imported as a module). This is the [canonic way](https://docs.python.org/3/library/__main__.html) to do this. 

##### Further information

* [Python docs](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#special-method-names)
* [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)
* [reprlib helps making better representations](https://docs.python.org/3.5/library/reprlib.html)
