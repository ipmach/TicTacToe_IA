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

def gameStadistic(size,train_steps, turnPlayer,agent, agent2, save_games = False,visualize = True):
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

    if visualize:
        df = pd.DataFrame({
            "Games Played": gamesPlayed,
            "Player 1: "+ turnPlayer.PLAYER1: player1,
            "Player 2: "+ turnPlayer.PLAYER2: player2
        })
        ax = df.plot.area(x="Games Played",stacked=False)
        plt.show()

    if save_games:
        return replay
