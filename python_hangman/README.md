# python_hangman

### I made improvments to code I found in a Tutorial
There were a lot of things that I didn't like about the code.

#### The Main issue that got me hooked on this project
- Only letters from the word that were found would flag a duplicate if used again and there was no further usage of that letter in the word. This meant if a letter not used in the word was guessed more than once the count of failed attempts would decrement increase.

- Removed the decrement of repeated wrong guesses
- Inform the user that the wrong guess was repeated, showing the repeat to the user

- Changes to the wording presented to the user as I felt it lacked something

- The removal of the time import  was contemplated but I kept it is for a little delay just prior to the  wrong guess.
The time delays were removed from the user signs in process, as I found them too long and not required.

- There was a bit of concatenation removed and replaced with f strings to make it easier on the eye


The list already_guessed was split into two variables.
- correct_guesses, used to hold only the guesses the user got correct. This is used at the end of a failed game in presenting the correct answer
- wrong_guess_list, to hold only the wrong guesses, this is used to manage repeated failed guesses
Management of these lists was required to ensure the lists were accurate at the points required.

- The original graphic wasn't granular enough across the amount of guesses, these were adjusted.

- Last part, remove as much of the repeating code as possible, keeping the game in a single module and simple to understand.


### Improvements that could still be applied

- The most glaring point, changes to how the random word is chosen. 
A bigger selection of words, making levels,  ie 4 letters, 5 letters or 6 letters.
This could be implemented at the sign in stage, with three lists and a selection variable.

- Added a test.py file with only headers to possible tests to make me think over issues rather than code the tests.
