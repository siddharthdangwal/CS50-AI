"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


#defining custom exception inheriting from the base exception class
class InvalidActionError(Exception):
    
    def __init__(self,value):
        self.value = value
    
    #to print the exception value
    def __str__(self):
        return(repr(self.value))
        

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
    
    x_num = 0
    o_num = 0
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == X):
                x_num += 1
            elif(board[i][j] == O):
                o_num += 1
    
    if(x_num == o_num):
        return X
    elif (x_num == (o_num +1)):
        return O
    else:
        raise Exception("InvalidBoard")
    
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible_moves = []
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                possible_moves.append((i,j))
                
    return possible_moves
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_with_turn = player(board)
    
    #can't just equate objects in python
    new_board = copy.deepcopy(board)
            
    if(action == None):
        return new_board
    
    row_action = action[0]
    col_action = action[1]
    
    if (board[row_action][col_action] == EMPTY):
        new_board[row_action][col_action] = player_with_turn
    else:
        raise (InvalidActionError((row_action,col_action)))
    
    return new_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    num_x_together = 0
    num_o_together = 0
    
    #checking all the rows first
    for i in range(3):
        
        num_x_together = 0
        num_o_together = 0
        
        for j in range(3):
            
            if(board[i][j] == X):
                num_x_together += 1
            elif(board[i][j] == O):
                num_o_together += 1
        
        if(num_x_together == 3):
            return X
        elif(num_o_together == 3):
            return O
    
    #checking all the columns now
    for i in range(3):
        
        num_x_together = 0
        num_o_together = 0
            
        for j in range(3):
            
            if(board[j][i] == X):
                num_x_together += 1
            elif(board[j][i] == O):
                num_o_together += 1
        
        if(num_x_together == 3):
            return X
        elif(num_o_together == 3):
            return O
    
    #checking the diagonals now
    num_x_together = 0
    num_o_together = 0
    for i in range(3):
        if(board[i][i] == X):
            num_x_together += 1
        elif(board[i][i] == O):
            num_o_together += 1
    if(num_x_together == 3):
            return X
    elif(num_o_together == 3):
            return O
    
    num_x_together = 0
    num_o_together = 0
    for i in range(3):
        if(board[i][2-i] == X):
            num_x_together += 1
        elif(board[i][2-i] == O):
            num_o_together += 1
    if(num_x_together == 3):
            return X
    elif(num_o_together == 3):
            return O
        
    #if no one is the winner then
    return None        
    
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game_winner = winner(board)
    
    if(game_winner == X or game_winner == O):
        return True
    
    #checking if the board is full or not
    empty_spots = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                empty_spots += 1
    
    #if the board is full
    if(empty_spots == 0):
        return True
    
    return False
        
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #ensure that the board is a terminal board
    assert (terminal(board) == True)
    
    if (winner(board) == X):
        return 1
    elif(winner(board) == O):
        return -1
    else:
        return 0
    
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #No optimal move if the board is already terminal
    if(terminal(board)):
        return None
    
    next_player = player(board)
    
    if(next_player == X):
        (score,best_action) = max_value(board)
        return best_action
    
    else:
        (score,best_action) = min_value(board)
        return best_action
        
        
        
        
    #raise NotImplementedError


def max_value(board):
    """returns the max_value and the action that leads to
    that max_value for a maximising state board as a tuple 
    (value,action). Assuming input is a non-terminal board"""
    
    if(terminal(board)):
        return (utility(board), None)
    
    max_val = -float('inf')
    best_action = None
    for action in actions(board):
        result_board = result(board, action)
        (min_val, min_action) = min_value(result_board)
        if(min_val > max_val):
            max_val = min_val
            best_action = action
    
    return (max_val, best_action)
        
def min_value(board):
    """returns the min_value and the action that leads to
    that min_value for a minimising state board as a tuple 
    (value,action). Assuming input is a non-terminal board"""
    
    if(terminal(board)):
        return (utility(board), None)

    min_val = float('inf')
    best_action = None
    for action in actions(board):
        result_board = result(board, action)
        (max_val, max_action) = max_value(result_board)
        if(max_val < min_val):
            min_val = max_val
            best_action = action
    
    return (min_val, best_action)
