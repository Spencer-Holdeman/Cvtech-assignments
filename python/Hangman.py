import random
import math
import os

words = ['red', 'blue', 'green', 'apple', 'bananna', 'grapes', 'car', 'dog', 'animals', 'skibidi', 'computer']
random_word = words[math.floor(random.random() * len(words))]
lives = 2
hidden_word = []
guessed_words = []
os.system('cls')
for x in random_word:
    lives += 1
    hidden_word += '_'
print(' '.join(hidden_word).replace(' ', ''))

while True:
    print(f"Letters Guessed: {', '.join(guessed_words)}")
    guess_is_contained = False
    user_guess = input(f'you have {lives} lives left! Guess a letter:')
    guessed_words += user_guess
    y = 0
    for x in range(0, len(random_word)):
        if list(random_word)[y] == user_guess:
            hidden_word[y] = user_guess
            guess_is_contained += True
        y += 1
    if guess_is_contained == False:
        lives -= 1
    if ' '.join(hidden_word).replace(' ', '') == random_word:
        print(random_word)
        print('You Win!')
        break
    if lives < 1 :
        print(f'You Lose! The Word Was {random_word}')
        break
    print(' '.join(hidden_word).replace(' ', ''))        

 


