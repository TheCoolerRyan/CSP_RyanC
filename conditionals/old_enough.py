# Ryan Crop, Old enough python
age = int(input("How old are you?\n"))
if age >= 18:
    print(f"Wow because your {age} you can vote, drive, get your learners permit, and go to school!\n") 
elif age < 18 & age >16:
    print(f"Sorry but because your only {age} years old, you can't vote, but you can drive, get your learners permit and go to school.\n")
elif age >15 & age < 18:
    print(f"Sense your {age} that means you can drive get your leanres permit and go to school but you cant vote!\n")
elif age == 15:
    print(f"Sorry but sense your only {age} you can't drive yet or vote, but you can get your learners permit and go to school.\n")
elif age > 14 & age < 16:
    print(f"Wow being {age} means you can get a Learners permit and go to school but you cant drive or vote!\n")
elif age < 15 & age >5:
    print(f"Sorry but sense your only {age} you can't get your learners permit drive or vote but you can go to school.\n")
elif age >= 5 & age <15:
    print(f"Wow, {age} is old enough that you can go to school, but you cant get your learners permit drive or vote!\n")
elif age <5:
    print(f"Sorry but {age} is not old enough to go to school, get your learners permit, drive, or vote.\n")
# Put in else statement