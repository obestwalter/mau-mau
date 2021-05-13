# Usage

## Command line access

After installation you have two additional commands in your virtualenv: `mau-mau` and `mau-mau-stats`. The cli (command line interface) is automatically generated with a fun little library called [python-fire](https://github.com/google/python-fire). The default behaviour for our `mau-mau` is to show the usage info with the available commands:
 
### Play or simulate a single game
 
$ mau-mau

    Type:        Cli
    String form: <mau_mau.play.cli.<locals>.Cli object at 0x7f7fa3b3e5c0>
    
    Usage:       mau-mau 
                 mau-mau play
                 mau-mau sim
 
 You can then ask for specific help for commands (note the `--` to separate the command from the fire arg `--help`), e.g:
 
    $ mau-mau play -- --help
    
    Type:        method
    String form: <bound method cli.<locals>.Cli.play of <mau_mau.play.cli.<locals>.Cli object at 0x7f92d2c46e80>>
    File:        /home/ob/do/mau-mau/src/mau_mau/play.py
    Line:        42
    Docstring:   Play a game against two computer players.
    
    If one of the players' names is 'human' it will be interactive.
    
    Usage:       mau-mau play [PLAYERS]
                 mau-mau play [--players PLAYERS]

You can start a game that you play against two computer players by calling `mau-mau play --players John,Terry,human`
 
The fire library accomplishes this using introspection of the code to generate arguments and documentation. A more standard approach would be [argparse](https://docs.python.org/3/library/argparse.html) which is provided in the standard library already.

### Simulate a game

    $ mau-mau sim

The output could be:

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

## Play against the computer

Play interactive game (and know and see everything ...):

    $ mau-mau play

The output could be:

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
