## [setup.py](https://github.com/obestwalter/mau-mau/blob/master/setup.py): make installable

The code of the actual software lives in[mau_mau/](https://github.com/obestwalter/mau-mau/tree/master/mau_mau/)

**NOTE:** Please replace `</path/to/your/clone>` with the actual path on your computer.

To develop or explore the code it is best if you install the [package as editable](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) into a virtualenv. This way all the paths are working correct for all use cases (e.g. running the tests) and the command line access `mau-mau` is also installed.

Install the package and all dependencies necessary for development as editable with:

        $ cd </path/to/your/clone>
        $ pip install --editable '.[all]'
      
## [play.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/play.py): The 'story'

The overall plot of the Mau Mau story can be found here. It is written in an [imperative](https://en.wikipedia.org/wiki/Imperative_programming) way (like a series of commands given to the computer). The code looks like a series of instructions which are to be carried out in a top down order, descending into the functions being called. The order can be influenced by loops (`for ... in` or `while`) and conditioned branches (`if ... then ... else`). These are the basic control flow constructs Python has. There are a few more, but not many.

**Behold! The whole program in 6 lines!**

```python
def play_game(rulesOfTheGame, players):
    game = setup_game(rulesOfTheGame, players)
    while not game.over:
        player = game.next_turn()
        player.play_turn(game.table)
    return game
```

This is the meat of the simulation. Here is where all the magic happens. if you call this function a game of Mau Mau will be simulated and a winner is determined. **6 lines of code** including the function header and the return statement. You now have read the whole plot of the fascinating Mau Mau story. If you want to understand more, you can start digging deeper and visit the definitions of the functions used in the `play_game` function. Reading and understanding the functions (in whatever order you might prefer) in this file means that you get the picture how a simulation of a simple turn based card game works.

To dig deeper and get a more detailed understanding of the program, you can start to explore the classes, their attributes, behaviour and how they interact. 

## [concepts.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/concepts.py): Abstract stuff

The general concepts used in the game as classes.

## Modules defining the classes

These look pretty different from `game.py` and they are. Here is where the object oriented part of the story kicks in. If `game.py` contains the plot, these modules contain the descriptions of the actors and props of the story. They describe the relevant part of the virtual universe that is created to run the simulation. It contains custom data structures (a.k.a. classes) to model the problem of simulating Mau Mau. You should be able to read through the classes and get an idea of what elements are needed to simulate a card game and how they might interact.

### [subjects.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/subjects.py) and [objects.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/objects.py)

I know .. in Python everything is an object, so this would be meaningless. This is also not [subject oriented programming](https://en.wikipedia.org/wiki/Subject-oriented_programming). These are just good terms for what those classes describe in the context of the program: there are objects in the game which are manipulated by the subjects.

### [rules.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/rules.py)

This contains the classes that implement the rules of Mau Mau. Start reading with the `MauMau` class and see if you can figure out how it works. There is always one concrete rule active on the table that is valid for the currently played round. Sometimes information gets transferred from one rule to the next (e.g. if a 7 was put on a seven, the number of draws have to accumulate). 

### [strategy.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/strategy.py)

**Note:** A player has a strategy, but the player also attaches it to the active rule, so that it can be queried for the wanted suit if a Jack is on the table.

#### `BasicStrategy` 

just plays according to the rules and always chooses random antidotes and cards. If playing a Jack it always asks for the suit it has the most of. 

This can be extended upon to implement "real" strategies.

#### `HumanStrategy`
 
Mainly to show that the existing design makes it very easy to even add interactivity to let a human play against a computer (`mau-mau human`).

## Command line access: [cli.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/cli.py)

This contains the code for the commandline interface. Its function `main` is configured in `setup.py` to act like a program called `mau-mau` that is accessible where the package is installed. At the moment the following can be accessed from the commandline:

## Statistics: [stats.py](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/stats.py)

Contains some functions to run the game simulations and collect statistics. See [usage examples](../guide/usage.md#collect-statistics)
