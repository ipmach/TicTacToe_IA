import sys
from boardInterfaces import graphicInterface, terminalInterface, stadisticInterface
from agents import agent_MCTS,agent_Heuristic, agent_MiniMax
import player

def agents_choose(agent_choose,size):
    agent_choose = int(agent_choose)
    if agent_choose ==1:
        agent = agent_MCTS.MCTS(exploration_weight = 150)
        print("MCTS loaded")
    elif agent_choose ==2:
        agent = agent_MiniMax.MiniMax(6)
        print("MiniMax loaded")
    elif agent_choose == 3:
        agent = agent_Heuristic.Heuristic()
        print("Heuristic loaded")
    else:
        agent = None
    return agent

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
    print("5) IA vs IA stadistics")
    while(True): #Initial menu
        try:
            game_mode = input("Select number: ")
            assert game_mode in ["1","2","3","4","5"], "Must be one of the options"
            break
        except:
            print("You must choose one of the options")

    boardType = "0"
    if int(game_mode) < 5:
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
        print("Choose IA:")
        print("1) MCTS (Monte Carlo Tree Search)")
        print("2) MiniMax")
        print("3) Heuristic")
        while(True): #Initial menu
            try:
                agent_choose = input("Select number: ")
                assert agent_choose in ["1","2","3"], "Must be one of the options"
                break
            except:
                print("You must choose one of the options")

    if int(game_mode) >= 4:
        print("Choose second IA:")
        print("1) MCTS (Monte Carlo Tree Search)")
        print("2) MiniMax (with Alpha Beta pruning)")
        print("3) Heuristic")
        while(True): #Initial menu
            try:
                agent_choose2 = input("Select number: ")
                assert agent_choose2 in ["1","2","3"], "Must be one of the options"
                break
            except:
                print("You must choose one of the options")

    ##LOAD AGENT
    agent = agents_choose(agent_choose,size)
    agent2 = agents_choose(agent_choose2,size) if int(game_mode) >= 4 else None
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
    elif game_mode >= 4:
        turnPlayer.insertPlayer_1(player.typePlayer.IA_PLAYER)
        turnPlayer.insertPlayer_2(player.typePlayer.IA_PLAYER_2)

    boardType = int(boardType)
    if game_mode == 5:
        stadisticInterface.gameStadistic(size,train_steps,turnPlayer,agent,agent2)
    elif boardType == 1:
        graphicInterface.gameInterface(height,width,size,train_steps,turnPlayer,agent,agent2)
    else:
        terminalInterface.gameTerminal(size,train_steps,turnPlayer,agent,agent2)

if __name__ == "__main__":
    main()
