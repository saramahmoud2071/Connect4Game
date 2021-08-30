import numpy as np
from copy import deepcopy 

LENGTH, WIDTH = 8, 8

# Find the right move according to the Minimax search algorithm
# k is the limit that we will truncate the game tree after K levels evaluating the states using the heuristic function.
# isPruning is a boolean indicates if we want to use alpha-beta pruning or not
def make_decision(state, k, isPruning) :
    new_state = maximize(state, k, isPruning, -10000, 10000)
    return new_state

# Find the child state with the highest utility value
def maximize(state, k, isPruning, alphaa, beta) :
    if (terminal_test(state, k)) :
        return (None , eval(state))
    
    max_child, max_utility = (None,-10000)

    for child in make_children(state, 2) :
        null, utility = minimize(child, k-1)
        if utility > max_utility :
            max_child, max_utility = (child, utility)
        if isPruning and max_utility >= beta :
            break
        if isPruning and max_utility > alphaa :
            alphaa = max_utility

    return (max_child, max_utility)

# Find the child state with the lowest utility value
def minimize(state, k, isPruning, alphaa, beta) :
    if (terminal_test(state, k)) :
        return None , eval(state)
    
    min_child, min_utility = (None,10000)

    for child in make_children(state, 1) :
        null, utility = maximize(child, k-1)
        if utility < min_utility :
            min_child, min_utility = (child, utility)
        if isPruning and min_utility <= alphaa :
            break
        if isPruning and min_utility < beta :
            beta = min_utility

    return (min_child,min_utility)

# Check if this state is a terminal state and if exceeds K levels
def terminal_test(state, k) :
    if k > 0 and 0 in state :
        return False
    return True
    
# Find the possible moves for the next step
def make_children(state, player) :
    children = []
    for i in range(len(state)) :
        for j in range(len(state[0])) :
            if state[i][j] == 0 :
                new_state = deepcopy(state)
                new_state[i][j] = player
                children.append(new_state)

    return children

def eval(state) :
    

    return