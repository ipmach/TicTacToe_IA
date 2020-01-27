import numpy as np
from game_nodes import Model
import mvc
from Agent import agent


class HMM(agent):

    def __init__(self, exploration_weight=1,size = 3):
        self.size =size
        self.w =exploration_weight #size of the exploration for the winning probability

    def b(self,tup):
        """
        Observation posibility
        """
        array = mvc.converv(np.array(tup))
        NoneP = 0
        for i in array:
            if i ==2:
                NoneP +=1
        return NoneP/array.shape[0]

    def _simulate(self,n,N,board,i, IAturn):
        """
        Calculate the probability p(On = win,On-1 = None, ..., O0 = None, Qn = ...)
        """
        if n == 0: #first move
            return self.b(board.tup) *self._simulate(n+1,N,board,i, IAturn)
        elif n==N: #Final move
            return 0.1
        else: #Rest of moves
            aux = 0
            for j in board.find_children():
                p = self.b(j.tup)
                if j.winner == IAturn:
                    aux +=1
                else:
                    aux += p*board.reward()*self._simulate(n+1,N,j,i, IAturn)
            return aux

    def do_rollout(self,board):
        """
        Don't need to train in each iteration
        """
        return None

    def choose(self,board):
        """
        Choose the option with highest probability of winning
        """
        children = {}
        list_children =board.find_children()
        for i in list_children:
            if i.winner == board.turn: #already win
                children[100] = i
            elif i.winner == i.turn: #Shold not be possible, he play and imediatly lose
                children[0] = i
            else: #Calculate the probabilities of winning
                index = mvc._find_new(board.tup,i.tup,self.size, inIndex = True)
                children[self._simulate(0,self.w,i,index,not i.turn)] = i
        return children[max(children.keys())]

    #print(choose(board))
