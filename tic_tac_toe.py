# Ryan Crop, Final project
grid = [['1','2','3'],
['4','5','6'],
['7','8','9']]


import random

game_finished = False

repeat = 1
taken_list = []

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
#Show grid after computer goes
    spot = int(input("pick a number for your spot 1-9 single digit please\n"))

    if spot in taken_list:
        print("That spot is taken.")
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
    for list in grid:
        print(f" {list[0]} | {list[1]} | {list[2]}\n --+---+--")
    grid = grid
# Figure out how to go back and continue the loop 

    #Create a taken list of user inputs so i can  say if random_integer == taken list, break