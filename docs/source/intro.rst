`Mau Mau <https://github.com/obestwalter/mau-mau>`__
====================================================

    Play is the highest form of research

    -- `Probably not Albert
    Einstein <http://quoteinvestigator.com/2014/08/21/play-research/>`__

Features of this implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Complete rules of Mau Mau
-  two different strategies:

   -  simple random strategy for a computer player
   -  strategy that adds interactivity so a human can play against the
      computer

-  Functions to run multiple games and collect stats
-  Flexible `command line interface <mau_mau/cli.py>`__ (add new
   functions without adjusting code)
-  `automatic tests <tests/>`__ with py.test, tox and Travis CI
-  Logging with the stdlib `logging
   module <https://docs.python.org/3/library/logging.html>`__
-  Use of `Python magic methods <https://docs.python.org/2/reference/datamodel
   .html#special-method-names>`__ to make our classes behave like inbuilt data types

Implementation
~~~~~~~~~~~~~~

The modelling problem we have here is a good fit to create your own data
structures (which classes are), so we will model the game flow using
`custom Python
classes <https://docs.python.org/3/tutorial/classes.html#classes>`__ and
see where we get.

The basic rules of Mau Mau
^^^^^^^^^^^^^^^^^^^^^^^^^^

    The game is played with a regular deck of playing cards. The players
    are dealt each a hand of cards (usually 5). The rest are placed face
    down as the drawing stack. At the beginning of the game the topmost
    card is revealed, then the players each get a turn to play cards.

    One can play a card if it corresponds to the suit or value of the
    open card. E.g. on a 10 of spades, only other spades can be played
    or other 10s. If a player is not able to, they draw one card from
    the stack. If he can play this card, he may do so, otherwise he
    keeps the drawn card and passes his turn. If the drawing stack is
    empty, the playing stack (except for the topmost card) is shuffled
    and turned over to serve as new drawing stack.

    -- `Wikipedia - Mau Mau <https://goo.gl/r7D63W>`__

Special rules
'''''''''''''

We add the three most common additional rules:

-  If an eight is played the next player is skipped
-  If a seven is played, the next player has to draw two cards. The next
   player can put another seven down and instead the following player
   will have to draw four cards (and so on).
-  A Jack can can be put on anything and the player who played it can
   ask for a different suite to be played

High level view
^^^^^^^^^^^^^^^

One koan in the `Zen of
Python <https://www.python.org/dev/peps/pep-0020/>`__ says: "If the
implementation is easy to explain, it may be a good idea". Let's put
this to the test and explain the implementation of our Mau Mau program
by simply describing the conditions and rules of the game using a rough
approximation of the programs' terminology and see if the objects and
their interactions make the implementation look obvious. Objects used in
the program are marked ``like this``, functions that describe
(inter)actions are marked like **this**). The game can also be described
in two phases, we could call "setup" and "play". The image shows all the
important elements of the simulation.

.. figure:: _static/cardroom.png
:alt: cardroom overview

   cardroom overview

**setup:** The ``players`` in the ``cardroom`` are **invited** to a
``game`` at the ``table``. A ``deck`` of ``cards`` is **shuffled**. The
same amount of cards is **dealt** to the ``players`` to form their
``hand``. One ``card`` - the ``upcard`` - is **drawn** from the
``stock`` and placed face up on the ``table``. The remaining cards are
``piled`` face down on the ``table`` and form the ``stock``. Now all is
in place to **play** the ``game``.

**play:** The ``players`` play in ``turns``. They choose a\ ``card``
that is **playable** with the ``upcard`` according to the rules (same
``suit`` or same ``value`` and `special rules <#special-rules>`__ and
place it on the ``table``. The played ``card`` ist the new ``upcard``
and the old ``upcard`` is now part of the ``waste``. Now the next
``player`` is up. If a player can't find a ``card`` to play, they have
to draw one from the ``stock`` and the next ``player`` is up. If the
``stock`` ``is empty``, the ``waste`` ``cards`` will be **shuffled** to
form the new ``stock``. The game is over and the ``winner`` is found as
soon as one ``player`` plays the last card of their ``hand``.

Easy enough to explain. This description of the rules and the gameplay
can double already as a high level explanation of the implementation. It
can also be read as an abstract story about a game, where the concrete
story would be the description of an actual game. The program code can
be viewed as story shape or abstract plot, with different executions of
it as concrete stories. If you have no idea what I mean just watch `Kurt
Vonneguts short talk about the shape of
stories <https://www.youtube.com/watch?v=oP3c1h8v2ZQ>`__ and transfer
your insights into thinking about abstract program code and its concrete
execution :)
