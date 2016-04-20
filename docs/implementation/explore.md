# Explore the repository

To explore the code repository it is best if you install the [sources as editable](../dev/getting-started.md). This means you can use the application just like as if it would be installed normally but change the code and experiment.

## [play.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/play.py)

!!! note "Start exploring here"

The overall plot of the Mau Mau story can be found here. This is the entry point to start exploring the actual application. It is written in an [imperative](https://en.wikipedia.org/wiki/Imperative_programming) way (like a series of commands given to the computer). The code looks like a series of instructions which are to be carried out in a top down order, descending into the functions being called. The order can be influenced by loops (`for ... in` or `while`) and conditioned branches (`if ... then ... else`). These are the basic control flow constructs Python has. There are a few more, but not many.

**Behold! The whole program in 6 lines!**

```python
def play_game(rulesOfTheGame, players):
    game = setup_game(rulesOfTheGame, players)
    while not game.over:
        player = game.next_turn()
        player.play_turn(game.table)
    return game
```

This is the meat of the simulation. Here is where all the magic happens. if you call this function a game of Mau Mau will be simulated and a winner is determined. **6 lines of code** including the function header and the return statement. You now have read the whole plot of the fascinating Mau Mau story. If you want to understand more, you can start digging deeper and visit the definitions of the [functions](https://docs.python.org/3/glossary.html#term-function) and [classes](https://docs.python.org/3/tutorial/classes.html) used in the `play_game` function. Just start to explore the code and how the objects interact in whatever non-linear way you might prefer. This gives you an idea of how a simulation of a simple turn based card game can be implemented as a program.

## Modules defining the classes

These look pretty different from `game.py` and they are. Here is where the object oriented part of the story kicks in. If `game.py` contains the plot, these modules contain the descriptions of the actors and props of the story. They describe the relevant part of the virtual universe that is created to run the simulation. It contains custom data structures (a.k.a. classes) to model the problem of simulating Mau Mau. You should be able to read through the classes and get an idea of what elements are needed to simulate a card game and how they might interact.

### [concepts.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/concepts.py)

Classes that stand somehow stand conceptually above the objects and subjects.

### [objects.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/objects.py) and [subjects.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/subjects.py)

I know .. in Python everything is an object, so this would be meaningless. This is also not [subject oriented programming](https://en.wikipedia.org/wiki/Subject-oriented_programming). These are just good terms for what those classes describe in the context of the program: there are objects in the game which are manipulated by the subjects.

### [rules.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/rules.py)

This contains the classes that implement the rules of Mau Mau. Start reading with the `MauMau` class and see if you can figure out how it works. There is always one concrete rule active on the table that is valid for the currently played round. Sometimes information gets transferred from one rule to the next (e.g. if a 7 was put on a seven, the number of draws have to accumulate). 

### [strategy.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/strategy.py): how to play

**Note:** A player has a strategy, but the player also attaches it to the active rule, so that it can be queried for the wanted suit if a Jack is on the table.

#### BasicStrategy

Player plays according to the rules and always chooses random antidotes if they have any (e.g. 7 on 7 to prevent having to draw) or normal cards. If playing a Jack it always asks for the suit it has the most of. 

This can be extended upon to implement "real" strategies.

#### HumanStrategy
 
Mainly to show that the existing design makes it very easy to even add interactivity to let a human play against a computer (`mau-mau human`).

The impact of this is very likely to be zero on a planetary basis, as this is just a learning tool, but in general one should be very wary of implementing something just because it's easy:

> I call it my billion-dollar mistake. It was the invention of the null reference in 1965. At that time, I was designing the first comprehensive type system for references in an object oriented language (ALGOL W). My goal was to ensure that all use of references should be absolutely safe, with checking performed automatically by the compiler. But I couldn't resist the temptation to put in a null reference, simply because it was so easy to implement. This has led to innumerable errors, vulnerabilities, and system crashes, which have probably caused a billion dollars of pain and damage in the last forty years.

> -- Tony Hoare

... you have been warned.

### [stats.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/stats.py): create statistics

Contains functions to run the game simulations and collect statistics. See [usage examples](../guide/usage.md#collect-statistics)

### [cli.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/cli.py): command line access

This contains the code for the commandline interface. Its function `main` is configured in `setup.py` `entry_points` to act like a program called `mau-mau` that is accessible where the package is installed. At the moment the following can be accessed from the commandline:

## Peripherals

!!! note
    These files are not part of the actual software but are still vital for helping with development, installation, testing, etc. -- this makes all that tedious stuff you need when writing software less ... tedious.

### [setup.py](https://github.com/obestwalter/mau-mau/blob/master/setup.py): make installable

This module is what is being called, when the package is installed via pip or with `python3 setup.py`. This is the standard way of doing it in the Python ecosystem and it is documented [here](https://docs.python.org/3.5/distutils/setupscript.html). 
      
### [tox.ini](https://github.com/obestwalter/mau-mau/blob/master/tox.ini): developer task automation

This [INI](https://en.wikipedia.org/wiki/INI_file) file configures tasks that can run with the tox commands. The primary goal of tox is to automate testing and act as a frontend for CI, but it can be used for automating other developer tasks as well. See also [the developer documentation](../dev/tox.md) for this tox.ini.

### [.travis.yml](https://github.com/obestwalter/mau-mau/blob/master/.travis.yml) and [appveyor.yml](https://github.com/obestwalter/mau-mau/blob/master/appveyor.yml): CI for different versions and osses

See [documentation about CI](../dev/ci.md)

### [mkdocs.yml](https://github.com/obestwalter/mau-mau/blob/master/mkdocs.yml): developer task automation

See the [documentation for the documentation](../dev/docs.md) (I'm not kidding ...).
