# Tic Tac Toe IA game

Game of the tic tac toe with an IA to play with. This code was made just for fun and to give a start point for future implementations of search tree algorithms. The game has a graphic interface and a terminal one, both can be played with different board sizes (3x3,4x4..).

The code is done in Python 3.7 and the actual IA implemented is Monte Carlo Tree Search a heuristic algorithm use in Alpha go.

## Play game
  -Terminal interface:
  * size: board size.
  * trains_steps: train steps in each iteration (MCTS).
  ```python
  python main_terminal.py size trains_steps
  ```
  -Graphic interface:
  * size: board size.
  * trains_steps: train steps in each iteration (MCTS).
  * height: height of the interface.
  * width: witdth of the interface.
  ```python
  python main size train_steps height width
```

## Game types
  Types of games that can be play.
  1. Player vs Player
  2. Player vs IA
  3. IA vs Player

## Code structure

![Graph](https://github.com/ipmach/TicTacToe_IA/blob/master/Documentation/graph.png)

## Dependecies
  Dependecies need it to run the code.
  * [Numpy](https://numpy.org/)
  ```python
  pip install numpy
  ```
  * [PyGame](https://www.pygame.org)
  ```python
  pip install pygame
  ```
## Implemented IAs
  -MCTS: Monte Carlo Tree Search
  
## External code
  The code use from other users of GiHub with some modifications.
  * [Monte Carlo Tree Search](https://github.com/int8/monte-carlo-tree-search/blob/master/mctspy/games/examples/tictactoe.py) from int8.
  * [Graphic interface](https://github.com/nyergler/teaching-python-with-pygame/blob/master/ttt-tutorial/tictactoe.py) from nyergler.
