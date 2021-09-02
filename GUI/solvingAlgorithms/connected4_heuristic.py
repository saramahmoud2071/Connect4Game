LENGTH, WIDTH = 8, 8

""" Calculating Heuristic values for terminal states """

def calculateHeuristic(nodegrid, humanScore, agentScore):
  # q: number of connected 4's of the human
  # w: number of connected 4's of the agent
  # e: number of connected 3's of the human
  # r: number of connected 3's of the agent
  # so heuristic equals w+r-q-e
  heuristic=0
  for i in range (0,LENGTH):
    for j in range (0,WIDTH):

      #get no of connected 4 & 3 horizontally for both players
      if j in range (0,WIDTH-3):
        q,w,e,r=horizontal4Or3(nodegrid,i,j)
        heuristic=heuristic+w+r-q-e
        
      #get no of connected 4 & 3 vertically for both players
      if i in range (3,8):
        q,w,e,r=vertical4Or3(nodegrid,i,j)
        heuristic=heuristic+w+r-q-e

      #get no of connected 4 & 3 diagonally for both players
      if i in range(0,LENGTH-3):
        if j in range (0,WIDTH-3):
          q,w,e,r=rightDiagonal4Or3(nodegrid,i,j)
          heuristic=heuristic+w+r-q-e

        if j in range (3,8):
          q,w,e,r=leftDiagonal4Or3(nodegrid,i,j)
          heuristic=heuristic+w+r-q-e
          
  #make the actual score weight equal 1
  heuristic= heuristic-9*agentScore+9*humanScore 
  return heuristic


def horizontal4Or3(grid,i,j):
  connected4player=0
  connected4agent=0
  connected3player=0
  connected3agent=0

  if grid[i][j]== grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 0:
    return 0,0,0,0

  #connected 4's for the human
  if grid[i][j]== grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 1:
    connected4player= 10
  #calculate no of connected 4's for the agent    
  elif grid[i][j]== grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 2:
    connected4agent= 10


  #check connected 3 cases
  elif grid[i][j]==0 and grid[i+1][j]!=0 if i+1 < LENGTH else True :
    if grid[i][j+1] == grid[i][j+2] == grid[i][j+3] ==1:
      connected3player= 1
    elif grid[i][j+1] == grid[i][j+2] == grid[i][j+3] ==2:
      connected3agent= 1

  elif grid[i][j]==1: 
    if grid[i][j+1] == grid[i][j+2] == 1 and grid[i][j+3] ==0 and grid[i+1][j+3]!=0 if i+1 < LENGTH else True :
      connected3player= 1
    elif  grid[i][j+1] ==0 and  grid[i][j+2] == grid[i][j+3] ==1 and grid[i+1][j+1] !=0 if i+1 < LENGTH else True :
      connected3player=1
    elif  grid[i][j+1] ==1 and grid[i][j+2] ==0 and grid[i][j+3] ==1 and grid[i+1][j+2] !=0 if i+1 < LENGTH else True :
      connected3player= 1   
        
  elif grid[i][j]==2: 
    if grid[i][j+1] == grid[i][j+2] == 2 and grid[i][j+3] ==0 and grid[i+1][j+3] !=0 if i+1 < LENGTH else True  :
      connected3agent= 1
    elif  grid[i][j+1] ==0 and  grid[i][j+2] == grid[i][j+3] ==2 and  grid[i+1][j+1] !=0 if i+1 < LENGTH else True :
      connected3agent=1
    elif grid[i][j+1] ==2 and grid[i][j+2] ==0 and grid[i][j+3] ==2 and grid[i+1][j+2] !=0 if i+1 < LENGTH else True :
       connected3agent= 1

  return connected4player,connected4agent,connected3player,connected3agent


def vertical4Or3(grid,i,j):
  connected4player=0
  connected4agent=0
  connected3player=0
  connected3agent=0

  if grid[i][j]== grid[i-1][j] == grid[i-2][j] == grid[i-3][j] == 0:
      return 0,0,0,0

  #calculate no of connected 4's for the player
  if grid[i][j]== grid[i-1][j] == grid[i-2][j] == grid[i-3][j] == 1:
      connected4player= 10
  #calculate no of connected 4's for the agent    
  elif grid[i][j]== grid[i-1][j] == grid[i-2][j] == grid[i-3][j] == 2:
      connected4agent= 10
 
  #check connected 3 cases
  elif grid[i][j]==0 and grid[i+1][j]!=0  if i+1 < LENGTH else True :
    if grid[i-1][j] == grid[i-2][j] == grid[i-3][j] ==1:
      connected3player= 1
    elif grid[i-1][j] == grid[i-2][j] == grid[i-3][j] ==2:
      connected3agent= 1
          
  elif grid[i][j]==1:
    if grid[i-1][j] == grid[i-2][j] == 1 and grid[i-3][j] ==0 and grid[i-3+1][j] !=0 if i-3+1 < LENGTH else True  :
      connected3player= 1
    elif grid[i-1][j] ==0 and  grid[i-2][j] == grid[i-3][j] ==1 and grid[i-1+1][j] !=0 if i-1+1 < LENGTH else True :
      connected3player= 1
    elif grid[i-1][j] ==1 and grid[i-2][j] ==0 and grid[i-3][j] ==1 and grid[i-2+1][j] !=0 if i-2+1 < LENGTH else True :
      connected3player= 1
      
  elif grid[i][j]==2:
    if grid[i-1][j] == grid[i-2][j] == 2 and grid[i-3][j] ==0 and grid[i-3+1][j] !=0 if i-3+1 < LENGTH else True :
      connected3agent= 1
    elif grid[i-1][j] ==0 and  grid[i-2][j] == grid[i-3][j] ==2 and grid[i-1+1][j] !=0 if i-1+1 < LENGTH else True :
      connected3agent= 1
    elif grid[i-1][j] ==2 and grid[i-2][j] ==0 and grid[i-3][j] ==2 and grid[i-2+1][j] !=0 if i-2+1 < LENGTH else True :
      connected3agent= 1

  return connected4player,connected4agent,connected3player,connected3agent

def rightDiagonal4Or3(grid,i,j):
  connected4player=0
  connected4agent=0
  connected3player=0
  connected3agent=0

  if grid[i][j]== grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == 0:
      return 0,0,0,0

  #calculate no of connected 4's for the player
  if grid[i][j]== grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == 1:
      connected4player= 10
  #calculate no of connected 4's for the agent    
  elif grid[i][j]== grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == 2:
      connected4agent= 10

  #check connected 3 cases
  elif grid[i][j]==0 and grid[i+1][j]!=0 if i+1 < LENGTH else True :
    if grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] ==1:
      connected3player= 1
    elif grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] ==2:
      connected3agent= 1
          
  elif grid[i][j]==1:
    if grid[i+1][j+1] == grid[i+2][j+2] == 1 and grid[i+3][j+3] ==0 and grid[i+3+1][j+3] !=0 if i+3+1 < LENGTH else True :
      connected3player= 1
    elif grid[i+1][j+1] ==0 and  grid[i+2][j+2] == grid[i+3][j+3] ==1 and grid[i+1+1][j+1] !=0 if i+1+1 < LENGTH else True :
      connected3player= 1
    elif grid[i+1][j+1] ==1 and grid[i+2][j+2] ==0 and grid[i+3][j+3] ==1 and grid[i+2+1][j+2] !=0 if i+2+1 < LENGTH else True :
      connected3player= 1
      
  elif grid[i][j]==2:
    if grid[i+1][j+1] == grid[i+2][j+2] == 2 and grid[i+3][j+3] ==0 and grid[i+3+1][j+3] !=0 if i+3+1 < LENGTH else True :
      connected3agent= 1
    elif grid[i+1][j+1] ==0 and  grid[i+2][j+2] == grid[i+3][j+3] ==2 and grid[i+1+1][j+1] !=0 if i+1+1 < LENGTH else True :
      connected3agent= 1
    elif grid[i+1][j+1] ==2 and grid[i+2][j+2] ==0 and grid[i+3][j+3] ==2 and grid[i+2+1][j+2] !=0 if i+2+1 < LENGTH else True :
      connected3agent= 1

  return connected4player,connected4agent,connected3player,connected3agent

def leftDiagonal4Or3(grid,i,j):
  connected4player=0
  connected4agent=0
  connected3player=0
  connected3agent=0

  if grid[i][j]== grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] == 0:
      return 0,0,0,0

  #calculate no of connected 4's for the player
  if grid[i][j]== grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] == 1:
      connected4player= 10
  #calculate no of connected 4's for the agent    
  elif grid[i][j]== grid[i+1][j+-1] == grid[i+2][j-2] == grid[i+3][j-3] == 2:
      connected4agent= 10

  #check connected 3 cases
  elif grid[i][j]==0 and grid[i+1][j]!=0 if i+1 < LENGTH else True :
    if grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] ==1:
      connected3player= 1
    elif grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] ==2:
      connected3agent= 1
          
  elif grid[i][j]==1:
    if grid[i+1][j-1] == grid[i+2][j-2] == 1 and grid[i+3][j-3] ==0 and grid[i+3+1][j-3] !=0 if i+3+1 < LENGTH else True  :
      connected3player= 1
    elif grid[i+1][j-1] ==0 and  grid[i+2][j-2] == grid[i+3][j-3] ==1 and  grid[i+1+1][j-1] !=0 if i+1+1 < LENGTH else True :
      connected3player= 1
    elif grid[i+1][j-1] ==1 and grid[i+2][j-2] ==0 and grid[i+3][j-3] ==1 and grid[i+2+1][j-2] !=0 if i+2+1 < LENGTH else True :
      connected3player= 1
      
  elif grid[i][j]==2:
    if grid[i+1][j-1] == grid[i+2][j-2] == 2 and grid[i+3][j-3] ==0 and grid[i+3+1][j-3] !=0 if i+3+1 < LENGTH else True :
      connected3agent= 1
    elif grid[i+1][j-1] ==0 and  grid[i+2][j-2] == grid[i+3][j-3] ==2 and grid[i+1+1][j-1] !=0 if i+1+1 < LENGTH else True :
      connected3agent= 1
    elif grid[i+1][j-1] ==2 and grid[i+2][j-2] ==0 and grid[i+3][j-3] ==2 and grid[i+2+1][j-2] !=0 if i+2+1 < LENGTH else True  :
      connected3agent= 1

  return connected4player,connected4agent,connected3player,connected3agent
