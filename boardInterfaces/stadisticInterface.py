import pygame
import numpy as np
from pygame.locals import *
from game_nodes import Model
import mvc
import time
import player
from matplotlib import pyplot as plt
import pandas as pd
import copy
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Command, NoEscape, TextBlock,Center
from pylatex.utils import italic,bold
import datetime


def gameStadistic(size,train_steps, turnPlayer,agent, agent2,train = 0 ,save_games = False,visualize = True):
    total_games = 1
    if train == 0:
        print("How many games:")
        while(True):
            try:
                total_games = input("Select number: ")
                total_games = int(total_games)
                assert total_games > 0, "Number must be positive."
                break
            except:
                print("You must choose a number")
    player1 = [0]
    player2 = [0]
    replay = []
    for j in range(total_games):
        round = 0
        model = Model(tup=(None,) * size**2, turn=True, winner=None,size = size ,terminal=False)
        if train == 0:
            print("Playing",j,"of",total_games)
        game = []
        while(True):
            #Check if a player won or tie
            if mvc._find_winner(model.tup,size) == True:
                player1.append(player1[-1] + 1)
                player2.append(player2[-1])
                break
            elif mvc._find_winner(model.tup,size) == False:
                player1.append(player1[-1])
                player2.append(player2[-1] +1)
                break
            elif mvc._isTie(size,round):
                player1.append(player1[-1])
                player2.append(player2[-1])
                break
            #Playing the game
            if turnPlayer.playerTurn() == player.typePlayer.IA_PLAYER:
                for _ in range(train_steps):
                    agent.do_rollout(model)
                model = agent.choose(model)
            elif turnPlayer.playerTurn() == player.typePlayer.IA_PLAYER_2:
                for _ in range(train_steps):
                    agent2.do_rollout(model)
                model = agent2.choose(model)
            round +=1
            if save_games:
                game.append(copy.copy(model))
            turnPlayer.newTurn()
        turnPlayer.reset()
        replay.append(game.copy())
    gamesPlayed = np.arange(total_games+1)

    #Create Report
    doc = Document('basic')
    doc.preamble.append(Command('title', 'Game report'))
    doc.preamble.append(Command('author', 'Tic Tac Toe'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    with doc.create(Section('Introducction')):
            doc.append(bold('This document was autogenerate. '))
            doc.append('Here we present the result between two agents after ' + str(total_games) + 'games.')
            doc.append(' This document present graphs with the victories of the agents and the total points obtain.')
            doc.append(' The agent 1 is ' + agent.agent_name + ' and the agent 2 is ' + agent2.agent_name + '. ')
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            doc.append(bold('Document generate ' + date  + '.'))

    with doc.create(Section('Agent 1: ' + agent.agent_name)):
            doc.append(NoEscape(agent.agent_description))
    with doc.create(Section('Agent 2: ' + agent2.agent_name)):
            doc.append(NoEscape(agent2.agent_description))
    with doc.create(Section('Victories count')):
        doc.append('In this secction we can see the plot with the point counts of each agent.')
        with doc.create(Figure(position='htbp')) as plot:
            df = pd.DataFrame({
                "Games Played": gamesPlayed,
                "Player 1: "+ turnPlayer.PLAYER1: player1,
                "Player 2: "+ turnPlayer.PLAYER2: player2
            })
            ax = df.plot.area(x="Games Played",stacked=False)
            plot.add_plot()
            plot.add_caption('Points per agent.')
            #plt.close()
    if visualize:
        plt.show()

    doc.generate_pdf('Reports/game_report', clean_tex=True)


    if save_games:
        return replay
