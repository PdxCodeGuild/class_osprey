import random
import string
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


def load_words():
    with open('code/mobs/hangman/english.txt', 'r') as file:
        words = file.read().split('\n')

    choices = []

    for word in words:
        if len(word) >= 5:
            choices.append(word)
    # print(choices)
    return(choices)

choices = load_words()

while True: 
    holder = []
    user_guesses = []
    guess_count = 10
    word_to_guess = random.choice(choices)
    for letter in range(len(word_to_guess)):
        holder.append('_') 
        blanks = ' '.join(holder)

    print(blanks)

    while True:
        guess = input("guess a letter: ").lower()
   
        if guess in word_to_guess:
            user_guesses.append(guess)
            for match in range(len(holder)):
                for letter in range(len(word_to_guess)):
                    if guess == word_to_guess[letter]:
                        holder[letter] = guess
                    
        
        elif guess in string.ascii_letters:
            user_guesses.append(guess)
            guess_count -= 1
        else:
            print("invalid guess.")
            continue
        print(f'''{holder}
guesses: {set(user_guesses)} 
guesses remaining: {guess_count}
''')
        if list(word_to_guess) == holder:
            print('you win!')
            break
        if guess_count == 0:
            print(f'you lost, the word was {word_to_guess}')
            break
    play_again = input("Would you like to play again?")
    if play_again == 'y':
        continue # TODO we need to move our random choice to game loop
    else:
        break