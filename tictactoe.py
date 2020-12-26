"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():

   # Returns starting state of the board.

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    #Returns player who has the next turn on a board.

    SO=0
    SX=0
    for i in board :
        for j in i:
            if j == "X" :
                SX +=1
            elif j == "O":
                SO +=1
    if SX == 5 :
        return(None)
    elif SO == SX :
        return("X")
    else:
        return("O")


def actions(board):

    #Returns set of all possible actions (i, j) available on the board.

    E= set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY :
                E.add((i,j))
    return(E)


def result(board, action):
    
    #Returns the board that results from making move (i, j) on the board.

    i,j = action
    if board[i][j] != EMPTY :
        raise Exception("dude u can't do this")
    newboard = copy.deepcopy(board)
    p = player(board)
    newboard[i][j] = p
    return(newboard)

def winner(board):
    
    #Returns the winner of the game, if there is one.
    
    ld=[]
    lad=[]
    for i in range(3) :
        if board[i] == ["X","X","X"] :
            return("X")
        elif board[i] == ["O","O","O"] :
            return("O")
        l=[]
        for j in range(3) :
            l.append(board[j][i])
        if l == ["X","X","X"] :
            return("X")
        elif l == ["O","O","O"] :
            return("O")
        ld.append(board[i][i])
        lad.append(board[2-i][i])
    if ld == ["X","X","X"] or lad == ["X","X","X"] :
            return("X")
    elif (ld == ["O","O","O"]) or (lad == ["O","O","O"]):
            return("O")
    return(None)

def terminal(board):
    
    #Returns True if game is over, False otherwise.
    
    for i in board :
        for j in i :
            if (j == EMPTY) and (winner(board) == None) :
                return(False)
    return(True)


def utility(board):

    #Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    
    p=winner(board)
    if p == "X":
        return(1)
    elif p == "O" :
        return(-1)
    else:
        return(0)


def min_value(board):

      #The minimum value of a board.
      
     if terminal(board):
           return(utility(board))
     v = 10
     for i in actions(board):
           v = min(v,max_value(result(board,i)))
     return(v)


def max_value(board):

      #The maximum value of a board.

      
     if terminal(board):
           return(utility(board))
     v = -10
     for i in actions(board):
           v = max(v,min_value(result(board,i)))
     return(v)

      
def value(elem):

      return(elem[0])

def minimax(board):

    #Returns the optimal action for the current player on the board.

    if terminal == True :
        return(None)
    elif player(board) == "X" :
        L = [(max_value( result(board,a) ),a) for a in actions(board)]
        L.sort(reverse = True,key = value)
        return(L[0][1])
    elif player(board) == "O" :
        L = [(min_value( result(board,a) ),a) for a in actions(board)]
        L.sort(key = value)
        return(L[0][1])
