# main.py
# Control file for the others

'''
random.seed(a=None, version=2)¶
Initialize the random number generator.

random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
'''

from random import seed
from random import randint
from os import system

from linear import linear
from halver import halver

system('cls') # Just to clear console
# seed(1) #Gives repeatable values whilst testing

# generate a number of random numbers, using seed of one value for testing
value = randint(1,100) # The range can be changed to any integer range
# value = 100

print(f'Value: {value}') # So I know the expected target value, to ensure modules work

# Function Calls - Remark out either to test just one of them.
linear(value)
halver(value)
