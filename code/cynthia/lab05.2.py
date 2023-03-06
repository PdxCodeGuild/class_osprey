#lab05.2

import string
string.ascii_lowercase

alphabet = list(string.ascii_lowercase)
cipher = list(string.ascii_lowercase)

user_input = input('What is your secret message?: ')
decrypted = (list(user_input))

rotation = int(input('Rotate the alphabet by: '))

encryption = cipher[(rotation):] + (cipher[:(rotation)])
print(encryption)

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

