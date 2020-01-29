from abc import ABC, abstractmethod
from collections import defaultdict
import mvc
from Agent import agent
from abc import ABC, abstractmethod
import numpy as np

class MiniMax(agent):

        def __init__(self,depth):
            self.depth = depth

        def _maxmin(self,old_value, new_value,turn):
            """
            If turn is positive: max(old_value,new_value)
            If turn is negative: min(old_value,new_value)
            """
            if turn:
                return min(old_value,new_value)
            else:
                return max(old_value,new_value)

        def _search(self,board,player,n,turn):
            """
            Depth tree search of the minimax algorithm
            """
            a=  mvc.converv(board.tup)
            if n == self.depth: #End of the exploration
                return 0
            if np.where(a==2)[0].shape[0] == 0: #Tie
                return 0
            if mvc._find_winner(board.tup,board.size) == player: #Win
                return 1
            if mvc._find_winner(board.tup,board.size) == (not player): #Loss
                return -1
            list_children =board.find_children()
            value = 0
            for i in list_children:
                new_value = self._search(i,player,n+1, not turn)
                value = self._maxmin(value, new_value,turn)
            return value

        def do_rollout(self,board):
            """
            Don't need to train in each iteration
            """
            return None

        def choose(self,board):
            """
            Choose the board to play
            """
            children_value = []
            children_board = []
            list_children =board.find_children()
            player = board.turn
            for i in list_children:
                children_value.append(self._search(i,player,0,True))
                children_board.append(i)
            aux = np.argmax(children_value)
            return children_board[aux]
