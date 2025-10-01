
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

size=9
mines=10
opened=0

grid = [[0 for _ in range(size)] for _ in range(size)]
grid_flag = [[0 for _ in range(size)] for _ in range(size)]
grid_hash = [['#' for _ in range(size)] for _ in range(size)]

def place_mines():
    temp=0

    while (temp<mines):
      tempr= random.randint(0, size-1)
      tempc= random.randint(0, size-1)
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

def place_numbers():

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
    global opened
    if row < 0 or col < 0 or row >= size or col >= size:
        return

    if grid_hash[row][col] != '#':
        return

    if grid[row][col] == 0:
        grid_hash[row][col] = '0'
        opened+=1
    else:
        grid_hash[row][col] = str(grid[row][col])
        opened+=1
        return

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr != 0 or dc != 0:
                check_mine(row + dr, col + dc)

def flag_set():
    print("Flag setting function")


def main():
    print("MINESWOOPER")
    for i in range(0, size):
        for j in range(0, size):
            print((grid_hash[i][j]), end=' ')
        print()

    place_mines()
    place_numbers()

    while(1):

        if(size*size-opened == mines):
            print("YOU WON! :)")
            break

        choice=input("Flag or Mine? (f/m): ")

        if(choice == "M" or choice=="m"):
            print("Mine")

            row= int(input(f"Enter Row Value (1-{size}): "))
            col= int(input(f"Enter Col Value (1-{size}): "))

            if(row>size or row<1 or col>size or col<1):
                print("Invalid number enter again")

            elif (grid_flag[row-1][col-1] == 1):
                print("Flagged!! try another cell")

            elif (grid[row-1][col-1] == '*'):
                print("GAME OVER :(")
                show_fullgrid()
                break

            else:
                check_mine(row-1, col-1)
                show_hashgrid()

        elif (choice == "F" or choice == 'f'):
            print("Flagging")
            frow = int(input(f"Enter Row Value (1-{size}): "))
            fcol = int(input(f"Enter Col Value (1-{size}): "))

            frow-=1
            fcol-=1

            if(grid_flag[frow][fcol]==0):
                grid_hash[frow][fcol]= "F"
                grid_flag[frow][fcol] =1

                show_hashgrid()

            else:
                print(f"Removed flag from {frow+1},{fcol+1}")
                grid_hash[frow][fcol] = "#"
                grid_flag[frow][fcol] = 0

                show_hashgrid()

        else:
            print("Invalid Character enter again!!!")


if __name__ == '__main__':
    main()