# Lab 06 TAKE TWO

import string
string.punctuation

with open ('code/cynthia/gettysburg_address.txt', 'r') as file:
    contents = file.read()

sentances = contents.count('.')

for character in string.punctuation:
    contents = contents.replace(character, '')

text_as_list = contents.split()
word_count = len(text_as_list)

contents = contents.replace(" ",'')
character_count = len(contents) 

input_number = round(4.71*(character_count/word_count) + 0.5*(word_count/sentances) -21.43)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

if input_number <= 14:
    ari_scale.get(input_number)
    print(f'The ARI for {file} is {input_number}')
    print(f"This corresponds to a {ari_scale.get(input_number)['grade_level']} level of difficulty")
    print(f"that is suitable for an everage perosn {ari_scale.get(input_number)['ages']} years old")
else:
    print(f'The ARI for {file} is 14')
    print(f"This corresponds to a College level of difficulty")
    print(f"that is suitable for an average person 18-22 years old.")