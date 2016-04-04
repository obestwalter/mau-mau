# Mau Mau 

**Part of the [Python Exploration Toolkit](https://github.com/obestwalter/pet)**

This serves to showcase a complete Python application and explores an approach to development that could be called "programming as non-linear storytelling".

## OOOMMM (Obvious Object Oriented Mau Mau Modelling)

### The rules of Mau Mau

>  The game is played with a regular deck of playing cards. The players are dealt each a hand of cards (usually 5). The rest are placed face down as the drawing stack. At the beginning of the game the topmost card is revealed, then the players each get a turn to play cards.

> One can play a card if it corresponds to the suit or value of the open card. E.g. on a 10 of spades, only other spades can be played or other 10s. If a player is not able to, they draw one card from the stack. If he can play this card, he may do so, otherwise he keeps the drawn card and passes his turn. If the drawing stack is empty, the playing stack (except for the topmost card) is shuffled and turned over to serve as new drawing stack.

> -- [Wikipedia - Mau Mau](https://goo.gl/r7D63W)

### How to turn that into a program?

Switching into egghead mode, you could say that a game of Mau Mau can be modelled as a series of interactions between actors with state preserving attributes and behaviours modifying their own state and initiating reactions in other actors. If you call the actors objects and the behaviour methods you have a basic description of object oriented programming.

One koan in the Zen of Python says: "If the implementation is easy to explain, it may be a good idea". Let's put this to the test and explain the implementation of our Mau Mau program by simply describing the conditions and rules of the game using a rough approximation of the programs' terminology and see if the objects and their interactions make the implementation look obvious. Objects used in the program are marked `like this` ; functions that describe interactions are marked like **this**).

The `Player`s in the `cardroom` are `invited` to a `Game` at the `Table`. A `deck` of `Card`s is **shuffled**. The same amount of cards is **dealt** to the `player`s to form their `hand`. One `card` - the `upcard` - is **draw**n from the `stock` and placed face up on the `table`. The remaining cards are `_Pile`d face down on the `Table` and form the `stock`. Now all is in place to **play** the `game`. The `players` play in `turns`. They choose a`card` that **is playable** with the `upcard` according to the rules (same `suit` or same `value`) and place it on the `table`. The played `card` ist the new  `upcard` and the old `upcard` is now part of the `Waste`. Now the next `player` is up. If a player can't find a `card` to play, they have to draw one from the `stock` and the next `player` is up. If the `stock` `isEmpty`, the `waste` `card`s will be **shuffle**d to form a new `stock`. The game is over and the `winner` is found as soon as one `player` plays the last card of their `hand`.

This description of the rules and the gameplay can double already as a high level description of the implementation of the game. It can also be read as an abstract story about a game, where the concrete story would be the description of an actual game. The program code can be viewed as an abstract story, with different executions of it as concrete expressions. If you have no idea what I mean just watch [this](https://www.youtube.com/watch?v=oP3c1h8v2ZQ) and transfer your insights into thinking about abstract program code and its conrete execution :)

## Programming as non-linear storytelling

Earlier on the term "programming as non-linear storytelling" was introduced. I have to admit that this is a term I just made up. I was trying to come up with a term of how (IMHO) working code often comes into being and how it should also be read or better: explored. Most of the time when I think that I came up with a new term for something, I find out that somebody already wrote a paper about it in 1972. So, when I come up with a term or concept that I think could be original, I deflate my ego right away by [googling it](https://goo.gl/JGfXTL). I then usually find a whole bunch of blogs and articles that use that term already and most of the time explain it better than I could. With this one I drew **almost** a blank. The links referred to non-linear storytelling in computer games or maths topics that did nonlinear stuff with things (don't ask me - I am really not into maths). But not programming. The very first hit though was an article about Ji-Sun Ham who uses a visual programming language called [Scratch](https://scratch.mit.edu/) to teach kids programming. The following quotes resonated with me:

> She started with a survey of current software developers, asking if they thought programming was a linear or non-linear process. "The surprising result was that the more number of years a programmer had under his or her belt, he or she was more inclined to say it's non-linear versus those with only one to three years, who would say that it's more linear than non-linear. I wondered how that could affect those wanting to learn how to program but then got discouraged because they can't think that linearly. Since it was always presented that way in school, how might a non-linear way encourage more students to learn programming isn't so intimidating?"

> \[...\]

> Ji-Sun's experience learning with Scratch and creating for other's learning with Scratch has challenged her assumptions about programming, storytelling, and personalized learning. "Programming isn't scary, and it's not only a certain group of people can really program. Programming isn't as linear as you think it is, just as storytelling really isn't as linear as you think it is."

> [Reading, Writing, Remixing: Programming Non-Linear Stories with Scratch](http://scratched.gse.harvard.edu/stories/reading-writing-remixing-programming-non-linear-stories-scratch)

Telling a story by starting in the middle and jumping back and forth on the timeline and switching between minute details and bird's eye views is a lot how you go about creating software and also how you should go about exploring an existing code base that you want to use or adapt. Code is not linear. Period. Please don't try reading the source code of any non trivial piece of software from top to bottom, file by file. Calling it reading code is very misleading - it should be called "decoding code" or "exploring code". After all: there is a reason why it's called code. 

Another hint that writing and reading software is not as linear and logical as it might seem is that the alternative translation of my german job description ("Software Entwickler") is "Software Unraveller". How fitting. I unravel software -  I don't develop it :)

## Exploring / unraveling the code

This is a very neat little project that is pretty optimized for being readable and easy to grasp. It is not a toy example, but the nasty details that usually screw with our nice and simple design and make the code grow tentacles and other cruft is not (yet) part of the code and so it can be read like a nice story. Even in this simple state it is already non-linear though and it came into live in a non-linear fashion.

### [`sim.py`](sim.py)

The overall plot of the Mau Mau story can be found here. It is described in an [imperative](https://en.wikipedia.org/wiki/Imperative_programming) way. You can read it as a series of commands given to the computer to simulate the game. The code looks like a series of instructions which are to be carried out in a specific order. The order can be influenced by loops (`for ... in` or `while`) conditioned branches (`if ... then ... else`). These are the basic control flow constructs Python has. There are a few more, but not many.

#### The central simulation function

```python
def play_game(players=3, cardsPerPlayer=5):
    game = start_new_game(players, cardsPerPlayer)
    while not game.over:
        game.next_turn()
        play_turn(game.player, game.table)
    return game
```

This is the meat of the simulation. Here is where all the magic happens. if you call this function a game of Mau Mau will be simulated and a winner is determined. **6 lines of code** including the function header and the return statement. You now have read the whole plot of the fascinating Mau Mau story. If you want to understand more, you can start digging deeper and visit the definitions of the functions used in the play function. Reading and understanding the functions (in whatever order you might prefer) in this file means that you get the picture how a simulation of a simple turn based card game works.

### [`cardroom.py`](cardroom.py)

This looks pretty different from `sim.py` and it is. If `sim.py` contains the plot, `cardroom.py` contains the descriptions of the Actors and props of the story. It describes the relevant part of the virtual universe that is created to run the simulation. It contains custom data structures (a.k.a. classes) to model the problem of simulating Mau Mau. You should be able to read through the classes and get an idea of what elements are needed to simulate a card game and how they interact. The order in which the classes are defined are from complex to simple.

### [`stats.py`](stats.py)

Contains some functions to run the game simulations and collect statistics. 

### [`cli.py`](cli.py)

This is the entry point and can be executed from the command line. `python ./cli.py` or simply [`./cli.py`](cli.py) executes the standard function that runs simulations and creates statistics from the results ([`stats.time_durations`](stats.py#L25)). If you call it with a command line argument (e.g. `./cli.py mean_turns`)the argument will be passed to `get_function_from_name` that fetches a function object of the same name from [`sim.py`](stats.py) and executes it. This is a very simple way to create a flexible command line interface that doew not need to be changed if you create more statistics functions in `stats.py`. Adding a new function to `sim.py` will automatically make it accessible through the command line interface.

## Things to point out

### Logging

Python has a simple to use and convenient [logging module](https://docs.python.org/3.5/library/logging.html) included. There is no reason why beginners shouldn't learn using that right away in their programs instead of cluttering the code with calls to `print`. One immediate advantage is the possibility to use different [log levels](https://docs.python.org/3.5/library/logging.html) in the program and adjust the output when debugging problems (e.g. `logging.DEBUG` to see the full story while debugging and `logging.WARNING` when running thousands of simulations, where logging would slow us down).

We use a [simple format](https://docs.python.org/3.5/library/logging.html#logrecord-attributes) and the [convenience function](https://docs.python.org/3.5/library/logging.html#logging.basicConfig) to initialize the logger to write to the terminal with a certain level.


### Automatic tests with [py.test](http://pytest.org)

The ability to write simple functions to test your code cannot be developed early enough, so why not start this right away as well? The examples are dead simple and not covering much yet, but show that it's not rocket science to write automatic tests for your code.

**Warning**: the default testrunner in PyCharm is Unittest. Switch to py.test like so: 
* **Find Action: [default testrunner](https://www.jetbrains.com/help/pycharm/2016.1/testing-frameworks.html)**: set to py.test 
* accept offer to install it in your project virtualenv or do it yourself with `pip install pytest`

### Use of custom [classes](https://docs.python.org/3.5/tutorial/classes.html)

Yes I know, you basically just learned about functions and variables inside of modules, but by having learned that you know almost everything already to start writing your own classes. The modelling problem we have here is a good fit to create your own data structures (which classes are), so here they are and they don't bite. 

### 'Magic' methods

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

### Parameter passing by assignment

The `play_turn` function could als be a method of `Game`. Vice versa the `next_turn` method could just as well be a function. This works without having to return the objects which are changed in the functions, because only their contents are modified. The way passing data to functions work in Python is [quite specific](https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/), so it is important, that you are aware of it and understand it. Walk through this example in the [tutor](http://goo.gl/MeBNPV) to visualize what is really happening, when you pass mutable objects into functions and append elements there. In example it is a list but this holds true for any object that contains references to other objects.

Changing the state of an object that is not returned explicitly is called a [side effect](https://goo.gl/3n4nXW) it is not automatically a BadThing and the discussion around when and how to use them is a huge topic. For now I just want to make you aware here, that our functions have side effects, meaning that not all changes to the state of the program are done by returning values. Raising exceptions are als side effects and they are used a lot in Python.

See also the Python programming FAQ:

> Remember that arguments are passed by assignment in Python. Since assignment just creates references to objects, there’s no alias between an argument name in the caller and callee, and so no call-by-reference per se. You can achieve the desired effect in a number of ways.

> -- [How do I write a function with output parameters (call by reference)?](https://docs.python.org/3.5/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)
