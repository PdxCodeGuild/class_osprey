#setup
from math import ceil
import string

#starting values
characters = 0
words = 0
sentences = 0


#file in
path = 'code\liam\python\lab06\spagettisburg.txt'

with open(path, 'r', encoding='utf-8') as file:
    contents = file.read()


#SENTENCE COUNT
for line in contents:
    if line == '.':
        sentences += 1
#WORD COUNT
    if line == ' ':
        words += 1
#CHARACTER COUNT
    if line in string.ascii_letters:
        characters += 1

#print(f'We counted {sentences} sentences, {characters} characters, and {words} words') 
#left line for test comparisions with other files

ari_calc = ( 4.71 * (characters / words) ) + ( 0.5 * (words / sentences)) - 21.43

ari_score = ceil(ari_calc) #ceiling rounds up

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

border = '\U0001F4DA \U0001F4D6 \U0001F4DA \U0001F4D6 \U0001F4DA \U0001F4D6 \U0001F4DA \U0001F4D6 \U0001F4DA \U0001F4D6 \U0001F4DA \U0001F4D6 '

print(f'''{border}{border}
\t\tThe ARI for this text is {ari_score}.
\tThis corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty,
 that is suitable for an average person of at least {ari_scale[ari_score]['ages']} years old.
{border}{border}''')