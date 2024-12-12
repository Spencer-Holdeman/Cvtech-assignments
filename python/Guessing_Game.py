import random
import math

random_number = math.floor(random.random() * 100)
guess_boolean = False
retry_value = 'guess a number between 1 and 100!'

while guess_boolean == False:
    guess = int(input(retry_value))
    if guess > random_number:
        retry_value = 'Guess a lower number!' 
    if guess < random_number:
        retry_value = 'Guess a higher number!'   
    if guess == random_number:
        guess_boolean = True
        print('You Win!!!')    
