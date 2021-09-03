import numpy as np 
from copy import deepcopy 

from solvingAlgorithms.connected4_heuristic import * 

LENGTH, WIDTH = 8, 8
MAX = True
MIN = False

# Minimax Tree node
class Node:
    parent = None 
    children = []
    state = np.array([]) 
    humanScore = 0
    agentScore = 0
    depth = 0 
    utility = None 
    minimax = None 
    change = None 
    terminal = False 
    
# Find the right move according to the Minimax search algorithm
# k is the limit that we will truncate the game tree after K levels evaluating the states using the heuristic function.
# isPruning is a boolean indicates if we want to use alpha-beta pruning or not
def make_decision(state, k, isPruning, humanScore, agentScore) :
    root = Node()
    root.state = state
    root.minimax = MAX
    root.humanScore = humanScore
    root.agentScore = agentScore
    new_state = maximize(root, k, isPruning, -10000, 10000)
    return new_state, root

# Find the child state with the highest utility value
def maximize(node: Node, k, isPruning, alpha, beta) :
    if (terminal_test(node.state, k)) :
        node.terminal = True
        return (None , eval(node))
    
    max_child, max_utility = (None,-10000)
    
    for child in make_children(node, k-1, 2) :
        null, utility = minimize(child, k-1, isPruning, alpha, beta)
        if utility > max_utility :
            max_child, max_utility = (child.state, utility)
        if isPruning and max_utility >= beta :
            break
        if isPruning and max_utility > alpha :
            alpha = max_utility

    node.utility = max_utility

    return (max_child, max_utility)

# Find the child state with the lowest utility value
def minimize(node: Node, k, isPruning, alpha, beta) :
    if (terminal_test(node.state, k)) :
        node.terminal = True
        return (None , eval(node))
    
    min_child, min_utility = (None,10000)

    for child in make_children(node, k-1, 1) :
        null, utility = maximize(child, k-1, isPruning, alpha, beta)
        if utility < min_utility :
            min_child, min_utility = (child.state, utility)
        if isPruning and min_utility <= alpha :
            break
        if isPruning and min_utility < beta :
            beta = min_utility

    node.utility = min_utility

    return (min_child,min_utility)

# Check if this state is a terminal state and if exceeds K levels
def terminal_test(state, k) :
    if k > 0 and 0 in state:
        return False
    return True
    
# Find the possible moves for the next step
def make_children(node: Node, k: int, player) :
    children = []
    for i in range(LENGTH):
      for j in range(WIDTH):
        if node.state[i][j] == 0:
            if i < LENGTH-1 and node.state[i+1][j] != 0 or i == LENGTH-1:
                new_state = deepcopy(node.state)
                new_state[i][j] = player
                child = Node(new_state, not node.minimax, j, k)
                children.append(child)
               
    node.children = children
    return children

def eval(node: Node) :
    return calculateHeuristic(node.state, node.humanScore, node.agentScore)

