from game_nodes import  Model
import mvc
from agent import MCTS
import sys
import numpy as np

def main():
    try:
        size = int(sys.argv[1])
        train_steps = int(sys.argv[2])
    except:
        raise RuntimeError("Error: must be 'python main size train_steps' with ints ")
    print("Welcome, choose game type:")
    print("1) Player vs Player")
    print("2) Player vs IA")
    print("3) IA vs Player")
    round = 0
    agent = MCTS(exploration_weight = 50)
    board = Model(tup=(None,) * size**2, turn=True, winner=None,size = size ,terminal=False)
    while(True): #Initial menu
        try:
            choose = input("Select number: ")
            assert choose in ["1","2","3"], "Must be one of the options"
            break
        except:
            print("You must choose one of the options")
    choose = int(choose)
    player = 1
    if choose ==3:
        choose = 2
        player = 0
    mvc.view(board.tup,size,round)
    while(True): #Loop of the total game
        player = int(not player) #Change player
        while(True): #Loop of a turn of a player
            if choose == 2 and player ==1:#Agent turn
                for _ in range(train_steps):
                    agent.do_rollout(board)
                board = agent.choose(board)
                print("IA choose")
                mvc.view(board.tup,size,round)
                break
            else: #Player turn
                while(True): #Player choose play
                    try:
                        print("Player:", player)
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
        player_won = mvc._find_winner(board.tup,size)
        if player_won != None: #Game check if the player won
            print("Congratulations, player",player_won,"won")
            break
        if mvc._isTie(size,round): #Game check if there is tie
            print("Game finish in a tie")
            break

if __name__ == "__main__":
    main()
