# Ryan Crop, Final project
grid = [['1','2','3'],
['4','5','6'],
['7','8','9']]
name = input("What is your name?\n")
print(f"Hello {name}. This is a game of tic tac toe but with a small extra rule. If you attempt to put your X on a spot already occupied, then you will get your turn skipped as punishment.")

import random

game_finished = False

repeat = 1
taken_list = []
def win(grid):
    #Change the row win statements to the format of the diagnal and down code ex. if grid [0][0]== x.
    if grid[0]==["X","X","X"]:
        print("X wins")
        set (game_finsished = True)
    elif grid[1]==["X", "X", "X"]:
        print("X wins")
        set (game_finsished = True)
    elif grid[2]==["X", "X", "X"]:
        print("X wins")
        set (game_finsished = True)
    elif grid[0]==["O", "O", "O"]:
        print("O wins")
        set (game_finsished = True)
    elif grid[1]==["O", "O", "O"]:
        print("O wins")
        set (game_finsished = True)
    elif grid[2]==["O", "O", "O"]:
        print("O wins")
        set (game_finsished = True)
    elif grid[0][0] == "X" and grid[1][0]=="X" and grid[2][0]=="X":
        print("X wins")
        set (game_finsished = True)
    elif grid[0][1] == "X" and grid[1][2]=="X" and grid[2][3]=="X":
        print("X wins")
        set (game_finsished = True)
    elif grid[0][2] == "X" and grid[1][2]=="X" and grid[2][2]=="X":
        print("X wins")
        set (game_finsished = True)
    elif grid[0][0] == "X" and grid[1][1]=="X" and grid[2][2]=="X":
        print("X wins")
        set (game_finsished = True)
    elif grid[0][2] == "X" and grid[1][1]=="X" and grid[2][0]=="X":
        print("X wins")
        set (game_finsished = True)
    elif grid[0][0] == "O" and grid[1][0]=="O" and grid[2][0]=="O":
        print("O wins")
        set (game_finsished = True)
    elif grid[0][1] == "O" and grid[1][2]=="O" and grid[2][3]=="O":
        print("O wins")
        set (game_finsished = True)
    elif grid[0][2] == "O" and grid[1][2]=="O" and grid[2][2]=="O":
        print("O wins")
        set (game_finsished = True)
    elif grid[0][0] == "O" and grid[1][1]=="O" and grid[2][2]=="O":
        print("O wins")
        set (game_finsished = True)
    elif grid[0][2] == "O" and grid[1][1]=="O" and grid[2][0]=="O":
        print("O wins")
        set (game_finsished = True)
    elif grid[0][0] == ("X" or "O") and grid[0][1] == ("X" or "O") and grid[0][2] == ("X" or "O") and grid[1][0] == ("X" or "O") and grid[1][1] == ("X" or "O") and grid[1][2] == ("X" or "O") and grid[2][0] == ("X" or "O") and grid[2][1] == ("X" or "O") and grid[2][2] == ("X" or "O"):
            print("Its a tie.")
            set (game_finsished = True)
    else:
        print("Yo.")
while game_finished == False:
    random_integer = random.randint(1, 9)

    
    if random_integer in taken_list:
        continue
    else:
        taken_list.append(random_integer)
        if random_integer == 1:
            grid[0][0] = "O" 
        elif random_integer == 2: 
            grid[0][1] = "O"
        elif random_integer == 3: 
            grid[0][2] = "O"
        elif random_integer == 4: 
            grid[1][0] = "O"
        elif random_integer == 5: 
            grid[1][1] = "O"
        elif random_integer == 6: 
            grid[1][2] = "O"
        elif random_integer == 7: 
            grid[2][0] = "O"
        elif random_integer == 8: 
            grid[2][1] = "O"
        elif random_integer == 9: 
            grid[2][2] = "O"
        for list in grid:
            print(f" {list[0]} | {list[1]} | {list[2]}\n --+---+--")

    spot = int(input("pick a number for your spot 1-9 single digit please\n"))

    if spot in taken_list:
        print("That spot is taken, because you didn't listen to the rules your turn is skipped >:) !")
        continue
    else: 
        taken_list.append(spot)
        if spot == 1:
            grid[0][0]="X"
        elif spot == 2:
            grid[0][1]  ="X"
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
    grid = grid
    win(grid)
    
    
# Figure out how to go back and continue the loop 

    #Create a taken list of user inputs so i can  say if random_integer == taken list, break