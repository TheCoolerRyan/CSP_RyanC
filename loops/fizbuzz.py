#Ryan Crop, FizzBuzz python
numbers = 0
while numbers >= 0 and numbers < 51:
    if numbers % 15 == 0:
        print("FizBuzz!!!\n")
    elif numbers % 5 == 0:
        print("Buzz.\n")
    elif numbers % 3 == 0:
        print("Fizz.\n")
    else:
        print(numbers)
    numbers += 1
