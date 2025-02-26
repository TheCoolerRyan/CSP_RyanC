# Ryan Crop, Old enough python
age = int(input("How old are you?\n"))
if age >= 18:
    print(f"Wow because your {age} you can vote!\n")
    if age >=16:
        print(f"Sense your {age} that means you can drive!\n")
        if age >= 15:
            print(f"Wow being {age} means you can get a Learners permit!\n")
            if age >= 5:
                print(f"Wow, {age} is old enough that you can go to school!\n")
            else:
                print(f"Sorry but {age} is not old enough to go to school.\n")
        else:
            print(f"Sorry but sense your only {age} you can't get your learners permit.\n")

    else:
        print(f"Sorry but sense your only {age} you can't drive yet.\n")
else:
    print(f"Sorry but because your only {age} years old, you can't vote yet.\n")


#Put highest age at the top and its else at the bottom.