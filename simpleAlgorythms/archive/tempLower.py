# temp guess lower than

# For Target being lower than current_guess
#     50 - last_guess l
#     25 - h 
#     25 < next_guess < 50

#

count = 1
guesses = [50]
target = 37
last_guess = 50
current_guess = 25
next_guess = 0

for count in range(10):
    if current_guess == target:
        count += 1
        print(f'\nHalver Search found the Correct Value {target} in {count} guesses.\n')
        break

    elif current_guess < target:
        count += 1
        print(f'{current_guess} is lower than target')
        print(f' This is guess number: {count}')
        # guesses.append(guess)
        last_guess = guesses[-1]

        next_guess = int(((last_guess - current_guess)/2) + current_guess)
        current_guess = next_guess


print(next_guess)