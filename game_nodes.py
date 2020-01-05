import numpy as np
from Node import Node
import mvc
from collections import namedtuple
from random import choice

_TTTB = namedtuple("Model", "tup turn winner size terminal")


class Model(_TTTB,Node):

    def find_children(board):
        """
        Find all possible children.
        """
        if board.terminal:  # If the game is finished then no moves can be made
            return set()
        # Otherwise, you can make a move in each of the empty spots
        return {
            board.make_move(i) for i, value in enumerate(board.tup) if value is None
        }

    def find_random_child(board):
        """
        Find a random children.
        """
        if board.terminal:
            return None  # If the game is finished then no moves can be made
        empty_spots = [i for i, value in enumerate(board.tup) if value is None]
        return board.make_move(choice(empty_spots))

    def reward(board):
        """
        Give the reward of the actual board.
        """
        """
        if not board.terminal:
            raise RuntimeError(f"reward called on nonterminal board {board}")
        if board.winner is board.turn:
            # It's your turn and you've already won. Should be impossible.
            raise RuntimeError(f"reward called on unreachable board {board}")
        """
        if board.turn is (not board.winner):
            return 0  # Your opponent has just won. Bad.
        if board.winner is None:
            return 0.5  # Board is a tie
        # The winner is neither True, False, nor None
        raise RuntimeError(f"board has unknown winner type {board.winner}")

    def is_terminal(board):
        """
        Check if the board is terminal.
        """
        return board.terminal

    def make_move(board, index):
        """
        Make a move in the game
        """
        tup = board.tup[:index] + (board.turn,) + board.tup[index + 1 :]
        turn = not board.turn
        size = board.size
        winner = mvc._find_winner(tup,size)
        is_terminal = (winner is not None) or not any(v is None for v in tup)
        return Model(tup, turn, winner, size,is_terminal)
