import random

# Hangman

'''
File read for english.txt
import words > 5 letters
display _'s
have a guess counter
keep track of guessed letters
add an addendum that only wrong guesses count 
whether they succeed or run out of guesses and ask if they want to play again
wants function load_words(path) so that will need to go into the file read
between the guess counter and guessed letters need to ask user to imput a letter
'''


# def load_words():
#     with open('code/mobs/hangman/english.txt', 'r') as file:
#         words = file.read().split('\n')

#     choices = []

#     for word in words:
#         if len(word) >= 5:
#             choices.append(word)
#     # print(choices)
#     return(choices)

# choices = load_words()
# word_to_guess = random.choice(choices)
# print(word_to_guess)

word_to_guess = 'otter'

holder = []

for letter in range(len(word_to_guess)):
    holder.append('_') 
blanks = ' '.join(holder)

print(blanks)


user_guesses = []
guess_count = 10


while True: 
    guesses = input("guess a letter: ")
    user_guesses.append(guesses)
    if guesses in word_to_guess:
        
        for letter in range(len(word_to_guess)):


    print(user_guesses, holder)
