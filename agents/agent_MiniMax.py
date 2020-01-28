from abc import ABC, abstractmethod
from collections import defaultdict
import mvc
from Agent import agent
from abc import ABC, abstractmethod
import numpy as np

class MiniMax(agent):

        def __init__(self,depth):
            self.depth = depth

        def _maxmin(self,old_value, new_value):
            if new_value == -1 or old_value == -1:
                return -1
            return max(old_value,new_value)

        def _search(self,board,player,n):
            a=  mvc.converv(board.tup)
            if n == self.depth:
                return 0
            if np.where(a==2)[0].shape[0] == 0:
                return 0
            if mvc._find_winner(board.tup,board.size) == player:
                return 1
            if mvc._find_winner(board.tup,board.size) == (not player):
                return -1
            list_children =board.find_children()
            value = 0
            for i in list_children:
                new_value = self._search(i,player,n+1)
                value = self._maxmin(value, new_value)
                if value == -1:
                    return -1
            return value

        def do_rollout(self,board):
            """
            Don't need to train in each iteration
            """
            return None

        def choose(self,board):
            children_value = []
            children_board = []
            list_children =board.find_children()
            player = board.turn
            for i in list_children:
                children_value.append(self._search(i,player,0))
                children_board.append(i)
            aux = np.argmax(children_value)
            return children_board[aux]

"""
agent = MiniMax(6)
model = Model(tup=(False,False,None,None,None,None,None,None,None), turn=True, winner=None,size = 3 ,terminal=False)

model2 = agent.choose(model)

print(model2.tup)
"""
