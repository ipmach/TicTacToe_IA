from game_nodes import  Model
import mvc
import sys
import numpy as np
import player


def gameTerminal(size,train_steps,turnPlayer,agent,agent2):
    round = 0
    board = Model(tup=(None,) * size**2, turn=True, winner=None,size = size ,terminal=False)
    mvc.view(board.tup,size,round)
    while(True): #Loop of the total game
        while(True): #Loop of a turn of a player
            if turnPlayer.playerTurn() == player.typePlayer.IA_PLAYER:#Agent turn
                for _ in range(train_steps):
                    agent.do_rollout(board)
                board = agent.choose(board)
                print("IA choose")
                mvc.view(board.tup,size,round)
                break
            if turnPlayer.playerTurn() == player.typePlayer.IA_PLAYER_2:#Agent turn
                for _ in range(train_steps):
                    agent2.do_rollout(board)
                board = agent2.choose(board)
                print("IA choose")
                mvc.view(board.tup,size,round)
                break
            else: #Player turn
                while(True): #Player choose play
                    try:
                        row_col = input("enter row,col: ")
                        row, col = map(int, row_col.split(","))
                        index = size * (row - 1) + (col - 1)
                        if not (mvc.correctNumber(size,col) and mvc.correctNumber(size,row)):
                            print("That position is out of the board")
                        elif np.array(board.tup)[index] != None:
                            print("That position is already taken.")
                        else:
                            break
                    except:
                        print("You must insert with this format row,col")
                try: #Game change the state
                    board = board.make_move(index)
                    mvc.view(board.tup,size,round)
                    break
                except Exception as e:
                    print(e)
        round +=1
        turnPlayer.newTurn()
        player_won = mvc._find_winner(board.tup,size)
        if player_won != None: #Game check if the player won
            print("Congratulations, player",player_won,"won")
            break
        if mvc._isTie(size,round): #Game check if there is tie
            print("Game finish in a tie")
            break
