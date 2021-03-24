# main.py
# Control file for the others

'''
random.seed(a=None, version=2)¶
Initialize the random number generator.

random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

The addition of a second dimension to the test is adding slightly more complexity.

This makes for a bit of additional information in the main.py but reuse of the other modules
is be possible for the second dimension. Reduxing the amount of coding.
'''

from random import seed
from random import randint
from os import system

from linear import linear
from binary import binary

system('cls') # Just to clear console
# seed(1) #Gives repeatable values whilst testing

# generate a number of random numbers, using seed of one value for testing
valueX = randint(1,100) # The range can be changed to any integer range
valueY = randint(1,100) # The range can be changed to any integer range

print(f'Target Values: ({valueX},{valueY})\n') # So I know the expected target co-ordinate, to ensure modules work

# Function Calls - Remark out either to test just one of them.
# This time rather than using the function to print out the results, I have set up main as I would normally do
# Yes, I was a bit lazy yesterday.

linearX, linearXCount = linear(valueX)
linearXCount = int(linearXCount)

linearY, linearYCount = linear(valueY)
linearYCount = int(linearYCount)

linearCount = linearXCount + linearYCount 
print('Linear Results: ')
print(f"Co-ordinates: ({linearX},{linearY}) Total Counts: ({linearCount})\n")
binaryX, binaryXCount = binary(valueX)
binaryXCount = int(binaryXCount)

binaryY, binaryYCount = binary(valueY)
binaryYCount = int(binaryYCount)

binaryCount = binaryXCount + binaryYCount
print('Binary Results: ')
print(f"Co-ordinates: ({binaryX},{binaryY}) Total Counts: ({binaryCount})\n")

