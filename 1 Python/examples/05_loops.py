from random import choice

'''
You can loop over any iterable type
iterables: list, string, tuple, dictionary
(and some other weird things like file objects, ranges, etc)
'''

# looping over a list
for color in ['red', 'green', 'blue']:
    print(f'I love {color}')


# looping over a dictionary

class_osprey = {
    'instructor': 'Danny',
    'TA': 'James',
    'student_count': 3,
    'grad_date': 'June 9'
}

for thing in class_osprey:
    print(f'{thing} -- {class_osprey[thing]}')

# use .items() to turn dict into list of tuples
for item in class_osprey.items():
    print(f'{item[0]} -- {item[1]}')


# looping over a string

greeting = 'Hello from Class Osprey'
output = ''

for letter in greeting:
    if choice((True, False)):
        output += letter.upper()
    else:
        output += letter.lower()

print(output)


# nested loop

students = [
    'Liam',
    'Cynthia',
    'Steve'
]

for student in students:
    output = ''
    for letter in student:
        if choice((True, False)):
            output += letter.upper()
        else:
            output += letter.lower()
    print(output)


students = {
    'Liam': {'pet': 'Jude', 'favorite band': 'Metric'},
    'Cynthia': {'pet': 'Penelope', 'favorite band': 'Grateful Dead'},
    'Steve': {'pet': 'Caboose', 'favorite band': 'Radiohead'},
}

for name in students:
    for fact in students[name]:
        print(f'{name}\'s {fact} is {students[name][fact]}')
