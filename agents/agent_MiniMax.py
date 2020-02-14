from abc import ABC, abstractmethod
from collections import defaultdict
import mvc
from Agent import agent
from abc import ABC, abstractmethod
import numpy as np

class MiniMax(agent):
        "MiniMax tree searcher, with alpha beta pruning optimization."

        agent_name = "MiniMax"

        def __init__(self,depth):
            self.depth = depth

        def train_model(self, total_games, learning_rate =0.9, loadPre = True):
            """
            Don't need to train in the beggining
            """
            return None

        def _maxmin(self,old_value, new_value,turn):
            """
            If turn is positive: max(old_value,new_value)
            If turn is negative: min(old_value,new_value)
            """
            if turn:
                return max(old_value,new_value)
            else:
                return min(old_value,new_value)

        def _search(self,board,player,n,turn,alpha):
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
                new_value = self._search(i,player,n+1, not turn, alpha)
                value = self._maxmin(value, new_value,turn)
                #Alpha beta pruning optimization
                if not turn and alpha < value: #Alpha
                    break
                if turn and alpha > value: #Beta
                    break
                alpha = value
                ########
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
            alpha = -2
            beta = 2
            for i in list_children:
                value = self._search(i,player,0,False,alpha)
                alpha = value
                children_value.append(value)
                children_board.append(i)
            aux = np.argmax(children_value)
            return children_board[aux]

"""
agent = MiniMax(4)
model = Model(tup=(False,False,None,None,None,None,None,None,True), turn=True, winner=None,size = 3 ,terminal=False)
print(agent.choose(model).tup)
model = Model(tup=(False,False,None,None,None,None,None,True,True), turn=True, winner=None,size = 3 ,terminal=False)
print(agent.choose(model).tup)
model = Model(tup=(False,False,None,True,None,None,None,None,True), turn=True, winner=None,size = 3 ,terminal=False)
print(agent.choose(model).tup)
model = Model(tup=(False,True,None,None,False,True,False,True,None), turn=True, winner=None,size = 3 ,terminal=False)
print(agent.choose(model).tup)
"""
