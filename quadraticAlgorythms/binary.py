# binary.py
'''
This function will choose a value half way between the possible numbers.
If incorrect and lower, will choose half way between those values.
If incorrect and higher, will choose half way betwwe those values.
Counting the number of times it has taken to reach the correct value
'''

def binary(value):
    count = 0
    possibles = 100
    guess = int(possibles/2)
    last_guess = guess
    guesses = []

    for count in range(possibles):
        if value == guess:
            count += 1
            break      
        elif guess < value:
            count += 1
            guesses.append(guess)
            if len(guesses) == 1:
                last_guess = 0
            elif len(guesses) == 2:
                last_guess = guesses[-2]
            else:
                last_guess = guesses[-2]
            next_guess = int(guess + int((abs(last_guess - guess))/2) +1)
            guess = next_guess

        elif guess > value:
            count += 1
            guesses.append(guess)
            if len(guesses) == 1:
                last_guess = 0
            elif len(guesses) == 2:
                last_guess = guesses[-2]
            else:
                last_guess = guesses[-2]
            next_guess = int(guess - (int(abs(guess - last_guess))/2))
            guess = next_guess
    return guess,count
