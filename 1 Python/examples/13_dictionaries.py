from random import random
''' Dictionaries 
Keys must be immutable types
strings and ints are most common
bool and float also work
tuples can be dict keys if they ONLY contain immutable
technically a range object is immutable but what are you doing?
'''

var1 = '6'

valid_dict = {
    'string key': 1,
    123: 2,
    4.5: 3,
    True: 4,
    (1, False): 5,
    var1: 6
}

print(valid_dict)

'''Accessing values'''

pizza_ratings = {
    'pineapple': 'the best',
    'olives': 'gross',
    'pepperoni': 'okay I guess'
}

# access by key with square brackets
print(pizza_ratings['olives'])
# print(pizza_ratings['mushrooms']) #KeyError: 'mushrooms'

# access by key with dict.get()
print(pizza_ratings.get('pepperoni'))
print(pizza_ratings.get('anchovies'))  # None


'''Adding and updating values'''

pizza_ratings['mushrooms'] = 'meh'
pizza_ratings['pineapple'] = 'the worst'

pizza_ratings.update({'peppers': 'great'})
pizza_ratings.update({'pineapple': 'controversial', 'sausage': 'basic'})

print(pizza_ratings)

'''Iterating over a dictionary'''

for key in pizza_ratings:
    val = pizza_ratings[key]
    print(key, val)

# exactly the same thing
for key in pizza_ratings.keys():
    # val = pizza_ratings[key]
    # print(key, val)
    ...

# almost exactly the same thing.... but better?
for key, val in pizza_ratings.items():
    # print(key, val)
    ...


for val in pizza_ratings.values():
    # print(val)
    ...


'''Dict methods
.get() returns the value of a key, or None
.update() merges two dicts
.items() returns a list-like object with tuples (key, val)
.values() returns a list-like object of the values
.keys() returns a list-like object of the keys

.clear() empties a dict
.copy() returns a copy
'''

# .popitem() returns a tuple of the most recently added key (and removes it)
pop_return = pizza_ratings.popitem()
# print(pop_return)
# print(pizza_ratings)

# .pop(key) returns the value for a key, and removes from the dict
pop_return = pizza_ratings.pop('pineapple')
# print(pop_return)
# print(pizza_ratings)

students = (
    'Steve',
    'Cynthia',
    'Liam'
)

student_grades = dict.fromkeys(students, None)
for student in student_grades:
    student_grades[student] = random() * 100

print(student_grades)

# the same thing
student_grades = {}
for s in students:
    student_grades[s] = random() * 100

print(student_grades)


'''Accessing and updating nested dictionaries'''

reading_levels = {
    1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
    3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

kindergarten = reading_levels[1]['grade_level']
print(kindergarten)

reading_levels[13]['grade_level'] = 'Senior Year'
reading_levels.get(14)['ages'] = 'no limit'
print(reading_levels)


'''Navigating a complex data structure'''

dans_pets = [
    {'turkey': {
        'fullname': 'Admiral Turkey Sandwich',
        'personality': 'rude',
        'favorite things': ['head butting', 'chewing things', 'knocking glasses down']
    }},
    {'barney': {
        'named_after': 'a basset hound from a kids movie',
        'was_smart': False
    }}
]

third_favorite_thing = dans_pets[0]['turkey']['favorite things'][2]
print(third_favorite_thing)

if not dans_pets[1]['barney']['was_smart']:
    print('Barney was the best dog ever')
