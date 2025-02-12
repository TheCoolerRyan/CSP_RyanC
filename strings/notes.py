#Ryan Crop, Strings Notes python.

#words in programing (data type)

name = input("What is your name?(First name only please.)\n").strip().capitalize()
print(f"Hello {name} welcome to my programe.")

sentence = "the quick brown fox jumps over the lazy dog."
word = sentence.find("fox")
#print (sentence[4:9])
#print(len(sentence))
#name = "Ryan"
#print(f"Welcome to the program {name}!")
percent = 89
print(f"Your grade is {percent:.1f}")
# F strings are   print(f"words {variable}!")