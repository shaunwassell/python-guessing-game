import random

number = random.randint(1, 10)
guess = int(input('I have selected a number between 1 and 10. Enter your guess: '))

if guess == number:
    print(f'You are correct! The number was {number}')
elif guess > number:
    print(f'Nope, you are wrong! That guess was too high')
else:
    print(f'Nope, you are wrong! That guess was too low')