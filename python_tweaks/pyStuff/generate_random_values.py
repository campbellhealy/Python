from random import choice, choices, random, randint, shuffle
from string import ascii_letters, digits, punctuation

print(random()) # Random between 0 and 1
print(randint(1,20)) # Random int between the two stated values
print(choice([1,22,333,44,5555])) # Random choice of supplied values
print(choices([1,22,333,44,5555], k=2)) # Random choice of multiple (k) supplied values
print(choices("abcdefghij", k=4)) # Random choice of multiple (k) chars from string
print("".join(choices("0123456789", k=4))) # Random choice of multiple (k) chars from string
print("-".join(choices("0123456789", k=4))) # Random choice of multiple (k) chars from string, with seprator

# Password generator
print("".join(choices(ascii_letters + digits + punctuation, k=16))) # Random choice of multiple (k) chars from string

# Shuffler
numbers = [1,2,3,4,5,6,7,8,9,0]
shuffle(numbers)
print(numbers)
