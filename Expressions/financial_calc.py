#Ryan Crop, Finaincal calculator.py
money = input("How much money did you make this year?")
print("Okay")
loss = input("How much money did you spend this year?")
print("Got it.")
if money < loss:
    print("Will need to work on that.")
    rent = input("How much did you spend on Rent?")
    utilites = input("Okay, how much did you spend on utilites?")
    grocies = input("Got it, so how much did you spend on grocies?")
    transportation =input("And finally how much did you spend on transportation?")
    total_loss = (rent+utilites+grocies+transportation)
if money >= loss:
    print("Thats great!")
