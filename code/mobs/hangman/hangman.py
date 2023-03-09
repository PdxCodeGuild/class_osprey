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


def load_words(path):
    with open('code\mobs\hangman\english.txt', 'r') as file:
        words = file.read().split('\n')

    choices = []

holder = []
singular_word = 'water'

for letter in range(len(singular_word)):
    holder.append('_') 
blanks = ' '.join(holder)




print(blanks)

