import random
import time

# Add your name
print("\nHangman\n")
name = input("Enter your name: ")
print(f"Hi {name}, are you ready!")

# I found these variable should be placed outwith the methods
correct_guesses = []
wrong_guess_list = []

def main():
    '''
    This sets up the variable but I don't see why the method should be called main
    I would be looking to expand on the words_to_guess and separate this into a seperate txt/module file
    '''
    global count, display, wrong_guess_list, word, correct_guesses, length, play_game
    words_to_guess = [
        "january",
        "border",
        "image",
        "film",
        "promise",
        "kids",
        "lungs",
        "doll",
        "rhyme",
        "damage",
        "plants",
    ]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    play_game = ""


def play_loop():
    ''' 
    This def: 
    If the user wants to play again they do not need to retype their name
    If the user doesn't want to play again there is a nice farewell message
    '''
    global play_game
    play_game = input("Play again? (y)es/(n)o \n")
    play_game = play_game.lower()
    while play_game not in ["y", "n"]:
        play_game = input("Play again? (y)es/(n)o \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print(f"Thanks For Playing! \nCome back sometime {name}!\n")
        exit()


def hangman():
    '''
    This method is the main part of the game.
    With the variables setup in main()
    This method takes the input from the user and passes it through the various components
    to determine if the guess is a letter in the random word
    '''
    global count, display, word, correct_guesses, play_game, wrong_guess_list

    limit = 5
    guess = input(f"Enter your Guess: {display} \n").strip()
    correct_guesses.append(guess)
    wrong_guess_list = correct_guesses[:-1]

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Must be a letter\n")
        hangman()

    elif guess in word:
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1 :]
        display = display[:index] + guess + display[index + 1 :]
        print(display + "\n")
        wrong_guess_list = wrong_guess_list[:-1]


    elif guess in wrong_guess_list:
        print(f"You have already guessed ({guess})\n")
        correct_guesses = correct_guesses[:-1]

    else:
        count += 1
        time.sleep(1)
        correct_guesses = correct_guesses[:-1]

        if count == 1:
            print(
                "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )

        elif count == 2:
            print(
                "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     |\n"
                "  |     O\n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )

        elif count == 3:
            print(
                "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |     | \n"
                "  |      \n"
                "__|__\n"
            )

        elif count == 4:
            print(
                "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |        \n"
                "__|__\n"
            )
        print(f"Wrong guess. {str(limit - count)} guesses remaining\n")

        if count == 5:
            # time.sleep(1)
            print(
                "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n"
            )
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", correct_guesses, word)
            play_loop()

    if word == "_" * length:
        print(f"Congrats {name}!\nYou have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()