from abc import ABC, abstractmethod
import numpy as np
import math
import mvc
from Agent import agent
from abc import ABC, abstractmethod
from agents import agent_Heuristic, agent_MCTS
import player
from boardInterfaces import stadisticInterface
import random
from matplotlib import pyplot as plt
import pandas as pd
import tqdm
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Command, NoEscape, TextBlock,Center
from pylatex.utils import italic,bold
import datetime


class QLearning(agent):

    """
    Q learning agent to play tic tac toe.
    """

    agent_name = "Q Learning"

    def __init__(self,size = 3, onTraining = False, save= True,limit = None, step = None):
        #Qtable use
        self.qtable = np.zeros((3**(size**2), (size**2) ))
        self.size = size #Size of the game
        self.onTraining = onTraining #If this agent is use for training
        self.limit = limit #total of games to train
        self.step = step #If on Training is true then step is the game we are in
        self.greedy = [0] #Count the number of greedy moves made
        self.save = save #If we save the qtable in a file

    def _ternaryToDecimal(self,list_num):
        """
        Convert a list of ternary numbers to decimals.
        """
        aux = 0
        for i in range(len(list_num)):
            aux += list_num[i] * 3** i
        return aux

    def _insertQtalble(self,old_state,new_state, learning_rate, win):
        """
        Insert a qvalue in the qtable, calculate the qvalue with the old_state and new_state
        """
        discountFactor = 1
        if win:
            reward = 1
        else:
            reward = 0
        #Action made
        action = mvc._find_new(old_state.tup, new_state.tup, self.size, inIndex = True)
        #Actual state
        state = self._ternaryToDecimal(mvc.converv(old_state.tup))
        #New state
        new_state = self._ternaryToDecimal(mvc.converv(new_state.tup))
        #aux = reward + discountFactor*max(Q(s',a))
        aux = reward if win else reward + discountFactor * max(self.qtable[new_state])
        #Q(s,a) = Q(s,a) + learning_rate * (aux - Q(s,a))
        self.qtable[state][action] = self.qtable[state][action] + \
                                    learning_rate  * (aux - self.qtable[state][action])
        #print(self.qtable[state])

    def choose(self, board):
        """
        Choose the action to made.
        """
        epsilon = 0
        if self.onTraining: #if is in training epsilon is not zero
            epsilon = (-0.9/self.limit) *self.step +1
        if random.randrange(0, 100, 1) /100 <= 1 - epsilon: #Normal action
            state = self.qtable[self._ternaryToDecimal(mvc.converv(board.tup))].copy()
            children = board.find_children()
            while(True): #Choose a valid action
                action = np.argmax(state)
                new_board = board.make_move(action)
                if new_board in children:
                    return new_board
                state[action] = -20
        else: #Greedy action
            self.greedy.append(self.greedy[-1] +1)
            return board.find_random_child()
            #return agent_Heuristic.Heuristic().choose(board)

    def do_rollout(self, board):
        """
        Don't need to train in each iteration
        """
        return None

    def train_model(self, total_games, learning_rate =0.4):
        """
        Trainin the model
        """
        turnPlayer = player.players()
        turnPlayer.insertPlayer_1(player.typePlayer.IA_PLAYER, "Training")
        turnPlayer.insertPlayer_2(player.typePlayer.IA_PLAYER_2, "Training")
        limit = total_games/2
        tie = [0]
        p1 = [0]
        p2 = [0]
        for game in tqdm.tqdm(np.arange(total_games)):
            agent = QLearning(size = self.size, onTraining = True, limit = limit, step=game, save = False)
            agent2 = agent_MCTS.MCTS(exploration_weight = 150) #agent use to train model
            agent.qtable = self.qtable
            replay = stadisticInterface.gameStadistic(self.size, 500,turnPlayer,agent, agent2,train =1 ,save_games = True, visualize = False)[0]
            replay.reverse()
            assert replay[0].terminal,"Something went wrong"
            #To plot the stadistics
            if replay[0].winner == None:
                tie.append(tie[-1] + 1)
                p1.append(p1[-1])
                p2.append(p2[-1])
            elif replay[0].winner == True:
                p1.append(p1[-1] + 1)
                p2.append(p2[-1])
                tie.append(tie[-1])
            else:
                p2.append(p2[-1] + 1)
                tie.append(tie[-1])
                p1.append(p1[-1])
            #Update the q table
            for j in range(len(replay)-2):
                if replay[j].winner == None:
                    self._insertQtalble(replay[j],replay[j+1],learning_rate,False)
                elif replay[j].terminal:
                    self._insertQtalble(replay[j],replay[j+1],learning_rate,True)
                else:
                    self._insertQtalble(replay[j],replay[j+2],learning_rate,False)
            #self.qtable = agent.qtable
            self.greedy = self.greedy +agent.greedy
        #Save the qtable if we choose to save it
        if self.save:
            a = str(self.size)
            np.save("agents/QLearningSave/qtable_"+a+"x"+a+".npy",self.qtable)
        #Create a report of the training
        doc = Document('basic')
        doc.preamble.append(Command('title', 'QLearning training report'))
        doc.preamble.append(Command('author', 'Tic Tac Toe'))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(r'\maketitle'))

        with doc.create(Section('Introducction')):
                doc.append(bold('This document was autogenerate. '))
                doc.append('Here we present the train ouput of the qlearning agent.')
                doc.append(' This document present graphs with the victories of the agent and his rival and the total ' \
                + 'number of greedy moves done in all the training. ')
                date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                doc.append(bold('Document generate ' + date  + '.'))

        with doc.create(Section('Victories count')):
            doc.append('In this secction we can see the plot with the point counts of each agent.')
            with doc.create(Figure(position='htbp')) as plot:
                    df = pd.DataFrame({
                        "Games Played": np.arange(total_games+1),
                        "Tie " :tie,
                        "Victory player 1 ":p1,
                        "Victory player 2 ":p2
                    })
                    ax = df.plot.area(x="Games Played",stacked=False)
                    plot.add_plot()
                    plot.add_caption('Points per agent.')
                    plt.close()

        with doc.create(Section('Greedy count')):
            doc.append('In this secction we can see the plot with the greedy moves count of the training agent.')
            with doc.create(Figure(position='htbp')) as plot:
                    dg = pd.DataFrame({
                        "times": np.arange(len(self.greedy)),
                        "greedy " :self.greedy,
                    })
                    ax = dg.plot.area(x="times",stacked=False)
                    plot.add_plot()
                    plot.add_caption('Count greedy moves.')
                    plt.close()
        doc.generate_pdf('Reports/qLearning_train_report', clean_tex=True)


"""
agent = QLearning(size = 3)

model1 = Model(tup=(None,None,True,None,None,None,None,None,None), turn=True, winner=None,size = 3 ,terminal=False)
model2 = Model(tup=(None,True,True,None,None,None,None,None,None), turn=True, winner=None,size = 3 ,terminal=False)
model3 = Model(tup=(True,True,True,None,None,None,None,None,None), turn=True, winner=None,size = 3 ,terminal=False)
agent._insertQtalble(model2, model3,0.8,True)
agent._insertQtalble(model1, model2,0.8,False)
agent.choose(model1)
#agent.train_model(500)
print(agent.qtable[agent._ternaryToDecimal(mvc.converv(model2.tup))])
print(agent.qtable[agent._ternaryToDecimal(mvc.converv(model1.tup))])
"""
