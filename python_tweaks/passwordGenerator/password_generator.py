from random import choice, choices, random, randint, shuffle
from string import ascii_letters, digits, punctuation
import clipboard

# Password generator
pw = ("".join(choices(ascii_letters + digits + punctuation, k=16))) # Random choice of multiple (k) chars from string
print(pw)
print()
clipboard.copy(pw)
print("Password Copied to Clipboard")
print(input("Press Enter to Close"))