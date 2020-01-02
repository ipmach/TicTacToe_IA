# Tic Tac Toe IA game

Game of the tic tac toe with an IA to play with.  This code was made just for fun an to give a start point for future implementations of search trees algorithms.
The game have a graphic interface and a terminal one, both can be play with different boards sizes (3x3,4x4..). 

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
