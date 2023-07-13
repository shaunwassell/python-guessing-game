import random

number = random.randint(1, 10)
guess = int(input('I have selected a number between 1 and 10. What do you think it is???: '))

while guess != number:
    print(f'Nope, you are wrong!')
    guess = int(input('Enter another guess: '))

print(f'Yayyyyyy! The number was {number}')