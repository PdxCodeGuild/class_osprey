'''Dictionary comrehensions
{key:val for element in iterable}
{key:val for element in iterable if condition}
'''

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
list1 = ['a', 'b', 'c', 'd', 'e']


comp1 = {letter: letter*3 for letter in list1}
print(comp1)

comp2 = {letter: letter*dict1[letter] for letter in dict1}
print(comp2)


zoo_popularity = {
    'alligator': '8%',
    'panda': '15%',
    'hippopotamus': '3%',
    'lion': '7%',
    'rhinocerous': '2%',
    'cheetah': '6%',
    'bat': '25%'
}

long_name_exhibit = {key.capitalize(): int(zoo_popularity[key][:-1])
                     for key in zoo_popularity if len(key) > 8}

print(long_name_exhibit)

labs = {
    'number to phrase': 82,
    'blackjack advice': 65,
    'pick 6': 95,
    'cc validator': 95,
    'rot13': 52,
    'contacts list': 30
}


def get_difficulty(num):
    if num > 90:
        return 'easy'
    elif num > 80:
        return 'kinda easy'
    elif num > 70:
        return 'kinda hard'
    else:
        return 'hard'


curriculum = {lab: get_difficulty(score)
              for lab, score in labs.items() if score >= 70}

print(curriculum)
