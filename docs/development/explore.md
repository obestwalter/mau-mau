## [setup.py](setup.py): make installable

The code of the actual software lives in[mau_mau/](https://github.com/obestwalter/mau-mau/tree/master/mau_mau/)

**NOTE:** Please replace `</path/to/your/clone>` with the actual path on your computer.

To develop or explore the code it is best if you install the [package as editable](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) into a virtualenv. This way all the paths are working correct for all use cases (e.g. running the tests) and the command line access `mau-mau` is also installed.

Install the package and all dependencies necessary for development as editable with:

        $ cd </path/to/your/clone>
        $ pip install --editable '.[all]'
      
output like:

    Obtaining file:///</path/to/your/clone>
    Installing collected packages: mau-mau
      Running setup.py develop for mau-mau
    Successfully installed mau-mau

You now have an additional command in your virtualenv: `mau-mau`. The default behaviour if you call it, is to simulate a simple game of Mau Mau between three computer players (and you can see the hands of all the players and every step of the game).
        
        $ cd </path/to/your/clone>
        $ mau-mau

output like:

    root                53  main             : play_simple_game() ...
    mau_mau.subjects    28  invite           : invite [Player('Player 1', Hand([])), Player('Player 2', Hand([])), Player('Player 3', Hand([]))] to: Table(None, None)
    mau_mau.subjects    100 draw             : Player 1 <- Card('10', '♣')
    mau_mau.subjects    100 draw             : Player 1 <- Card('8', '♣')
    mau_mau.subjects    100 draw             : Player 1 <- Card('Ace', '♣')
    mau_mau.subjects    100 draw             : Player 1 <- Card('Ace', '♠')
    mau_mau.subjects    100 draw             : Player 1 <- Card('9', '♥')
    mau_mau.subjects    100 draw             : Player 2 <- Card('8', '♥')
    mau_mau.subjects    100 draw             : Player 2 <- Card('7', '♣')
    mau_mau.subjects    100 draw             : Player 2 <- Card('Queen', '♥')
    mau_mau.subjects    100 draw             : Player 2 <- Card('7', '♠')
    mau_mau.subjects    100 draw             : Player 2 <- Card('8', '♦')
    mau_mau.subjects    100 draw             : Player 3 <- Card('10', '♥')
    mau_mau.subjects    100 draw             : Player 3 <- Card('9', '♦')
    mau_mau.subjects    100 draw             : Player 3 <- Card('Jack', '♠')
    mau_mau.subjects    100 draw             : Player 3 <- Card('Jack', '♣')
    mau_mau.subjects    100 draw             : Player 3 <- Card('King', '♥')
    mau_mau.play        28  setup_game       : Start new game: Game(Table(MauMau(5), [Player('Player 1', Hand([Card('10', '♣'), Card('8', '♣'), Card('Ace', '♣'), Card('Ace', '♠'), Card('9', '♥')])), Player('Player 2', Hand([Card('8', '♥'), Card('7', '♣'), Card('Queen', '♥'), Card('7', '♠'), Card('8', '♦')])), Player('Player 3', Hand([Card('10', '♥'), Card('9', '♦'), Card('Jack', '♠'), Card('Jack', '♣'), Card('King', '♥')]))]))
    mau_mau.concepts    25  next_turn        : -------------------- turn 1 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('Queen', '♣')
    mau_mau.concepts    27  next_turn        : Player('Player 1', Hand([Card('10', '♣'), Card('8', '♣'), Card('Ace', '♣'), Card('Ace', '♠'), Card('9', '♥')])) is up
    mau_mau.strategy    17  play             : encountered rule BasicRule on Card('Queen', '♣')
    mau_mau.strategy    56  _play            : find card to play
    mau_mau.subjects    103 put              : play Card('10', '♣')
    [--- SNIP ---]
    mau_mau.concepts    25  next_turn        : -------------------- turn 27 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('Jack', '♥')
    mau_mau.concepts    27  next_turn        : Player('Player 3', Hand([Card('King', '♥'), Card('Queen', '♦'), Card('9', '♠')])) is up
    mau_mau.strategy    17  play             : encountered rule DemandWantedSuit on Card('Jack', '♥')
    mau_mau.strategy    56  _play            : find card to play
    mau_mau.strategy    65  _play            : nothing to play
    mau_mau.subjects    100 draw             : Player 3 <- Card('8', '♠')
    mau_mau.concepts    25  next_turn        : -------------------- turn 28 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('Jack', '♥')
    mau_mau.concepts    27  next_turn        : Player('Player 1', Hand([Card('Ace', '♠'), Card('King', '♠'), Card('7', '♥'), Card('King', '♦')])) is up
    mau_mau.strategy    17  play             : encountered rule DemandWantedSuit on Card('Jack', '♥')
    mau_mau.strategy    56  _play            : find card to play
    mau_mau.strategy    65  _play            : nothing to play
    mau_mau.subjects    100 draw             : Player 1 <- Card('Queen', '♠')
    mau_mau.concepts    25  next_turn        : -------------------- turn 29 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('Jack', '♥')
    mau_mau.concepts    27  next_turn        : Player('Player 2', Hand([Card('King', '♣')])) is up
    mau_mau.strategy    17  play             : encountered rule DemandWantedSuit on Card('Jack', '♥')
    mau_mau.strategy    56  _play            : find card to play
    mau_mau.subjects    103 put              : play Card('King', '♣')
    root                21  play_simple_game : And the winner is Player 2


## [`cli.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/cli.py): command line access

This contains the code for the commandline interface. Its function `main` is configured in `setup.py` to act like a program called `mau-mau` that is accessible where the package is installed. At the moment the following can be accessed from the commandline:

* `mau-mau`: If you do not pass anything a single game will be played with high verbosity settings in the logger
* `mau-mau <stats.function>`: e.g. `mau-mau mean_turns` - the argument will be passed to `get_function_from_name` that fetches a function object of the same name from [`stats.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/stats.py) and executes it. This is a very simple way to create a flexible command line interface that does not need to be changed if you create more statistics functions in `stats.py`. Adding a new function to `stats.py` will automatically make it accessible through the command line interface.
* `mau-mau interactive` ... or any other argument that does not map to a function in stats: play a game against the computer

See the different sections for more examples of commandline usage.

## [`game.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/play.py): the 'story'

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

## [`concepts.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/concepts.py)

The general concepts used in the game as classes.

## Modules defining the classes

These look pretty different from `game.py` and they are. Here is where the object oriented part of the story kicks in. If `game.py` contains the plot, these modules contain the descriptions of the actors and props of the story. They describe the relevant part of the virtual universe that is created to run the simulation. It contains custom data structures (a.k.a. classes) to model the problem of simulating Mau Mau. You should be able to read through the classes and get an idea of what elements are needed to simulate a card game and how they might interact.

### [`subjects.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/subjects.py) and [`objects.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/objects.py)

I know .. in Python everything is an object, so this would be meaningless. This is also not [subject oriented programming](https://en.wikipedia.org/wiki/Subject-oriented_programming). These are just good terms for what those classes describe in the context of the program: there are objects in the game which are manipulated by the subjects.

## [`rules.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/rules.py)

This contains the classes that implement the rules of Mau Mau. Start reading with the `MauMau` class and see if you can figure out how it works. There is always one concrete rule active on the table that is valid for the currently played round. Sometimes information gets transferred from one rule to the next (e.g. if a 7 was put on a seven, the number of draws have to accumulate). 

## [`strategy.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/strategy.py)

**Note:** A player has a strategy, but the player also attaches it to the active rule, so that it can be queried for the wanted suit if a Jack is on the table.

### `BasicStrategy` 

just plays according to the rules and always chooses random antidotes and cards. If playing a Jack it always asks for the suit it has the most of. 

This can be extended upon to implement "real" strategies.

### `HumanStrategy`
 
Mainly to show that the existing design makes it very easy to even add interactivity to let a human play against a computer.

Play interactive game:

    $ mau-mau human
 
output like:

    root                53  main             : play_interactive_game() ...
    mau_mau.subjects    28  invite           : invite [Player('Eric', Hand([])), Player('John', Hand([])), Player('human', Hand([]))] to: Table(None, None)
    mau_mau.subjects    100 draw             : Eric <- Card('Queen', '♠')
    mau_mau.subjects    100 draw             : Eric <- Card('10', '♠')
    mau_mau.subjects    100 draw             : Eric <- Card('Queen', '♣')
    mau_mau.subjects    100 draw             : Eric <- Card('8', '♦')
    mau_mau.subjects    100 draw             : Eric <- Card('7', '♠')
    mau_mau.subjects    100 draw             : John <- Card('9', '♠')
    mau_mau.subjects    100 draw             : John <- Card('Ace', '♠')
    mau_mau.subjects    100 draw             : John <- Card('10', '♦')
    mau_mau.subjects    100 draw             : John <- Card('Ace', '♣')
    mau_mau.subjects    100 draw             : John <- Card('8', '♥')
    mau_mau.subjects    100 draw             : human <- Card('Ace', '♦')
    mau_mau.subjects    100 draw             : human <- Card('7', '♦')
    mau_mau.subjects    100 draw             : human <- Card('King', '♥')
    mau_mau.subjects    100 draw             : human <- Card('9', '♦')
    mau_mau.subjects    100 draw             : human <- Card('King', '♠')
    mau_mau.play        28  setup_game       : Start new game: Game(Table(MauMau(5), [Player('Eric', Hand([Card('Queen', '♠'), Card('10', '♠'), Card('Queen', '♣'), Card('8', '♦'), Card('7', '♠')])), Player('John', Hand([Card('9', '♠'), Card('Ace', '♠'), Card('10', '♦'), Card('Ace', '♣'), Card('8', '♥')])), Player('human', Hand([Card('Ace', '♦'), Card('7', '♦'), Card('King', '♥'), Card('9', '♦'), Card('King', '♠')]))]))
    mau_mau.concepts    25  next_turn        : -------------------- turn 1 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('Jack', '♣')
    mau_mau.concepts    27  next_turn        : Player('Eric', Hand([Card('Queen', '♠'), Card('10', '♠'), Card('Queen', '♣'), Card('8', '♦'), Card('7', '♠')])) is up
    mau_mau.strategy    17  play             : encountered rule DemandWantedSuit on Card('Jack', '♣')
    mau_mau.strategy    56  _play            : find card to play
    mau_mau.subjects    103 put              : play Card('Queen', '♣')
    mau_mau.concepts    25  next_turn        : -------------------- turn 2 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('Queen', '♣')
    mau_mau.concepts    27  next_turn        : Player('John', Hand([Card('9', '♠'), Card('Ace', '♠'), Card('10', '♦'), Card('Ace', '♣'), Card('8', '♥')])) is up
    mau_mau.strategy    17  play             : encountered rule BasicRule on Card('Queen', '♣')
    mau_mau.strategy    56  _play            : find card to play
    mau_mau.subjects    103 put              : play Card('Ace', '♣')
    [---- SNIP ----]
    mau_mau.concepts    25  next_turn        : -------------------- turn 22 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('8', '♥')
    mau_mau.concepts    27  next_turn        : Player('Eric', Hand([Card('10', '♣'), Card('10', '♥')])) is up
    mau_mau.strategy    17  play             : encountered rule SkipNextPlayer on Card('8', '♥')
    mau_mau.strategy    56  _play            : find card to play
    mau_mau.subjects    103 put              : play Card('10', '♥')
    mau_mau.concepts    25  next_turn        : -------------------- turn 23 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('10', '♥')
    mau_mau.concepts    27  next_turn        : Player('John', Hand([Card('Ace', '♥'), Card('King', '♦'), Card('7', '♥')])) is up
    mau_mau.strategy    17  play             : encountered rule BasicRule on Card('10', '♥')
    mau_mau.strategy    56  _play            : find card to play
    mau_mau.subjects    103 put              : play Card('Ace', '♥')
    mau_mau.concepts    25  next_turn        : -------------------- turn 24 --------------------
    mau_mau.concepts    26  next_turn        : upcard: Card('Ace', '♥')
    mau_mau.concepts    27  next_turn        : Player('human', Hand([Card('King', '♥')])) is up
    mau_mau.strategy    17  play             : encountered rule BasicRule on Card('Ace', '♥')
    mau_mau.strategy    56  _play            : find card to play
    choose card to play.
    1 -> Card('King', '♥') | 1
    mau_mau.subjects    103 put              : play Card('King', '♥')
    root                27  play_interactive_game: And the winner is human

## [`stats.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/stats.py)

Contains some functions to run the game simulations and collect statistics. 

    $ mau-mau mean_turns

output like:

    root                42  main             : mean_turns() ...
    mau_mau.stats       35  _simulate_games  : players: 3; 1000 reps
    mau_mau.stats       12  mean_turns       : mean turns played: 34.097

input:

    $ mau-mau winner_distribution

output like:

    root                52  main             : winner_distribution() ...
    mau_mau.stats       35  _simulate_games  : players: ('Eric', 'Terry', 'John'); 1000 reps
    mau_mau.stats       21  winner_distribution: winner distribution: {'Eric': 345, 'Terry': 327, 'John': 328}

input:

    $ mau-mau time_durations

output like:

    root                52  main             : time_durations() ...
    mau_mau.stats       31  time_durations   : it takes 0.643 seconds to play 1000 games
