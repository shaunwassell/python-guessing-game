import random

number = random.randint(1, 10)
guess = int(input('I have selected a number between 1 and 10. Enter your guess: '))

while guess != number:
    print(f'Nope, you are wrong!')
    guess = int(input('Enter another guess: '))

print(f'You are correct! The number was {number}')