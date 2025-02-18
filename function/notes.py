# Ryan Crop, Function Notes in python

#Function is an action stored in a keyword

#snake_Case = no capitals, underscores instead of spaces
#camalCase = removes spaces, any word AFTER the 1st starts with a capital 
#number = int(input("Tell me a number:\n"))
#def add(numOne, numTwo): #Parameters go in the parenthesis seperated by commas
    #print(numOne+numTwo)

#add(number,20)#Arguments are given when the function is called and must match the number of parameters

def user(word):
   return input(f"Tell me a {word}:\n")

name = user("name")
verb = user("verb")
place = user("place")
print(f"{name} was {verb} and somehow got to {place}")


