from abc import ABC, abstractmethod
from collections import defaultdict
import mvc
from Agent import agent
from abc import ABC, abstractmethod
import numpy as np

class Heuristic(agent):
    "Heuristic agent, doesn't look the long game he just care about the next two moves"

    agent_name = "Heuristic"
    agent_description = "This agent was design to be a simple player. He only look if he is gonna" + \
    "win next turn or if he is gonna lose, if none of this two cases is apply then the agent play randomly."

    def do_rollout(self,board):
        """
        Don't need to train in each iteration
        """
        return None

    def train_model(self, total_games, learning_rate =0.9, loadPre = True):
        """
        Don't need to train in the beggining
        """
        return None

    def choose(self,board):
        """
        Choose the board to play
        """
        children_board = []
        list_children =board.find_children()
        player = board.turn
        #Check if I can win the next move
        for i in list_children:
            if mvc._find_winner(i.tup,i.size) == player:
                return i
        ideas = []
        #Check to avoid lose in two moves
        for i in list_children:
            list_children_2 = i.find_children()
            choose = True
            for j in list_children_2:
                if mvc._find_winner(j.tup,j.size) == (not player):
                    choose = False
            if choose:
                ideas.append(i)
        if len(ideas) > 0: #Choose a random play that dont make me lose in two moves
            return ideas[np.random.choice(np.arange(len(ideas)))]
        else: #Choose an random play already knowing I am gonna lose
            list_children = list(list_children)
            return list_children[np.random.choice(np.arange(len(list_children)))]
