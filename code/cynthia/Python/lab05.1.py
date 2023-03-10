 #lab05 ROT Cipher
#Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string.
#Notice that there are 26 letters in the English language, so encryption is the same as decryption.

import string
string.ascii_lowercase

alphabet = list(string.ascii_lowercase)
cipher = list(string.ascii_lowercase)

encryption = cipher[-13:] + (cipher[:13])


user_input = input('What is your secret message?: ')
decrypted = (list(user_input))


decrypted_index= []
for value in decrypted:
    decrypted == alphabet
    decrypted_index.append(alphabet.index(value))
# print(decrypted_index)

secret_message = []
for i in decrypted_index:
    decrypted_index == encryption
    secret_message.append(encryption[i])

print(' '.join(secret_message))