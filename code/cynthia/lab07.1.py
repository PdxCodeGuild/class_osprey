#lab07.1
#without using csv import

with open('code/cynthia/addess_book.csv', 'r') as file:
    text = file.read().split('\n')

details =[]
friends_dictionary = {}

for line in text:
    details = line.split(',')

    name = details[0]
    favorite_fruit = details[1]
    favorite_color = details[2]

    friends_dictionary = {'name': name, 'favorite color':favorite_color, 'favorite fruit':favorite_fruit }
    print(friends_dictionary)
