# Usage

## Command line access

After installation you have an additional command in your virtualenv: `mau-mau`. The default behaviour if you call it without parameters is to simulate a simple game of Mau Mau between three computer players (and you can see the hands of all the players and every step of the game).


**FIXME** I use fire now ... adapt
* `mau-mau`: Play single game with high verbosity settings in the logger
* `mau-mau <stats.function>`: e.g. `mau-mau turns` - the argument will be passed to `get_function_from_name` that fetches a function object of the same name from [`stats.py`](https://github.com/obestwalter/mau-mau/blob/master/mau_mau/statistics.py) and executes it. This is a very simple way to create a flexible command line interface that does not need to be changed if you create more statistics functions in `statistics.py`. Adding a new function to `statistics.py` will automatically make it accessible through the command line interface.
* `mau-mau human` ... or any other argument that does not map to a function in stats: play a game against the computer.

## Run a simple simulation

        $ cd </path/to/your/clone>
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

## Collect statistics

    $ mau-mau turns

The output could be:

    mau_mau.stats       35  _simulate_games  : players: 3; 1000 reps
    mau_mau.stats       12  turns            : mean turns played: 34.097

Input:

    $ mau-mau winners

The output could be:

    mau_mau.stats       35  _simulate_games  : players: ('Eric', 'Terry', 'John'); 1000 reps
    mau_mau.stats       21  distribution     : winner distribution: {'Eric': 345, 'Terry': 327, 'John': 328}

Input:

    $ mau-mau durations

The output could be:

    mau_mau.stats       31  time_durations   : it takes 0.643 seconds to play 1000 games
