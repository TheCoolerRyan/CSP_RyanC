# Ryan Crop, Final project
#grid
grid = [[1,2,3],
[4,5,6],
[7,8,9]]


import random

game_finished = False

random_integer = random.randint(1, 9)

taken_list = []

while game_finished == False:

    if random_integer == taken_list:
        break
    else:
        taken_list.append(random_integer)
    if random_integer == 1:
        grid[0][0] = "O" 
    elif random_integer == 2: #Repeat for numbers one through nine and get updated graph from santiago
        break

for grid in grid:
    print(f" {grid[0]} | {grid[1]} | {grid[2]}")
    #Create a taken list of user inputs so i can  say if random_integer == taken list, break