# Linear.py
'''
This function will go through each value starting at 1 until it finds the correct result.
Counting the number of times it has taken to reach the correct value
'''

def linear(value):
    count = 0
    guess = 1

    for count in range(1000):
        if count == value:
            print(f'\nLinear Search found the Correct Value {value} in {count} guesses.')
        else:
            count+= 1
    return guess, count


