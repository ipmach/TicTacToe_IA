from abc import ABC, abstractmethod
from collections import defaultdict
import mvc
from Agent import agent
from abc import ABC, abstractmethod
import numpy as np

class Heuristic(agent):

    def do_rollout(self,board):
        """
        Don't need to train in each iteration
        """
        return None

    def choose(self,board):
        """
        Choose the board to play
        """
        children_board = []
        list_children =board.find_children()
        player = board.turn
        for i in list_children:
            if mvc._find_winner(i.tup,i.size) == player:
                return i
        ideas = []
        for i in list_children:
            list_children_2 = i.find_children()
            choose = True
            for j in list_children_2:
                if mvc._find_winner(j.tup,j.size) == (not player):
                    choose = False
            if choose:
                ideas.append(i)
        if len(ideas) > 0:
            return ideas[np.random.choice(np.arange(len(ideas)))]
        else:
            list_children = list(list_children)
            return list_children[np.random.choice(np.arange(len(list_children)))]
