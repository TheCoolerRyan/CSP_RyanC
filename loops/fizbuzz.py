#Ryan Crop, FizzBuzz python
numbers = 0
while numbers >= 0 and numbers < 51:
    if numbers == (3 or 6 or 9 or 12 or 18 or 21 or  24 or 27 or 33 or 36 or 39 or 42 or 48):
        print("Fizz.\n")
    elif numbers == (5 or 10 or 20 or 25 or 35 or 40 or 50):
        print("Buzz.\n")
    elif numbers == (15 or 30 or 45):
        print("FizBuzz!!!\n")
    else:
        print(numbers)
    numbers += 1

# Fix varible with equation