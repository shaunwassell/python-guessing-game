import random

mode = input('Select game mode (E/M/H): ')

if mode == 'E':
    number = random.randint(1, 5)
elif mode == 'M':
    number = random.randint(1, 10)
else:
    number = random.randint(1, 20)

guess = int(input('I have selected a number between 1 and 10. Enter your guess: '))

if guess == number:
    print(f'You are correct! The number was {number}')
else:
    print(f'Nope, you are wrong! The number was {number}')
