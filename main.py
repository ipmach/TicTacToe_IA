import sys
from boardInterfaces import graphicInterface, terminalInterface
from agents import agent_MCTS,agent_HMM
import player


def main():
    try:
        size = int(sys.argv[1])
        train_steps = int(sys.argv[2])
        height = int(sys.argv[3])
        width = int(sys.argv[4])
    except:
        raise RuntimeError("Error: must be 'python main size train_steps height width' with ints ")
    print("Welcome, choose game type:")
    print("1) Player vs Player")
    print("2) Player vs IA")
    print("3) IA vs Player")
    print("4) IA vs IA")
    while(True): #Initial menu
        try:
            game_mode = input("Select number: ")
            assert game_mode in ["1","2","3","4"], "Must be one of the options"
            break
        except:
            print("You must choose one of the options")

    print("Choose board:")
    print("1) Graphic board")
    print("2) Terminal board")
    while(True): #Initial menu
        try:
            boardType = input("Select number: ")
            assert boardType in ["1","2"], "Must be one of the options"
            break
        except:
            print("You must choose one of the options")

    agent_choose = 0
    if int(game_mode) > 1:
        print("Choose IA to fight against:")
        print("1) MCTS (Monte Carlo Tree Search)")
        print("2) HMM (Hidden Markov Model)")
        while(True): #Initial menu
            try:
                agent_choose = input("Select number: ")
                assert agent_choose in ["1","2"], "Must be one of the options"
                break
            except:
                print("You must choose one of the options")

    ##LOAD AGENT
    agent_choose = int(agent_choose)
    if agent_choose ==1:
        agent = agent_MCTS.MCTS(exploration_weight = 150)
        print("MCTS loaded")
    elif agent_choose ==2:
        agent = agent_HMM.HMM(exploration_weight = 10, size = size)
        print("HMM loaded")
    else:
        agent = None

    #CHOOSE GAME MODE
    game_mode = int(game_mode)
    turnPlayer = player.players()
    if game_mode == 1:
        turnPlayer.insertPlayer_1(player.typePlayer.GRAPHIC_PLAYER)
        turnPlayer.insertPlayer_2(player.typePlayer.GRAPHIC_PLAYER)
    elif game_mode == 2:
        turnPlayer.insertPlayer_1(player.typePlayer.GRAPHIC_PLAYER)
        turnPlayer.insertPlayer_2(player.typePlayer.IA_PLAYER)
    elif game_mode == 3:
        turnPlayer.insertPlayer_1(player.typePlayer.IA_PLAYER)
        turnPlayer.insertPlayer_2(player.typePlayer.GRAPHIC_PLAYER)
    elif game_mode == 4:
        turnPlayer.insertPlayer_1(player.typePlayer.IA_PLAYER)
        turnPlayer.insertPlayer_2(player.typePlayer.IA_PLAYER)

    boardType = int(boardType)
    if boardType == 1:
        graphicInterface.gameInterface(height,width,size,train_steps,turnPlayer,agent)
    else:
        terminalInterface.gameTerminal(size,train_steps,turnPlayer,agent)

if __name__ == "__main__":
    main()
