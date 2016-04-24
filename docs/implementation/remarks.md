# Remarks

## Significant whitespace

Python is a language where space matters ... meaning  units of code (blocks, function bodies, etc.) are delimited by a colon (`:`) and indentation (4 spaces by convention) of all the following lines that belong to that block. A good editor that is language aware will help with that. It [indents](http://www.diveintopython.net/getting_to_know_python/indenting_code.html) the code automatically after ending a line with a colon. It also lets you indent and dedent entire blocks of code that are marked by pressing the `Tab` key and [outdents](https://www.jetbrains.com/pycharm/webhelp/changing-indentation.html?) them when pressing `Shift + Tab`. 

See also: [code layout](https://www.python.org/dev/peps/pep-0008/#code-lay-out) in PEP8.

Example:

```python
def my_super_function():
    print("I am indented with 4 spaces")
    print("Me too! I belong to the function")
print("I am not inside the function block anymore :(")

for currentElement in range(5):
    print(currentElement)
    print("I also belong to the loop block")
print("I don't belong to the loop block anymore")
```

## **Everything** is an object

Everything. Even functions, classes, modules and files. Everything.

In this [Python Online Tutor example](http://goo.gl/Yqt7hL) you can see how really, really everything in a running Python program is an object.

## Passing by assignment

> Remember that arguments are passed by assignment in Python. Since assignment just creates references to objects, there’s no alias between an argument name in the caller and callee, and so no call-by-reference per se.

> -- [How do I write a function with output parameters (call by reference)?](https://docs.python.org/3.5/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)

The way passing data to functions work in Python is [quite specific](https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/), so it is important that you are aware of it and understand it. Walk through this example in the [tutor](http://goo.gl/MeBNPV) to visualize what is really happening when you pass mutable objects into functions and e.g. append elements to a list object that was passed into a function. In the example it is a list but this holds true for any object that contains references to other objects.

Changing the state of an object that is not returned explicitly is called a [side effect](https://goo.gl/3n4nXW). Purists of certain programming paradigms would tell you that this style is messy and error prone. I won't argue with them, because I might lose. For now that's how we do it here, because than you really understand how it works. Real world programs have lots of side effects anyway so better just get used to it :) The discussion around when and how to use side effects is a huge topic. For now I just want to make you aware that some of our functions and methods have side effects, meaning that not all changes to the state of the program are communicated purely by returning values. BTW: raising exceptions are also considered side effects and they are used a lot in Python.

## Magic methods (protocols)

Those `__something__()` thingies might look scary for the uninitiated, but you will love them, once you got the idea. These methods are a way to use the internal language mechanics of Python for your own classes. They make up an important part of the Python superpowers and it's never too early to learn about them (you should at least know that they exist and that they have special meaning). Some of them are used in the model classes to create pythonic behaviour of the objects (e.g. make them iterable and comparable) and good representations.

### Object representation (`__repr__`)

> If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value

> -- [Python docs](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#object.__repr__)

In this simple simulation this is actually possible for all objects, so why not do it? This makes it possible to copy object representations from the output and recreate them in the REPL to experiment with them. If done right this works correctly when using inheritance as well (see `Stock` and `Waste`).

This could also be useful: [reprlib helps making better representations](https://docs.python.org/3.5/library/reprlib.html).

### Make your own objects behave like built in data types

* let an object have a [length (`__len__`)](https://docs.python.org/2/reference/datamodel.html#object.__len__) and a concept of being `True` or `False` depending on having a length > 0 or not.
* make an object [iterable (`__iter__`)](https://docs.python.org/2/reference/datamodel.html#object.__iter__).

### Other uses of special object attributes

All objects have a [name (`__name__`)](https://docs.python.org/2/library/stdtypes.html?highlight=__name__#class.__name__)

The name attribute of module objects are set dynamically depending on the context in which the module is loaded. If the module is run like a script it has a different name than when it is imported by another module. The names of modules are used for two purposes in this program:

1. Set the name of the logger object to get information from where the log was written
1. If a module is started directly it has the special name `__main__` - this can be used to only execute certain code if it is meant to behave like a script (as opposed to being imported as a module). This is the [canonic way](https://docs.python.org/3/library/__main__.html) to do this. 

**More resources about magic methods**

* [Python docs](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#special-method-names)
* [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)

## Assertions

> What can be asserted without evidence can be dismissed without evidence.

> -- Christopher Hitchens

To assert something means "to state or express positively". Assertions are regarded as important enough in Python that [`assert` is a statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) (since Python 3 even `print` is not important enough to be a statement). `assert` evaluates an expression and raises an [`AssertionError`](https://docs.python.org/3/library/exceptions.html?highlight=assert#AssertionError) if the result of the evaluation is `False` (with a customizable message to provide more information about the problem). This can be a very simple check like making sure that an object is [truthy](https://docs.python.org/3/library/stdtypes.html#truth) if evaluated as [`bool`](https://docs.python.org/3/library/functions.html#bool). 

```Python
def spam(someObject):
    assert someObject, "Hey! %s is not what I want!" % (someObject)
    print(someObject)
    
spam([1, 2])
spam([])
```

The assert in the `spam` function makes sure that the argument passed evaluates to `True` before moving on. The first call is o.k. but the second raises the exception and prints the message as part of the traceback.

This is a good way to make sure that your program crashes early if the preconditions are not what you expect them. Like making sure there is a chair under your bottom before you make an attempt to sit down. Used with good measure this can safe you a lot of trouble - finding the good measure for usage of the assert statement in your code is an art and not a science.

Look for uses of the assert statement in the code to get an idea how it might be used.

## Logging

Python has a simple to use and convenient [logging module](https://docs.python.org/3.5/library/logging.html) included. There is no reason why beginners shouldn't learn using that right away in their programs instead of cluttering the code with calls to `print`. One immediate advantage is the possibility to use different [log levels](https://docs.python.org/3.5/library/logging.html) in the program and adjust the output when debugging problems (e.g. `logging.DEBUG` to see the full story while debugging and `logging.WARNING` when running thousands of simulations, where logging would slow us down).

We use a [simple format](https://docs.python.org/3.5/library/logging.html#logrecord-attributes) and the [convenience function](https://docs.python.org/3.5/library/logging.html#logging.basicConfig) to initialize the logger to write to the terminal with a certain level.
