# Unravel the code

With all this in mind, we can finally move on to look at the code.

This simulation of a simple card game is optimized for being readable, easy to grasp and to demonstrate a whole range of concepts. It is not a toy example, ~~but the nasty details that usually screw with our nice and simple design and make the code grow tentacles and other cruft is not (yet) part of the code~~ but it can still be read like a nice little completely non-linear story (hopefully). It came into live in a non-linear fashion and should also be read that way.

## [setup.py](setup.py): make installable

The code of the actual software lives in[mau_mau/](mau_mau/)

**NOTE:** Please replace `</path/to/your/clone>` with the actual path on your computer.

To develop or explore the code it is best if you install the [package as editable](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) into a virtualenv. This way all the paths are working correct for all use cases (e.g. running the tests) and the command line access `sim` is also installed.

Install the package as editable with:

        $ cd </path/to/your/clone>
        $ pip install --editable .
      
**NOTE:**The dot at the end of the command is **not a typo or a spot on your screen you can't wipe away**! It means: install the contents of the folder that I am currently in as an editable package.

output like:

    Obtaining file:///</path/to/your/clone>
    Installing collected packages: OOOMMM
      Running setup.py develop for OOOMMM
    Successfully installed OOOMMM

You now have an additional command in your virtualenv: `sim`.
        
        $ cd </path/to/your/clone>
        $ sim

output like:

    root                42  main             : play_simple_game() ...
    mau_mau.sim         38  invite_players   : invited players are: [Player('Player 1', None), Player('Player 2', None), Player('Player 3', None)]
    mau_mau.cardroom    92  deal_fresh_hand  : Player('Player 1', [Card('9', '♥'), Card('Jack', '♣'), Card('9', '♣'), Card('8', '♣'), Card('8', '♦')])
    mau_mau.cardroom    92  deal_fresh_hand  : Player('Player 2', [Card('8', '♥'), Card('Queen', '♠'), Card('King', '♠'), Card('10', '♥'), Card('Queen', '♥')])
    mau_mau.cardroom    92  deal_fresh_hand  : Player('Player 3', [Card('King', '♣'), Card('Ace', '♦'), Card('7', '♠'), Card('Ace', '♥'), Card('9', '♦')])
    mau_mau.sim         23  setup_game       : Start new game: Game(Table(MauMau(5), [Player('Player 1', [Card('9', '♥'), Card('Jack', '♣'), Card('9', '♣'), Card('8', '♣'), Card('8', '♦')]), Player('Player 2', [Card('8', '♥'), Card('Queen', '♠'), Card('King', '♠'), Card('10', '♥'), Card('Queen', '♥')]), Player('Player 3', [Card('King', '♣'), Card('Ace', '♦'), Card('7', '♠'), Card('Ace', '♥'), Card('9', '♦')])]))
    mau_mau.cardroom    29  next_turn        : ------------------------------------------------------------------------------------------
    mau_mau.cardroom    30  next_turn        : Player('Player 1', [Card('9', '♥'), Card('Jack', '♣'), Card('9', '♣'), Card('8', '♣'), Card('8', '♦')]) is up (turn 1)
    mau_mau.strategy    15  play             : encountered rule BasicRule on Card('Queen', '♣')
    mau_mau.strategy    53  _play            : find card to play
    mau_mau.cardroom    96  play_card        : play Card('Jack', '♣') on Card('Queen', '♣')
    mau_mau.cardroom    29  next_turn        : ------------------------------------------------------------------------------------------
    mau_mau.cardroom    30  next_turn        : Player('Player 2', [Card('8', '♥'), Card('Queen', '♠'), Card('King', '♠'), Card('10', '♥'), Card('Queen', '♥')]) is up (turn 2)
    mau_mau.strategy    15  play             : encountered rule DemandWantedSuit on Card('Jack', '♣')
    mau_mau.strategy    53  _play            : find card to play
    mau_mau.strategy    62  _play            : nothing to play
    mau_mau.cardroom    111 draw_from_stock  : Card('10', '♣')
    mau_mau.cardroom    29  next_turn        : ------------------------------------------------------------------------------------------

    [-...SNIPPING LOTS OF OUTPUT...]

    mau_mau.cardroom    30  next_turn        : Player('Player 3', [Card('7', '♠'), Card('9', '♦'), Card('Jack', '♦')]) is up (turn 30)
    mau_mau.strategy    15  play             : encountered rule BasicRule on Card('King', '♠')
    mau_mau.strategy    53  _play            : find card to play
    mau_mau.cardroom    96  play_card        : play Card('7', '♠') on Card('King', '♠')
    mau_mau.cardroom    29  next_turn        : ------------------------------------------------------------------------------------------
    mau_mau.cardroom    30  next_turn        : Player('Player 1', [Card('9', '♠'), Card('8', '♠'), Card('Jack', '♠'), Card('10', '♠'), Card('Ace', '♠'), Card('Ace', '♣'), Card('10', '♦'), Card('Jack', '♥'), Card('Queen', '♦')]) is up (turn 31)
    mau_mau.strategy    15  play             : encountered rule MakePlayerDrawTwoCards on Card('7', '♠')
    mau_mau.strategy    38  choose_antidote  : find antidote
    mau_mau.cardroom    111 draw_from_stock  : Card('King', '♥')
    mau_mau.cardroom    111 draw_from_stock  : Card('Jack', '♣')
    mau_mau.strategy    53  _play            : find card to play
    mau_mau.cardroom    96  play_card        : play Card('9', '♠') on Card('7', '♠')
    mau_mau.cardroom    29  next_turn        : ------------------------------------------------------------------------------------------
    mau_mau.cardroom    30  next_turn        : Player('Player 2', [Card('Queen', '♠')]) is up (turn 32)
    mau_mau.strategy    15  play             : encountered rule BasicRule on Card('9', '♠')
    mau_mau.strategy    53  _play            : find card to play
    mau_mau.cardroom    96  play_card        : play Card('Queen', '♠') on Card('9', '♠')
    root                20  play_simple_game : And the winner is Player 2

## [`cli.py`](mau_mau/cli.py): command line access

This contains the code for the commandline interface. Its function `main` is configured in `setup.py` to act like a program called `sim` that is accessible where the package is installed. At the moment the following can be accessed from the commandline:

* `sim`: If you do not pass anything a single game will be played with high verbosity settings in the logger
* `sim <stats.function>`: e.g. `sim mean_turns` - the argument will be passed to `get_function_from_name` that fetches a function object of the same name from [`stats.py`](mau_mau/stats.py) and executes it. This is a very simple way to create a flexible command line interface that does not need to be changed if you create more statistics functions in `stats.py`. Adding a new function to `stats.py` will automatically make it accessible through the command line interface.
* `sim interactive` ... or any other argument that does not map to a function in stats: play a game against the computer

See the different sections for more examples of commandline usage.

## [`sim.py`](mau_mau/sim.py): the 'story'

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

## config.py

FIXME modify according to new structure

## subjects.py

FIXME modify according to new structure

## concepts.py

FIXME modify according to new structure

## objects.py

I know .. in Python everything is an object, so this would be meaningless.
In the context of the
program but they are objects in the level of abstractio we care about, when
crating the software, which is: they are objects of the game which are
manipulated by the subjects of the game.

## [`cardroom.py`](mau_mau/cardroom.py)

To dig deeper and get a more detailed understanding of the program, you should start to explore the classes, their attributes and behaviour and how they interact. The best place to start is the cardroom.

This looks pretty different from `sim.py` and it is. Here is where the OO part of the story kicks in. If `sim.py` contains the plot, `cardroom.py` contains the descriptions of the actors and props of the story. It describes the relevant part of the virtual universe that is created to run the simulation. It contains custom data structures (a.k.a. classes) to model the problem of simulating Mau Mau. You should be able to read through the classes and get an idea of what elements are needed to simulate a card game and how they might interact. The order in which the classes are defined are from compounded to simple.

## [`rules.py`](mau_mau/rules.py)

This contains the classes that implement the rules of Mau Mau. Start reading with the `MauMau` class and see if you can figure out how it works. There is always one rule active on the table that is valid for the currently played round. Sometimes information gets transferred from one rule to the next (e.g. if a 7 was put on a seven, the number of draws have to accumulate). 

## [`strategy.py`](mau_mau/strategy.py)

**Note:** A player has a strategy, but the player also attaches it to the active rule, so that it can be queried for the wanted suit if a Jack is on the table.

### `BasicStrategy` 

just plays according to the rules and always chooses random antidotes and cards. If playing a Jack it always asks for the suit it has the most of. 

This can be extended upon to implement "real" strategies.

### `HumanStrategy`
 
Mainly to show that the existing design makes it very easy to even add interactivity to let a human play against a computer.

Play interactive game:

    $ sim interactive
 
output like:

    root                52  main             : play_interactive_game() ...
    mau_mau.sim         44  invite_players   : invited players are: [Player('Eric', None), Player('John', None), Player('human', None)]
    mau_mau.cardroom    83  deal_fresh_hand  : Player('Eric', [Card('King', '♦'), Card('Queen', '♠'), Card('9', '♣'), Card('7', '♥'), Card('Ace', '♠')])
    mau_mau.cardroom    83  deal_fresh_hand  : Player('John', [Card('Queen', '♦'), Card('Ace', '♦'), Card('8', '♦'), Card('7', '♦'), Card('9', '♥')])
    mau_mau.cardroom    83  deal_fresh_hand  : Player('human', [Card('8', '♥'), Card('10', '♥'), Card('King', '♥'), Card('7', '♠'), Card('8', '♠')])
    [...]
    mau_mau.cardroom    24  next_turn        : upcard: Card('Ace', '♠')
    mau_mau.cardroom    25  next_turn        : Player('human', [Card('8', '♥'), Card('10', '♥'), Card('King', '♥'), Card('7', '♠'), Card('8', '♠'), Card('King', '♠'), Card('Ace', '♥')]) is up
    mau_mau.strategy    16  play             : encountered rule BasicRule on Card('Ace', '♠')
    mau_mau.strategy    55  _play            : find card to play
    choose card to play.
    1 -> Card('7', '♠') | 2 -> Card('8', '♠') | 3 -> Card('King', '♠') | 4 -> Card('Ace', '♥') | 1
    mau_mau.cardroom    87  play_card        : play Card('7', '♠')
    mau_mau.cardroom    23  next_turn        : --------------------------------------------- turn: 10 ---------------------------------------------
    mau_mau.cardroom    24  next_turn        : upcard: Card('7', '♠')
    mau_mau.cardroom    25  next_turn        : Player('Eric', [Card('9', '♣'), Card('7', '♥')]) is up
    mau_mau.strategy    16  play             : encountered rule MakePlayerDrawTwoCards on Card('7', '♠')
    mau_mau.strategy    39  choose_antidote  : find antidote
    mau_mau.strategy    43  choose_antidote  : found antidote Card('7', '♥')
    mau_mau.cardroom    87  play_card        : play Card('7', '♥')
    [...]
    mau_mau.cardroom    23  next_turn        : --------------------------------------------- turn: 18 ---------------------------------------------
    mau_mau.cardroom    24  next_turn        : upcard: Card('Ace', '♥')
    mau_mau.cardroom    25  next_turn        : Player('human', [Card('8', '♥'), Card('10', '♥'), Card('King', '♥'), Card('8', '♠'), Card('King', '♠'), Card('King', '♣'), Card('Jack', '♥'), Card('Jack', '♠'), Card('9', '♠'), Card('Queen', '♣')]) is up
    mau_mau.strategy    16  play             : encountered rule BasicRule on Card('Ace', '♥')
    mau_mau.strategy    55  _play            : find card to play
    choose card to play.
    1 -> Card('8', '♥') | 2 -> Card('10', '♥') | 3 -> Card('King', '♥') | 4 -> Card('Jack', '♥') | 4
    mau_mau.cardroom    87  play_card        : play Card('Jack', '♥')
    mau_mau.cardroom    23  next_turn        : --------------------------------------------- turn: 19 ---------------------------------------------
    mau_mau.cardroom    24  next_turn        : upcard: Card('Jack', '♥')
    mau_mau.cardroom    25  next_turn        : Player('Eric', [Card('Jack', '♣'), Card('8', '♣'), Card('9', '♦')]) is up
    mau_mau.strategy    16  play             : encountered rule DemandWantedSuit on Card('Jack', '♥')
    choose wanted suit.
    1 -> ♦ | 2 -> ♥ | 3 -> ♠ | 4 -> ♣ | 4
    mau_mau.strategy    55  _play            : find card to play
    mau_mau.cardroom    87  play_card        : play Card('8', '♣')
    [...]


## [`stats.py`](mau_mau/stats.py)

Contains some functions to run the game simulations and collect statistics. 

    $ sim mean_turns

output like:

    root                42  main             : mean_turns() ...
    mau_mau.stats       35  _simulate_games  : players: 3; 1000 reps
    mau_mau.stats       12  mean_turns       : mean turns played: 34.097

input:

    $ sim winner_distribution

output like:

    root                52  main             : winner_distribution() ...
    mau_mau.stats       35  _simulate_games  : players: ('Eric', 'Terry', 'John'); 1000 reps
    mau_mau.stats       21  winner_distribution: winner distribution: {'Eric': 345, 'Terry': 327, 'John': 328}

input:

    $ sim time_durations

output like:

    root                52  main             : time_durations() ...
    mau_mau.stats       31  time_durations   : it takes 0.643 seconds to play 1000 games