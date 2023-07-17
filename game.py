import random
import requests

print('Hello and welcome to Shaun\'s Magnificent Guessing Game!')

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
    else:
        print(f'Nope, you are wrong! That guess was too low')
    guess = int(input('Enter another guess: '))

print(f'Yayyyyyy! The number was {number}')

print('Thank you for playing! We hope to see you again soon.')