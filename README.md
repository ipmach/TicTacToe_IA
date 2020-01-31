# Tic Tac Toe IA game

Game of the tic tac toe with an IA to play with. This code was made just for fun and to give a start point for future implementations of search tree algorithms. The game has a graphic interface and a terminal one, both can be played with different board sizes (3x3,4x4..).

The code is done in Python 3.7 and the actual IAs implemented are Monte Carlo Tree Search a heuristic algorithm use in Alpha go and a simple version of Hidden Markov Model.

[![video](https://img.youtube.com/vi/ngVd-QV7YvY/0.jpg)](https://www.youtube.com/watch?v=ngVd-QV7YvY)
### (Click in the image to watch the video)



## Play game
  -Terminal interface:
  * size: board size.
  * trains_steps: train steps in each iteration (MCTS).

  -Graphic interface:
  * size: board size.
  * trains_steps: train steps in each iteration (MCTS).
  * height: height of the interface.
  * width: width of the interface.
  ```python
  python main.py size train_steps height width
```

## Game types
  Types of games that can be play.
  1. Player vs Player
  2. Player vs IA
  3. IA vs Player
  4. IA vs IA

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
  -[MCTS](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search): Monte Carlo Tree Search. <br />
  -[MM](https://en.wikipedia.org/wiki/Minimax): MiniMax, with "alpha beta optimization" <br />
  -Heuristic

## External code
  The code use from other users of GiHub with some modifications.
  * [Monte Carlo Tree Search](https://github.com/int8/monte-carlo-tree-search/blob/master/mctspy/games/examples/tictactoe.py) from int8.
  * [Graphic interface](https://github.com/nyergler/teaching-python-with-pygame/blob/master/ttt-tutorial/tictactoe.py) from nyergler.
