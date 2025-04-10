#Ryan Crop, Loop notes python
# 1 What is a loop? 
    # A section of code that is going to repeat.
# 2 What are the two types of loops?
    #While loop
x = 0
while x < 10:
    print("Hello", x)
    x += 1
    #for loop
nums = [3,5,7,2,8]
for num in nums:
    print(num)
# 3 What is iteration
    # The act of repeating
# 4 What are lists? 
    # A bunch of values in the same variable.
familys = ["Reese", "caden", "julia", "dad", "mom"]
#Print one item from the list
print(familys[2])
#change an item in a list
familys[2] = "Jules"
#remove an item from list
familys.pop(4)
# 5 How do you make lists in python? family = ["Reese", "caden", "julia", "dad", "mom"]
# 6 How do you make for loops in python? 
#proper list printing with a for loop
for family in familys:
    print(f"{num}. {family} Crop")
    num += 1

for num in range (1, 11, 3):
    #             num, num, How much it goes up by 
    print(num)
# 7 How do you make while loops in python?
import random

num = 1
rand = random.randint(1,20)
while num < 21:
    if num == rand:
        print("Goose!")
        break # Stops until finished
    else:
        print("Duck")
    num += 1

# continue tells the loop to stop that iteration and start over