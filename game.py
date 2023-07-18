import random
import requests

# Introduction
print("Welcome to Shaun's Magnificent Python Guessing Game! \nPrepare yourself for a thrilling challenge of guessing the secret number. \nAre you ready to put your intuition to the test? Choose your difficulty level and let's begin!\n")

# Score (equals the needed guesses)
wrong_guesses = 0

mode = input('Select game mode (E/M/H): ')

if mode == 'E':
    response = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=1&max=5&count=1')
    number = response.json()[0]
    guess = int(input('I have selected a number between 1 and 5. What do you think it is???: '))
elif mode == 'M':
    response = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1')
    number = response.json()[0]
    guess = int(input('I have selected a number between 1 and 10. What do you think it is???: '))
else:
    response = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=1&max=20&count=1')
    number = response.json()[0]
    guess = int(input('I have selected a number between 1 and 20. What do you think it is???: '))

while guess != number:
    if guess > number:
        print(f'Nope, you are wrong! That guess was too high')
        wrong_guesses += 1
    else:
        print(f'Nope, you are wrong! That guess was too low')
        wrong_guesses += 1

    guess = int(input('Enter another guess: '))

# Calculating the score based on the chosen difficulty (Upper boundary - wrong guesses)
if mode == 'E':
    score = 5 - wrong_guesses
elif mode == 'M':
    score = 10 - wrong_guesses
else:
    score = 20 - wrong_guesses

# Goodbye Message
print(f'\nCongratulations! You\'ve successfully guessed the secret number {number} with a score of {score}. \nYou\'re a true master of deduction! Thanks for playing the Number Guessing Game. \nFeel free to play again and see if you can beat a higher difficulty or get a higher score. Good luck!"')
