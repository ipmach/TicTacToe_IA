import pygame
import numpy as np
from pygame.locals import *
from game_nodes import Model
import mvc
import time
import player
from matplotlib import pyplot as plt

def gameStadistic(size,train_steps, turnPlayer,agent, agent2):
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
    for j in range(total_games):
        round = 0
        model = Model(tup=(None,) * size**2, turn=True, winner=None,size = size ,terminal=False)
        print("Playing",j,"of",total_games)
        while(True):
            #Check if a player won or tie
            if mvc._find_winner(model.tup,size) == True:
                player1.append(player1[-1] + 1)
                player2.append(player2[-1] -1)
                break
            elif mvc._find_winner(model.tup,size) == False:
                player1.append(player1[-1] -1)
                player2.append(player2[-1] +1)
                break
            elif mvc._isTie(size,round):
                player1.append(player1[-1] +0)
                player2.append(player2[-1] +0)
                break
            #Playing the game
            if turnPlayer.playerTurn() == player.typePlayer.IA_PLAYER:
                for _ in range(train_steps):
                    agent.do_rollout(model)
                model = agent.choose(model)
            elif turnPlayer.playerTurn() == player.typePlayer.IA_PLAYER_2:
                for _ in range(train_steps):
                    agent.do_rollout(model)
                model = agent2.choose(model)
            round +=1
            turnPlayer.newTurn()
        turnPlayer.reset()
    gamesPlayed = np.arange(total_games+1)
    #Ploting results
    fig = plt.figure("Games")
    fig.suptitle('Games played', fontsize=20)
    plt.xlabel('Games', fontsize=14)
    plt.ylabel('Score', fontsize=14)
    plt.plot(gamesPlayed,player1,'-',label = "Player 1")
    plt.plot(gamesPlayed,player2,'-',label = "Player 2")
    plt.legend()
    plt.show()
