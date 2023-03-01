'''List comprehensions'''

numbers = []
for x in range(10):
    numbers.append(x ** 2)


# new_list = [appended_value for thing in things]
numbers = [x ** 2 for x in range(10)]

print(numbers)

numbers = [1, 2, 3, 4, 5]
odds = []
for num in numbers:
    if num % 2 == 1:
        odds.append(num)

# new_list = [appended_value for thing in things if condition]
odds = [num for num in numbers if num % 2 == 1]
print(odds)


'''Practice 1'''

hats = ['baseball cap', 'fedora', 'derby', 'panama']

for hat in hats:
    print(hat)

print_returns = [print(hat) for hat in hats]
print(print_returns)


'''Practice 2'''

dogs = ['lassie', 'fido', 'pickle', 'jack-jack', 'clifford']

dog_facts = []
for dog in dogs:
    dog_facts.append(f'{dog.capitalize()} is a good boy')

dog_facts = [f'{dog.capitalize()} is a good boy' for dog in dogs]

print(dog_facts)


'''Practice 3'''

numbers = [1, 245, 83, 29321, 4, 19, 218093, 2, 5]

evens = []
odds = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 == 1]

print(evens, odds)


'''Nested List Comprehension'''

spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'february']

seasons2d = [spring, summer, fall, winter]

months = []
for season in seasons2d:
    for month in season:
        months.append(month)


seasons = [month for month in season for season in seasons2d]
print(months)


# making a matrix
tic_tac_toe = [['|  |' for _ in range(3)] for _ in range(3)]
print(tic_tac_toe)
