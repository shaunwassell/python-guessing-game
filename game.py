import random

mode = input('Select game mode (E/M/H): ')

if mode == 'E':
    number = random.randint(1, 5)
    guess = int(input('I have selected a number between 1 and 5. What do you think it is???: '))
elif mode == 'M':
    number = random.randint(1, 10)
    guess = int(input('I have selected a number between 1 and 10. What do you think it is???: '))
else:
    number = random.randint(1, 20)
    guess = int(input('I have selected a number between 1 and 20. What do you think it is???: '))

while guess != number:
    if guess > number:
        print(f'Nope, you are wrong! That guess was too high')
    else:
        print(f'Nope, you are wrong! That guess was too low')
    guess = int(input('Enter another guess: '))

print(f'Yayyyyyy! The number was {number}')
