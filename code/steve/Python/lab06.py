#ARI 
from string import ascii_letters
import math
relative_path = 'code/steve/Python/abe_speech.txt'
with open(relative_path, 'r') as file:
   document = file.read()

#document = input("write a sentence: ")

word_count = len(document.split())

characters = list(document)

character_count = 0
for character in characters:
   
    if character in ascii_letters:
        character_count +=1 


sentence_count = (len(document.split(".")) - 1) + (len(document.split("!")) - 1) + (len(document.split("?")) - 1)



ari = 4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
if ari > 14:
    ari == 14
ari = math.ceil(ari)
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

grade = ari_scale[ari]['grade_level']
age = ari_scale[ari]['ages']

print(f'The ARI for {relative_path} is {ari}.\nThis corresponds to a {grade} level of difficulty\nthat is suitable for an average person {age} years old.')