# Ryan Crop, Conditional notes python

#print("Hello, welcome to my program that will sort you into a catagory.")

#name = input("What is your name:\n")

#Two options, == checks if content is the same, === which check if the content and the data type is the same.

#if name == "Vienna":
    #print("Oh your the teacher .  .  . nevermind.")
#else:
    #print("You are a student. Welcome to class!")

#num = int(input("How many would you like:(give me a number above 0)\n"))
# Conditionals start at the top and then work there way down. They will only take the first correct statement. Starts with an if and ends with an else and everything inbetween is elif. Top of the if statements should be the lest likly outcome.
#if num == 1:
    #print("You have asked for a item.")
#elif conbines Else and if and just works as another if statement
#elif num <= 3:
    #print("You have asked for a couple of the item.")
#elif num <= 5:
    #print ("You have asked for a few of the item.  .  .or your in the south and you asked for a couple")
#else:
    #print("You have asked for some of the item.")


name = "Katie"
if "a" in name or "e" in name or "i" in name or "o" in name or "U" in name:
    print("Your name has a vowel!")
else: 
    print("Your name dosn't have a vowel.")