
'''
grid[row][col]

mine- true/false                    '*'
adj- number of mines around it
hidden -true/false, visible or not, '#'
flagged- true/false

functions:
place_mines() → randomly place mines in the grid.
calculate_adjacency() → count neighbors for each non-mine cell.
reveal(r, c) → change cell state and flood-fill zeros.
flag(r, c) -> toggle flags
'''
import random

size=10
#rowzero = ['0' , '0','0','0','0','0','0','0']
#grid=[ rowzero, rowzero, rowzero, rowzero, rowzero, rowzero, rowzero, rowzero]
grid = [[0 for _ in range(size)] for _ in range(size)]
grid_hash = [['#' for _ in range(size)] for _ in range(size)]

print("MINESWOOPER")
for i in range(0,size):
    for j in range(0,size):
        #print('# ', end='')
        #grid_num = random.randint(0, 8)
        #grid[i][j]=grid_num
        print((grid_hash[i][j]), end=' ')
    print()

def place_mines():
    #print("place mines function")
    count=10
    temp=0

    while (temp<count):
      tempr= random.randint(0, 7)
      tempc= random.randint(0, 7)
      #print(tempr, tempc)
      if grid[tempr][tempc] != '*':
          grid[tempr][tempc]= '*'
          temp+=1

'''
    #printing mines list
    for i in range(0,size):
        for j in range(0,size):
            print(grid[i][j], end=' ')
        print()
'''

def show_fullgrid():
    for i in range(0,size):
        for j in range(0,size):
            print(grid[i][j], end=' ')
        print()

def show_hashgrid():
    for i in range(0, size):
        for j in range(0, size):
            print((grid_hash[i][j]), end=' ')
        print()

place_mines()

def place_numbers():
    #print("place numbers function")

    for i in range(0, size):
        for j in range(0, size):
            if(grid[i][j]=='*'):

                #if(i== 0 or j == 0 or i== 7 or j == 7):
                #    continue
                #else:
                    for tempr in range(i-1, i+2):
                        for tempc in range(j-1, j+2):
                            if (tempr == -1 or tempc == -1 or tempr == size or tempc == size ):
                                continue
                            if grid[tempr][tempc] == '*':
                                continue
                            else:
                                grid[tempr][tempc] = grid[tempr][tempc]+1
'''
    for i in range(0, size):
        for j in range(0, size):
            print(grid[i][j], end=' ')
        print()
'''

place_numbers()

'''
def check_mine(row, col):
    print("in the checking function")

    if(grid[row][col] == 0):
        #grid_hash[row][col]= grid[row][col]

        for chrow in range(row-1, row+2):
            for chcol in range(col-1, col+2):

                if (chrow == -1 or chcol == -1 or chrow == 8 or chcol == 8):
                    continue

                if(grid[chrow][chcol] == 0):
                    check_mine(chrow, chcol)

                elif(grid[chrow][chcol] != 0):
                    grid_hash[chrow][chcol]= grid[chrow][chcol]
                    return

    #display after opening all 0

'''

def check_mine(row, col):
    if row < 0 or col < 0 or row >= size or col >= size:
        return

    # Stop if already revealed
    if grid_hash[row][col] != '#':
        return

    # Reveal the current cell
    if grid[row][col] == 0:
        grid_hash[row][col] = '0'
    else:
        grid_hash[row][col] = str(grid[row][col])
        return  # Stop if it's a number (not 0)

    # Recurse to neighbors if 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr != 0 or dc != 0:
                check_mine(row + dr, col + dc)


while(1):
    row= int(input(f"Enter Row Value (1-{size}): "))
    col= int(input(f"Enter Col Value (1-{size}): "))

    if(row>size or row<1 or col>size or col<1):
        print("Invalid number enter again")

    elif (grid[row - 1][col - 1] == '*'):
        print("GAMEEEEEEEEEEEE OVERRRRRRRRRRRRRRRR :((((((((((((((((((((((((((")
        print("GAMEEEEEEEEEEEE OVERRRRRRRRRRRRRRRR :((((((((((((((((((((((((((")
        print("GAMEEEEEEEEEEEE OVERRRRRRRRRRRRRRRR :((((((((((((((((((((((((((")
        print("GAMEEEEEEEEEEEE OVERRRRRRRRRRRRRRRR :((((((((((((((((((((((((((")
        print("GAMEEEEEEEEEEEE OVERRRRRRRRRRRRRRRR :((((((((((((((((((((((((((")
        #thanku Canononononononn
        show_fullgrid()
        break

    else:
        #print("hi")
        check_mine(row-1, col-1)
        show_hashgrid()