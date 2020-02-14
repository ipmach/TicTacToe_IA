# Tic Tac Toe IA game

Game of the tic tac toe with different IAs to play with. This code was made just for fun and to give a start point for future implementations of new algorithms. The game has a graphic interface, a terminal one and a statistic one, they can be played with different board sizes (3x3,4x4..).

The code is done in Python 3.7 and the actual IAs implemented are Monte Carlo Tree Search a heuristic algorithm use in Alpha go, Q-Learning an reinforcement learning algorithm, Minimax, and a simple heuristic algorithm.


[![video](https://youtu.be/cNNNZ7tfg1o)
### (Click in the image to watch the video)



## Play game
  -Terminal interface:
  * size: board size.
  * trains_steps: train steps in each iteration (MCTS).

  -Stadistic interace:
  * Plot the score after x games between two agents.

  -Graphic interface:
  * size: board size.
  * trains_steps: train steps in each iteration (MCTS).
  * height: height of the interface.
  * width: width of the interface.
  ```python
  python main.py size
```

  To get a report of a qtable already train.
  ```python
  python check_qtable.py size
```

## Game types
  Types of games that can be play.
  1. Player vs Player
  2. Player vs IA
  3. IA vs Player
  4. IA vs IA
  5. IA vs IA stadistics

## Code structure

![Graph](https://github.com/ipmach/TicTacToe_IA/blob/master/Documentation/graph.png)

## Implemented IAs
  -[MCTS](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search): Monte Carlo Tree Search. <br />
  -[MM](https://en.wikipedia.org/wiki/Minimax): MiniMax, with "alpha beta optimization". <br />
  -[Q-Learning](https://en.wikipedia.org/wiki/Q-learning): Reinforcement learning control. <br />
  -Heuristic

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

  * [Matplotlib](https://matplotlib.org/)
  ```python
  pip install matplotlib
  ```

  * [Pandas](https://pandas.pydata.org/)
  ```python
  pip install pandas
  ```

  * [tqdm](https://github.com/tqdm/tqdm)
  ```python
  pip install tqdm
  ```

  * [PyLatex](https://jeltef.github.io/PyLaTeX/current/index.html)
  ```python
  pip install pylatex
  ```

## External code
  The code use from other users of GiHub with some modifications.
  * [Monte Carlo Tree Search](https://github.com/int8/monte-carlo-tree-search/blob/master/mctspy/games/examples/tictactoe.py) from int8.
  * [Graphic interface](https://github.com/nyergler/teaching-python-with-pygame/blob/master/ttt-tutorial/tictactoe.py) from nyergler.
