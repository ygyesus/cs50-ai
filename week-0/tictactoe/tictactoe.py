"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xCount = oCount = 0
    for row in board:
        xCount += row.count(X)
        oCount += row.count(O)

    if xCount == oCount:
        return X
    elif xCount > oCount:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))

    return moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i,j = action


    if not board[i][j] == EMPTY or not (0<=i<3 and 0<=j<3):
        raise Exception("Cell is already occupied!")

    newBoard = deepcopy(board)
    turn = player(newBoard)
    newBoard[i][j] = turn

    return newBoard

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 3 horizontal checks
    for row in range(3):
        if board[row] == [X,X,X]: return X
        if board[row] == [O,O,O]: return O

    # 2 diagonal checks
    if board[0][0] == board[1][1] == board[2][2]: 
        if board[1][1]:
            return board[1][1]
    if board[2][0] == board[1][1] == board[0][2]: 
        if board[1][1]:
            return board[1][1]

    # 3 vertical checks
    for col in range(3):
        
        if board[0][col] == board[1][col] == board[2][col]: 
            if board[1][col]:
                return board[1][col]
        
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board): return True

    for row in board:
        if EMPTY in row: return False

    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if X == winner(board): return 1
    if O == winner(board): return -1
    return 0
    raise NotImplementedError

v_to_action = {}
def minValue(board):
    if terminal(board): return utility(board)

    v = float('inf')
    ans_action = None
    for action in actions(board):
        val = maxValue(result(board, action))
        if val<v:
            v = val
            ans_action = action

    v_to_action[v] = ans_action

    return v

def maxValue(board):
    if terminal(board): return utility(board)

    v = float('-inf')
    for action in actions(board):
        val = minValue(result(board, action))

        if val>v:
            v = val
            ans_action = action
    v_to_action[v] = ans_action
    return v  

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    turn = player(board)
    if turn == X:
        v = maxValue(board)
        return v_to_action[v]
    else:
        v = minValue(board)
        return v_to_action[v]




    raise NotImplementedError
