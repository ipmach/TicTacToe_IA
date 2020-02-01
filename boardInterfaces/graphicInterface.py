#!/usr/bin/python

#GIT: https://github.com/nyergler/teaching-python-with-pygame/blob/master/ttt-tutorial/tictactoe.py
# import necessary modules
import pygame
import numpy as np
from pygame.locals import *
from game_nodes import Model
from mvc import _find_winner_UI,_find_new,view, _find_winner,correctNumber,_isTie
import time
import player


#Initial parameters
XO   = "X" #First character
winner = None #winner
height = 300 #height of the board
width =300 #width of the board
size = 3 #size of the board
train_steps = 1000 #training steps of the tree
game_type= 0 #Game type 0: Player vs Player, 1: Player vs IA, 2: IA vs Player
board = None #Board interface
model = None #Model of the game
agent = None #IA who plays
agent2 = None #second IA (optional)
round = 0 #Round game
turnPlayer = None #object players

def initBoard(ttt):
    """
    Initialize the board
    """
    global size, height,width
    # set up the background surface
    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((220, 220, 220))
    # draw the grid lines
    # vertical lines...
    high = height/size
    for i in range(1,size):
        pygame.draw.line (background, (0,0,0), (i*high, 0), (i*high, height), 2)

    # horizontal lines...
    large = width/size
    for i in range(1,size):
        pygame.draw.line (background, (0,0,0), (0, i*large), (width, i*large), 2)

    return background

def drawStatus (board):
    """
    Write the message of the actual status of the game
    """
    global XO, winner,size, height,width,round, turnPlayer

    # determine the status message
    # determine the status message
    if _isTie(size,round):
        message = "Tie"
    elif (winner is None):
        message = "Round: " + str(round) + "     " + XO + "'s turn"
    else:
        if winner == True:
            message = "Round: " + str(round) + "     " + "X" + " won!" + " Congratulations: " + turnPlayer.PLAYER1
        else:
            message =  "Round: " + str(round) + "     " +"O" + " won!" + " Congratulations: " + turnPlayer.PLAYER2

    # render the status message
    font = pygame.font.Font(None, 30)
    text = font.render(message, 5, (240, 240, 240))

    # copy the rendered message onto the board
    board.fill ((105, 105, 105), (0, height, width, 25))
    board.blit(text, (10, width))

def showBoard (ttt, board):
    """
    Display the update board.
    """
    drawStatus (board)
    ttt.blit (board, (0, 0))
    pygame.display.flip()

def boardPos (mouseX, mouseY):
    """
    Given a set of coordinates from the mouse, determine which board space.
    (row, column) the user clicked in.
    """
    global size, height,width

    # determine the row the user clicked
    high = height/size
    for i in range(1,size+1):
        if mouseY < high*i:
            row = i -1
            break
    # determine the column the user clicked
    large = width/size
    for i in range(1,size+1):
        if mouseX < large*i:
            col = i -1
            break
    # return the tuple containg the row & column
    return (row, col)

def drawMove (board, boardRow, boardCol, Piece):
    """
     Draw the new move in the board.
     board     : the game board surface
     boardRow,
     boardCol  : the Row & Col in which to draw the piece (0 based)
     Piece     : X or O
    """
    # determine the center of the square
    global model, size, height, width
    high = height/size
    large = width/size
    centerX = int(((boardCol) * high) + high/2)
    centerY = int(((boardRow) * large) + large/2)
    # draw the appropriate piece
    if (Piece == 'O'):
        pygame.draw.circle (board, (0,0,250), (centerX, centerY), int(high/2)- 6, 5)
    else:
        pygame.draw.line (board, (128,0,128), (centerX - int(large/4), centerY - int(high/4)), \
                         (centerX + int(large/4), centerY + int(high/4)), 5)
        pygame.draw.line (board, (128,0,128), (centerX + int(large/4), centerY - int(high/4)), \
                         (centerX - int(large/4), centerY + int(high/4)), 5)


def clickBoard(board):
    """
    Determine where the user clicked and if the space is not already
    occupied, draw the appropriate piece there (X or O).
    """
    global grid, XO,size,model

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos (mouseX, mouseY)

    # make sure no one's used this space
    index = size * row  + col
    if np.array(model.tup)[index] != None:
        print("That position is already taken.")
        # this space is in use
        return

    model = model.make_move(index)

    # draw an X or O
    drawMove (board, row, col, XO)

    # toggle XO to the other player's move
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"

def gameWon(board):
    """
    Draw the line of the winning combination.
    """
    global grid, winner,model,size,height, width
    isWin, data =  _find_winner_UI(model.tup,size)
    if isWin: #Enter here if a player won the game
        if any(data[0]): #Draw for winning row
            high = height/size
            for row in range(0,size):
                if data[0][row]:
                    winner = _find_winner(model.tup,size)
                    pygame.draw.line (board, (250,0,0), (0, (row + 1)*high - high/2), \
                                      (height, (row + 1)*high - high/2), 5)
                    break

        elif any(data[1]): #Draw winning column
            large = width/size
            for col in range(0,size):
                if data[1][col]:
                    winner = _find_winner(model.tup,size)
                    pygame.draw.line (board, (250,0,0), ((col + 1)* large - large/2, 0), \
                                      ((col + 1)* large - large/2, width), 5)
                    break

        elif data[2]: #Draw winning diagonal
            high = height/(2*size)
            large = width/(2*size)
            winner = _find_winner(model.tup,size)
            pygame.draw.line (board, (250,0,0), (high, large), (height - high, width - large), 5)

        elif data[3]:#Draw winning diagonal
            high = height/(2*size)
            large = width/(2*size)
            winner = _find_winner(model.tup,size)
            pygame.draw.line (board, (250,0,0), (height - high, high), (large, width - large), 5)

def playIA(board,agent):
    """
    Make the play from the IA
    """
    global model,size,train_steps,XO
    for _ in range(train_steps):
        agent.do_rollout(model)
    model_new = agent.choose(model)
    col,row= _find_new(model.tup,model_new.tup,size)
    model = model_new
    drawMove (board, row, col, XO)
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"

# --------------------------------------------------------------------
# initialize pygame and our window

def gameInterface(heightP,widthP,sizeP,train_stepsP,turnPlayers,agent_choose,agent_choose2):
    global height,width,size,train_steps,game_type,board,model,agent, agent2,winner,round, turnPlayer
    pygame.init()
    agent = agent_choose
    agent2 = agent_choose2
    height = heightP
    width =widthP
    size = sizeP
    train_steps = train_stepsP
    round = 0
    ttt = pygame.display.set_mode ((height, width+25))
    turnPlayer = turnPlayers

    pygame.display.set_caption ('Tic-Tac-Toe')
    # create the game board
    board = initBoard (ttt)
    model = Model(tup=(None,) * size**2, turn=True, winner=None,size = size ,terminal=False)
    # main event loop
    running = 1
    while (running == 1):
        #Events created by the player
        for event in pygame.event.get():
            if event.type is QUIT:
                running = 0
            elif winner == None and not _isTie(size,round):
                if event.type is MOUSEBUTTONDOWN and turnPlayer.playerTurn() == player.typePlayer.GRAPHIC_PLAYER:
                    # the user clicked; place an X or O
                    clickBoard(board)
                    view(model.tup,size,round)
                    round +=1
                    turnPlayer.newTurn()
                    gameWon(board)
                    showBoard (ttt, board)
        #Plays by the IA
        if winner == None and not _isTie(size,round):
            if turnPlayer.playerTurn() == player.typePlayer.IA_PLAYER:
                playIA(board,agent)
                view(model.tup,size,round)
                round +=1
                turnPlayer.newTurn()
            elif turnPlayer.playerTurn() == player.typePlayer.IA_PLAYER_2:
                playIA(board,agent2)
                view(model.tup,size,round)
                round +=1
                turnPlayer.newTurn()
        # check for a winner
        gameWon(board)
        # update the display
        showBoard (ttt, board)

#gameInterface(600,600,3,100,1)
