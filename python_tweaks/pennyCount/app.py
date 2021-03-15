# app.py
"""
Guess the Number of pennies in a jar.
The values are set in the cinstants  file and imported to separate this from
the workings of the app.

The default values:
Pennies equals an int between 1 to 100 inclusive
Guesses limit is set to 5

"""
from constants import (
    actual_pennies,
    number_of_guesses,
    player_guess,
    maximum_guess_limit,
)

# Variables: Changed the name into a smaller word for ease of writing only, the verbose name
# has been put in the constants.py for clarity
pennies = actual_pennies

# Header
print(" ")
print("---------------------------------")
print("   Guess the number of pennies ")
print("--- Value between 1 and 100 -----")
print("----------------------------------")
print(" ")
print(" ")


while number_of_guesses < maximum_guess_limit:
    number_of_guesses += 1
    player_guess = int(input(f"Take guess {number_of_guesses}: "))

    if player_guess == pennies:
        print(f"Well done, your guess of {player_guess} was correct!")
        break
    elif player_guess < pennies:
        print(f"Sorry that guess of {player_guess} was too low, try again")
    elif player_guess > pennies:
        print(f"Sorry that guess of {player_guess} was too high, try again")
else:
    print(f"All {number_of_guesses} have been used,")
    print(f"the correct values was {pennies}")
    print(" ")

# Exit Game
print("Thanks for Playing!")


# print(pennies)
# print(number_of_guesses)
# print(player_guess)
