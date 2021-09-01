from copy import deepcopy 

from solvingAlgorithms.connected4_heuristic import * 

LENGTH, WIDTH = 8, 8

class Node:
    children = []
    parent = None
    state = []
    depth = 0
    
# Find the right move according to the Minimax search algorithm
# k is the limit that we will truncate the game tree after K levels evaluating the states using the heuristic function.
# isPruning is a boolean indicates if we want to use alpha-beta pruning or not
def make_decision(state, k, isPruning) :
    root = Node()
    root.state = state
    new_state = maximize(root, k, isPruning, -10000, 10000)
    return new_state, root

# Find the child state with the highest utility value
def maximize(node, k, isPruning, alpha, beta) :
    if (terminal_test(node.state, k)) :
        return (None , eval(node.state))
    
    max_child, max_utility = (None,-10000)
    
    for child in make_children(node, 2) :
        null, utility = minimize(child, k-1, isPruning, alpha, beta)
        if utility > max_utility :
            max_child, max_utility = (child.state, utility)
        if isPruning and max_utility >= beta :
            break
        if isPruning and max_utility > alpha :
            alpha = max_utility

    return (max_child, max_utility)

# Find the child state with the lowest utility value
def minimize(node, k, isPruning, alpha, beta) :
    if (terminal_test(node.state, k)) :
        return (None , eval(node.state))
    
    min_child, min_utility = (None,10000)

    for child in make_children(node, 1) :
        null, utility = maximize(child, k-1, isPruning, alpha, beta)
        if utility < min_utility :
            min_child, min_utility = (child.state, utility)
        if isPruning and min_utility <= alpha :
            break
        if isPruning and min_utility < beta :
            beta = min_utility

    return (min_child,min_utility)

# Check if this state is a terminal state and if exceeds K levels
def terminal_test(state, k) :
    if k > 0 and has_zero(state):
        return False
    return True
    
# Find the possible moves for the next step
def make_children(node, player) :
    children = []
    for i in range(LENGTH):
      for j in range(WIDTH):
        if node.state[i][j] == 0:
            if i < LENGTH-1 and node.state[i+1][j] != 0 or i == LENGTH-1:
                child = Node()
                child.state = deepcopy(node.state)
                child.state[i][j] = player
                child.parent = node
                children.append(child)
               
    node.children = children
    return children

def eval(state) :
    return calculateHeuristic(state)

def has_zero(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return True
    return False

