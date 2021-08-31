HUMAN = False
COMPUTER = True

def horizontal4(grid, player, i, j):

  if player == HUMAN:
    if grid[i][j]== grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 1:
       return 1

  else:
    if grid[i][j]== grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == 2:
      return 1    

  return 0
  

def vertical4(grid, player, i, j):
   
   if player == HUMAN:
     if grid[i][j]== grid[i-1][j] == grid[i-2][j] == grid[i-3][j] == 1:
       return 1
       
   else:
      if grid[i][j]== grid[i-1][j] == grid[i-2][j] == grid[i-3][j] == 2:
        return 1

   return 0
 

def rightDiagonal4(grid, player, i, j):

  if player == HUMAN:
    if grid[i][j]== grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == 1:
      return 1

    elif grid[i][j]== grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == 2:
      return 1

  return 0


def leftDiagonal4(grid, player, i, j):
  
  if player == HUMAN:
    if grid[i][j]== grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] == 1:
      return 1

  else:
    if grid[i][j]== grid[i+1][j+-1] == grid[i+2][j-2] == grid[i+3][j-3] == 2:
      return 1

  return 0
