import numpy as np

def view(tup,size,round):
    """
    Print in the console the actual state of the board.
    """
    print("Round:", round)
    up_aux = np.array(tup)
    for i in range(size+1):
        if i == 0:
            print(" "," ",end="")
        else:
            print(i," ",end="")
    print("")
    for i in range(size):
        for j in range(size+1):
            if j == 0:
                print(i+1," ",end = "")
            else:
                aux = up_aux[i*size + j-1]
                if aux == True:
                    print("x"," ",end = "")
                elif aux == False:
                    print("o"," ",end = "")
                else:
                        print(" "," ",end = "")
        print(" ")

def _isTie(size,round):
    """
    Check if the game finish in a tie.
    Return True if is a tie.
    """
    isfinish =  True if size*size ==round else False
    return isfinish


def _find_winner(tup,size):
    """
    Check if the player won the game.
    Return True if is a win.
    """
    won = None
    for player in [True,False]:
        check = np.zeros((size,size))
        tup_aux = np.array(tup)
        for i in range(size): #Transform the string list to a int matrix
            for j in range(size):
                check[i][j] = 1 if tup_aux[i*size + j] == player else 0
        #Check if the player won in the rows
        winRow = any([np.sum(check[i]) == size for i in range(size)])
        #Check if the player won in the columns
        checkT = check.transpose()
        winColumn = any([np.sum(checkT[i]) == size for i in range(size)])
        #Check if the player won in the diagonals
        winDig = np.sum(check.diagonal()) == size
        winDigI = np.sum(np.rot90(check).diagonal()) == size
        if any([winRow,winColumn,winDig,winDigI]):
            won = player
    return won

def _find_winner_UI(tup,size):
    """
    Check if the player won the game.
    Return True if is a win.
    """
    for player in [True,False]:
        check = np.zeros((size,size))
        tup_aux = np.array(tup)
        for i in range(size): #Transform the string list to a int matrix
            for j in range(size):
                check[i][j] = 1 if tup_aux[i*size + j] == player else 0
        #Check if the player won in the rows
        winRow = [np.sum(check[i]) == size for i in range(size)]
        #Check if the player won in the columns
        checkT = check.transpose()
        winColumn = [np.sum(checkT[i]) == size for i in range(size)]
        #Check if the player won in the diagonals
        winDig = np.sum(check.diagonal()) == size
        winDigI = np.sum(np.rot90(check).diagonal()) == size
        if any([any(winRow),any(winColumn),winDig,winDigI]):
            return True,[winRow,winColumn,winDig,winDigI]
    return False,[]

def convert(x):
    """
    Convert the boolean list to a int list.
    """
    if x == None:
        return 2
    if x == False:
        return 0
    else:
        return 1

converv = np.vectorize(convert)

def _find_new(old_tup,new_tup,size, inIndex = False):
    """
    Find the new element on the board updated.
    """
    a = converv(np.array(old_tup))
    b = converv(np.array(new_tup))
    index = np.nonzero(a - b)[0][0]
    if inIndex:
        return index
    row = int(index/size)
    col = index - size*row
    return col,row


def correctNumber(size,aux):
    """
    Check if the number is inside the board.
    """
    return 0 < aux <= size
