from string import ascii_letters

#ROT13

cypher_intake = list((input('Sentence please: ')))

rot_holder = []
rot_amount = 13

first_half_lower = ascii_letters[0:13]
second_half_lower = ascii_letters[13:26]
first_half_upper = ascii_letters[26:39]
second_half_upper = ascii_letters[39:]

for character in cypher_intake:
    if character in ascii_letters:
        if character.islower and character in first_half_lower:
            encryption = chr(ord(character) + rot_amount)
        elif character.islower and character in second_half_lower:
            encryption = chr(ord(character) - rot_amount)
        if character.isupper and character in first_half_upper:
            encryption = chr(ord(character) + rot_amount)
        elif character.isupper and character in second_half_upper:
            encryption = chr(ord(character) - rot_amount)
        rot_holder.append(encryption)
    else:
        rot_holder.append(character) #adds uncyphered if not alphabetical

cypher_output = ''.join(rot_holder)
print(cypher_output)