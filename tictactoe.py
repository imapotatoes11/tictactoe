"""
Tic Tac Toe Player
"""

import math
import copy
from random import choice

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
    x = 9
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == EMPTY:
                x -= 1
    if x % 2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultt = copy.deepcopy(board)
    if resultt[action[0]][action[1]] != EMPTY:
        raise InvalidBoardStateError
    resultt[action[0]][action[1]] = player(board)
    return resultt

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        if board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        if board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
    if board[1][1] == X:
        if board[0][0] == X and board[2][2] == X or board[0][2] == X and board[2][0] == X:
            return X
    if board[1][1] == O:
        if board[0][0] == O and board[2][2] == O or board[0][2] == O and board[2][0] == O:
            return O
    return EMPTY

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY:
        return True
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    a = actions(board)
    p = player(board)
    if p == X:
        tmp = []
        tmp2 = []
        tmp3 = -2
        for action in a:
            util = Min(result(board, action))
            tmp.append(action)
            tmp2.append(util)
            if util > tmp3:
                tmp3 = util
        i = [0, len(tmp)]
        while i[0] < i[1]:
            if tmp2[i[0]] < tmp3:
                tmp.pop(i[0])
                tmp2.pop(i[0])
                i[0] -= 1
                i[1] -= 1
            i[0] += 1
        print(f"{tmp3}")
    else:
        tmp = []
        tmp2 = []
        tmp3 = 2
        for action in a:
            util = Max(result(board, action))
            tmp.append(action)
            tmp2.append(util)
            if util < tmp3:
                tmp3 = util
        i = [0, len(tmp)]
        while i[0] < i[1]:
            if tmp2[i[0]] > tmp3:
                tmp.pop(i[0])
                tmp2.pop(i[0])
                i[0] -= 1
                i[1] -= 1
            i[0] += 1
        print(f"{tmp3}")
    print("")
    return choice(tmp)

def Max(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, Min(result(board, action)))
    return v

def Min(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, Max(result(board, action)))
    return v