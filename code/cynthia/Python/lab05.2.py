#lab05.2

import string
string.ascii_lowercase

alphabet = string.ascii_lowercase


user_input = input('What is your secret message?: ').lower()
decrypted = user_input

rotation = int(input('Rotate the alphabet by: '))


encrypted = ''
for chr in user_input:
    index = alphabet.index(chr) 
    encrypted = encrypted + alphabet[(index + rotation) % 26] 
print(encrypted)
