# Ryan Crop, Final project
grid = [['1','2','3'],
['4','5','6'],
['7','8','9']]
name = input("What is your name?\n")
print(f"Hello {name}. This is a game of tic tac toe but with a small extra rule.\n First the bot gets to go first because of how hard he works each day.\n Next is if you attempt to put your X on a spot already occupied, then you will get your turn skipped as punishment.")

import random

game_finished = False

repeat = 1
taken_list = []
def win(grid):

    if   grid[0][0] == "X" and grid[0][1]=="X" and grid[0][2]=="X":
         print("X wins")
         set(game_finished = True)
    elif grid[1][0] == "X" and grid[1][1]=="X" and grid[1][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[2][0] == "X" and grid[2][1]=="X" and grid[2][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][0] == "O" and grid[0][1]=="O" and grid[0][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[1][0] == "O" and grid[1][1]=="O" and grid[1][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[2][0] == "O" and grid[2][1]=="O" and grid[2][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][0] == "X" and grid[1][0]=="X" and grid[2][0]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][0] == "X" and grid[1][1]=="X" and grid[2][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][2] == "X" and grid[1][2]=="X" and grid[2][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][0] == "X" and grid[1][1]=="X" and grid[2][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][2] == "X" and grid[1][1]=="X" and grid[2][0]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][1] == "X" and grid[1][1]=="X" and grid[2][1]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][0] == "O" and grid[1][0]=="O" and grid[2][0]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][0] == "O" and grid[1][1]=="O" and grid[2][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][2] == "O" and grid[1][2]=="O" and grid[2][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][0] == "O" and grid[1][1]=="O" and grid[2][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][2] == "O" and grid[1][1]=="O" and grid[2][0]=="O":
        print("O wins")
        set(game_finished = True)
    elif all(spot in ["X", "O"] for row in grid for spot in row):
        print("It's a tie.")
        set(game_finished = True)
    return grid
while game_finished == False:
    random_integer = random.randint(1, 9)

    
    if random_integer in taken_list:
        continue
    else:
        taken_list.append(random_integer)
        if random_integer == 1:
            grid[0][0] ="O" 
        elif random_integer == 2: 
            grid[0][1] ="O"
        elif random_integer == 3: 
            grid[0][2] ="O"
        elif random_integer == 4: 
            grid[1][0] ="O"
        elif random_integer == 5: 
            grid[1][1] ="O"
        elif random_integer == 6: 
            grid[1][2] ="O"
        elif random_integer == 7: 
            grid[2][0] ="O"
        elif random_integer == 8: 
            grid[2][1] ="O"
        elif random_integer == 9: 
            grid[2][2] ="O"
        for list in grid:
            print(f" {list[0]} | {list[1]} | {list[2]}\n --+---+--")
        win(grid) 
        if game_finished == True:
            break
        else:
            print("")
    

    spot = int(input("pick a number for your spot 1-9 single digit please\n"))

    if spot in taken_list:
        print("That spot is taken, because you didn't listen to the rules your turn is skipped >:) !")
        continue
    else: 
        taken_list.append(spot)
        if spot == 1:
            grid[0][0]="X"
        elif spot == 2:
            grid[0][1] ="X"
        elif spot == 3:
            grid[0][2] ="X"
        elif spot == 4:
            grid[1][0]="X"
        elif spot == 5: 
            grid[1][1]="X"
        elif spot == 6:
            grid[1][2] ="X"
        elif spot == 7:
            grid[2][0] ="X"
        elif spot == 8:
            grid[2][1] ="X"
        elif spot == 9:
            grid[2][2] ="X"
    win(grid) # Make it so it checks who wins after O goes and after X goes. Also coppy and paste X straight down winning code and change it to O so the O code will work.
    if game_finished == True:
        break
    else:
        print("")
    
# Fix why O cant win