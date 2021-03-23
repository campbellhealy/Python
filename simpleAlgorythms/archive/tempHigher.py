# Temp guess greater than 

# For Target being higher than current_guess
#     50 - last_guess h
#     75 - l
#     50 < next_guess < 75
    
#     last_guess < next_guess < current_gues
count = 1
guesses = [50]
target = 59
last_guess = 50
current_guess = 75
next_guess = 0

for count in range(10):
    if current_guess == target:
        count += 1
        print(f'\nHalver Search found the Correct Value {target} in {count} guesses.\n')
        break

    elif current_guess > target:
        count += 1
        print(f'{current_guess} is greater than target')
        print(f' This is guess number: {count}')
        # guesses.append(guess)
        last_guess = guesses[-1]

        next_guess = int(((current_guess - last_guess)/2) + last_guess)
        current_guess = next_guess


print(next_guess)