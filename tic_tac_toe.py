# Ryan Crop, Final project
grid = [[1,2,3],
[4,5,6],
[7,8,9]]


import random

game_finished = False


taken_list = []

while game_finished == False:
    random_integer = random.randint(1, 9)

    if random_integer == taken_list:
        break
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
        break


for grid in grid:
    print(f" {grid[0]} | {grid[1]} | {grid[2]}\n --+---+--")
    #Create a taken list of user inputs so i can  say if random_integer == taken list, break