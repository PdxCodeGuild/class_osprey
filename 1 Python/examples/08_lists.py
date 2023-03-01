"""Nested List Access"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter, summer]
print(seasons2d)

# access by index c
july = seasons2d[1][1]
letter_y = seasons2d[1][1][3]
print(letter_y)


'''Using indices'''
# find the index of a value in a list
# list.index() returns the index of the FIRST instance of whatever you search for
summer_index = seasons2d.index(summer)
print(summer_index)
july = seasons2d[summer_index][summer.index('july')]
print(july)


# reassign value by index
seasons2d[3][2] = 'february'
seasons2d[3][2] = 'june again'
# print(seasons2d)


'''Looping'''
# nested loop
for season in seasons2d:
    for month in season:
        # print(month)
        pass


# nested loop with index
for i in range(len(seasons2d)):
    for j in range(len(seasons2d[i])):
        # print(seasons2d[i][j])
        pass


'''Inclusion'''
grocery_list = ['apples', 'beans', 'bread', 'juice']
items_to_add = ['milk', 'coffee', 'juice', 'juice', 'apples']

# 'in' is a boolean operator that checks for inclusion in a list
# for item in items_to_add:
#     if item not in grocery_list:
#         grocery_list.append(item)

print(grocery_list)


'''List methods'''

# extend
grocery_list.extend(items_to_add)

# insert
grocery_list.insert(1, 'juice')

# remove (removes first instance it finds)
grocery_list.remove('juice')
# grocery_list.remove('bananas')

# pop
apples = grocery_list.pop()
print(apples)

juice = grocery_list.pop(3)
print(juice)

# count
print(grocery_list.count('juice'))


# remove all instances
while 'juice' in grocery_list:
    grocery_list.remove('juice')

print(grocery_list)


'''Slicing'''

middle_three = grocery_list[1:4]
first_three = grocery_list[:3]
last_two = grocery_list[3:]

print(first_three)
print(middle_three)
print(last_two)

# step
print(grocery_list[0:5:3])

# negative indexes count from the end
print(grocery_list[-2])

print(grocery_list[0:-2])
print(grocery_list[-4:-1])

# negative step reverses the list
print(grocery_list[::-1])


languages_frameworks_engines_etc = [
    'Unity',
    'Angular',
    'French',
    'Django Rest Framework',
    'Russian',
    'Lua',
    'Vue',
    'Pascal',
    'Godot',
    'JavaScript',
    'Korean',
    'PHP',
    'Django',
    'Perl',
    'Dutch',
    'CSS',
    'Express',
    'HLSL',
    'HTML',
    'Unreal Engine',
    'Dothraki',
    'Flask',
    'Elvish',
    'Doggo-Speak',
    'Python',
    'High Valyrian',
    'Morse Code',
    'C++'
]

curriculum = languages_frameworks_engines_etc[-4:3:-3]
print(curriculum)
