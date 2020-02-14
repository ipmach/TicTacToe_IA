import sys
from boardInterfaces import graphicInterface, terminalInterface, stadisticInterface
from agents import agent_MCTS,agent_Heuristic, agent_MiniMax,agent_QLearning
import player
import json

def agents_choose(agent_choose,size):
    """
    Load the agent
    """
    agent_choose = int(agent_choose)
    data = config()
    if agent_choose ==1:
        agent = agent_MCTS.MCTS(exploration_weight = data["agents"]["MCST"]["exploration_weight"])
        print("MCTS loaded")
    elif agent_choose ==2:
        agent = agent_MiniMax.MiniMax(data["agents"]["MiniMax"]["depth"])
        print("MiniMax loaded")
    elif agent_choose == 3:
        agent = agent_Heuristic.Heuristic()
        print("Heuristic loaded")
    elif agent_choose == 4:
        agent = agent_QLearning.QLearning(size = size)
        print("Q learning loaded")
    else:
        agent = None
    return agent

def config():
    """
    Load the config.json file
    """
    try:
        with open('config.json') as f:
            data = json.load(f)
    except:
        assert False, "Error reading config.json."
    return data

def train(agent):
    """
    Train the agent
    """
    data = config()
    learning_rate = data["agents"]["Training"]["learning_rate"]
    total_games = data["agents"]["Training"]["total_games"]
    loadPre = data["agents"]["Training"]["preload"]
    print("Training agent")
    agent.train_model(total_games, learning_rate = learning_rate, loadPre = loadPre)
    return agent

def main():
    try:
        size = int(sys.argv[1])
        data = config()
        width = data["Graphic interace screen"]["witdh"]
        height = data["Graphic interace screen"]["height"]
        train_steps = data["agents"]["train_steps"]
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
        print("4) Q learning")
        while(True): #Initial menu
            try:
                agent_choose = input("Select number: ")
                assert agent_choose in ["1","2","3","4"], "Must be one of the options"
                break
            except:
                print("You must choose one of the options")

    if int(game_mode) >= 4:
        print("Choose second IA:")
        print("1) MCTS (Monte Carlo Tree Search)")
        print("2) MiniMax (with Alpha Beta pruning)")
        print("3) Heuristic")
        print("4) Q learning")
        while(True): #Initial menu
            try:
                agent_choose2 = input("Select number: ")
                assert agent_choose2 in ["1","2","3","4"], "Must be one of the options"
                break
            except:
                print("You must choose one of the options")

    ##LOAD AGENT
    agent = agents_choose(agent_choose,size)
    agent = train(agent)
    agent2 = agents_choose(agent_choose2,size) if int(game_mode) >= 4 else None
    agent2 = train(agent2) if int(game_mode) >= 4 else None
    #CHOOSE GAME MODE
    game_mode = int(game_mode)
    turnPlayer = player.players()
    if game_mode == 1:
        turnPlayer.insertPlayer_1(player.typePlayer.GRAPHIC_PLAYER, "Player 1")
        turnPlayer.insertPlayer_2(player.typePlayer.GRAPHIC_PLAYER, "Player 2")
    elif game_mode == 2:
        turnPlayer.insertPlayer_1(player.typePlayer.GRAPHIC_PLAYER, "Player 1")
        turnPlayer.insertPlayer_2(player.typePlayer.IA_PLAYER, agent.agent_name)
    elif game_mode == 3:
        turnPlayer.insertPlayer_1(player.typePlayer.IA_PLAYER, agent.agent_name)
        turnPlayer.insertPlayer_2(player.typePlayer.GRAPHIC_PLAYER, "Player 2")
    elif game_mode >= 4:
        turnPlayer.insertPlayer_1(player.typePlayer.IA_PLAYER, agent.agent_name)
        turnPlayer.insertPlayer_2(player.typePlayer.IA_PLAYER_2, agent2.agent_name)

    boardType = int(boardType)
    if game_mode == 5:
        visualize = data["Stadistics interface"]["visualize"]
        save_games = data["Stadistics interface"]["save_games"]
        stadisticInterface.gameStadistic(size,train_steps,turnPlayer,agent,agent2,save_games = save_games,visualize =visualize)
    elif boardType == 1:
        graphicInterface.gameInterface(height,width,size,train_steps,turnPlayer,agent,agent2)
    else:
        terminalInterface.gameTerminal(size,train_steps,turnPlayer,agent,agent2)

if __name__ == "__main__":
    main()
