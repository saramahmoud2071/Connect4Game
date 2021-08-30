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
    # q: number of connected 4's of the human
    # w: number of connected 4's of the agent
    # e: number of connected 3's of the human
    # r: number of connected 3's of the agent
    # so heuristic equals w+r-q-e
    heuristic=0
    for i in range (0,8):
        for j in range (0,8):

        #get no of connected 4 & 3 horizontally for both players
        if j in range (0,5):
            q,w,e,r=horizontal4Or3(state,i,j)
            heuristic=heuristic+w+r-q-e
        
        #get no of connected 4 & 3 vertically for both players
        if i in range (3,8):
            q,w,e,r=vertical4Or3(state,i,j)
            heuristic=heuristic+w+r-q-e

        #get no of connected 4 & 3 diagonally for both players
        if i in range(0,5):
            if j in range (0,5):
                q,w,e,r=rightDiagonal4Or3(state,i,j)
                heuristic=heuristic+w+r-q-e

            if j in range (3,8):
                q,w,e,r=leftDiagonal4Or3(state,i,j)
                heuristic=heuristic+w+r-q-e
    
    return heuristic

def horizontal4Or3(grid,i,j):
    connected4player=0
    connected4agent=0
    connected3player=0
    connected3agent=0

    #connected 4's for the human
    if grid[i][j]== grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 1:
        connected4player= 1
    #calculate no of connected 4's for the agent    
    elif grid[i][j]== grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 2:
        connected4agent= 1

    #check connected 3 cases
    elif grid[i][j]==0 :
        if grid[i][j+1] == grid[i][j+2] == grid[i][j+3] ==1:
            connected3player= 1
        elif grid[i][j+1] == grid[i][j+2] == grid[i][j+3] ==2:
            connected3agent= 1

    elif grid[i][j]==1: 
        if grid[i][j+1] == grid[i][j+2] == 1 and grid[i][j+3] ==0:
            connected3player= 1
        elif  grid[i][j+1] ==0 and  grid[i][j+2] == grid[i][j+3] ==1:
            connected3player=1
        elif  grid[i][j+1] ==1 and grid[i][j+2] ==0 and grid[i][j+3] ==1:
            connected3player= 1   
        
    elif grid[i][j]==2: 
        if grid[i][j+1] == grid[i][j+2] == 2 and grid[i][j+3] ==0:
        connected3agent= 1
        elif  grid[i][j+1] ==0 and  grid[i][j+2] == grid[i][j+3] ==2:
            connected3agent=1
        elif grid[i][j+1] ==2 and grid[i][j+2] ==0 and grid[i][j+3] ==2:
            connected3agent= 1
            
    return connected4player,connected4agent,connected3player,connected3agent

def vertical4Or3(grid,i,j):
    connected4player=0
    connected4agent=0
    connected3player=0
    connected3agent=0

    #calculate no of connected 4's for the player
    if grid[i][j]== grid[i-1][j] == grid[i-2][j] == grid[i-3][j] == 1:
          connected4player= 1
    #calculate no of connected 4's for the agent    
    elif grid[i][j]== grid[i-1][j] == grid[i-2][j] == grid[i-3][j] == 2:
        connected4agent= 1
 
    #check connected 3 cases
    elif grid[i][j]==0:
        if grid[i-1][j] == grid[i-2][j] == grid[i-3][j] ==1:
            connected3player= 1
        elif grid[i-1][j] == grid[i-2][j] == grid[i-3][j] ==2:
            connected3agent= 1
          
    elif grid[i][j]==1:
        if grid[i-1][j] == grid[i-2][j] == 1 and grid[i-3][j] ==0:
            connected3player= 1
        elif grid[i-1][j] ==0 and  grid[i-2][j] == grid[i-3][j] ==1:
            connected3player= 1
        elif grid[i-1][j] ==1 and grid[i-2][j] ==0 and grid[i-3][j] ==1:
            connected3player= 1
      
    elif grid[i][j]==2:
        if grid[i-1][j] == grid[i-2][j] == 2 and grid[i-3][j] ==0:
            connected3agent= 1
        elif grid[i-1][j] ==0 and  grid[i-2][j] == grid[i-3][j] ==2:
            connected3agent= 1
        elif grid[i-1][j] ==2 and grid[i-2][j] ==0 and grid[i-3][j] ==2:
            connected3agent= 1

    return connected4player,connected4agent,connected3player,connected3agent


def rightDiagonal4Or3(grid,i,j):
    connected4player=0
    connected4agent=0
    connected3player=0
    connected3agent=0


    #calculate no of connected 4's for the player
    if grid[i][j]== grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == 1:
          connected4player= 1
    #calculate no of connected 4's for the agent    
    elif grid[i][j]== grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == 2:
          connected4agent= 1

    #check connected 3 cases
    elif grid[i][j]==0:
        if grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] ==1:
            connected3player= 1
        elif grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] ==2:
            connected3agent= 1
          
    elif grid[i][j]==1:
        if grid[i+1][j+1] == grid[i+2][j+2] == 1 and grid[i+3][j+3] ==0:
            connected3player= 1
        elif grid[i+1][j+1] ==0 and  grid[i+2][j+2] == grid[i+3][j+3] ==1:
            connected3player= 1
        elif grid[i+1][j+1] ==1 and grid[i+2][j+2] ==0 and grid[i+3][j+3] ==1:
            connected3player= 1
      
    elif grid[i][j]==2:
        if grid[i+1][j+1] == grid[i+2][j+2] == 2 and grid[i+3][j+3] ==0:
            connected3agent= 1
        elif grid[i+1][j+1] ==0 and  grid[i+2][j+2] == grid[i+3][j+3] ==2:
            connected3agent= 1
        elif grid[i+1][j+1] ==2 and grid[i+2][j+2] ==0 and grid[i+3][j+3] ==2:
            connected3agent= 1

    return connected4player,connected4agent,connected3player,connected3agent

def leftDiagonal4Or3(grid,i,j):
    connected4player=0
    connected4agent=0
    connected3player=0
    connected3agent=0

    #calculate no of connected 4's for the player
    if grid[i][j]== grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] == 1:
        connected4player= 1
    #calculate no of connected 4's for the agent    
    elif grid[i][j]== grid[i+1][j+-1] == grid[i+2][j-2] == grid[i+3][j-3] == 2:
        connected4agent= 1

    #check connected 3 cases
    elif grid[i][j]==0:
        if grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] ==1:
            connected3player= 1
        elif grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] ==2:
            connected3agent= 1
          
    elif grid[i][j]==1:
        if grid[i+1][j-1] == grid[i+2][j-2] == 1 and grid[i+3][j-3] ==0:
            connected3player= 1
        elif grid[i+1][j-1] ==0 and  grid[i+2][j-2] == grid[i+3][j-3] ==1:
            connected3player= 1
        elif grid[i+1][j-1] ==1 and grid[i+2][j-2] ==0 and grid[i+3][j-3] ==1:
            connected3player= 1
      
    elif grid[i][j]==2:
        if grid[i+1][j-1] == grid[i+2][j-2] == 2 and grid[i+3][j-3] ==0:
            connected3agent= 1
        elif grid[i+1][j-1] ==0 and  grid[i+2][j-2] == grid[i+3][j-3] ==2:
            connected3agent= 1
        elif grid[i+1][j-1] ==2 and grid[i+2][j-2] ==0 and grid[i+3][j-3] ==2:
            connected3agent= 1

    return connected4player,connected4agent,connected3player,connected3agent

