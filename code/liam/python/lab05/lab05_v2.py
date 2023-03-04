from string import ascii_letters

#ROT13

cypher_intake = list((input('Sentence please: ')))

while True:
    rot_amount = int(input('How many rotations: '))
    if rot_amount == 0:
        print('Must be at least 1.')
        continue
    break

rot_holder = []

first_half_lower = ascii_letters[0:(26 - rot_amount)]
second_half_lower = ascii_letters[(26 - rot_amount):26]
first_half_upper = ascii_letters[26:(52 - rot_amount)] 
second_half_upper = ascii_letters[(52 - rot_amount):] 

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