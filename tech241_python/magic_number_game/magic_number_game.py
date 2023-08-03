# Magic number game
import random
# Set magic number
magic_num = random.randint(1, 10)

# Ask the user for a guess
guess = input('Guess my magic number between 1 & 10? ')

# Check if the user's guess was correct
valid_guesses = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'}
for num in range(1, 11):
    valid_guesses.add(str(num))


def guess_again():
    new_guess = input('That\'s not a number between 1 & 10, try again: ')
    return new_guess


while guess.lower() not in valid_guesses:
    guess = guess_again()

if not guess.isnumeric():
    word_nums = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    guess = str(word_nums.index(guess.lower()))

# Give them the result
if int(guess) == magic_num:
    print('You guessed my magic number, well done!')
elif int(guess) >= magic_num:
    print('You guessed too high, sorry.')
elif int(guess) <= magic_num:
    print('You guessed too low, sorry.')

print(magic_num)
