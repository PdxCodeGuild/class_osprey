#lab07.2
#without using csv import

#implement a CRUD REPL

with open('code/cynthia/addess_book.csv', 'r') as file:
    text = file.read().split('\n')

details =[]
friends_list = []

for line in text:
    details = line.split(',')

    name = details[0]
    favorite_color= details[1]
    favorite_fruit = details[2]

    friends_list.append({'name': name, 'favorite color':favorite_color, 'favorite fruit':favorite_fruit})
print(friends_list)

# create = input('Would you like to add a new friend?:')
# create = 'y'

# while create == 'y':
# new_friend = input("new friends name: ")
# new_color = input("their favorite color: ")
# new_fruit = input("their favorite fruit: ")
# add_friends_list=[{'name': new_friend, 'favorite color': new_color, 'favorite fruit':new_fruit}]

# friends_list.extend(add_friends_list)
# print(friends_list)

friend_info = []
# # retrieve = input('Would you like to retrieve friend?:')
# # retrieve = 'y'

# # while retrieve == 'y':
# info = input('Name of friend for info: ')

# for i in range(len(friends_list)):
#     if friends_list[i].get('name') == info:
#         friend_info.append(friends_list[i])
#         break
# print(friend_info)

friend_to_update = input('Name of the friend you want to update: ')
attribute_key= input('What attribute do you want to update? ')
new_attribute = input('New attribute: ')

for i in range(len(friends_list)):
    if friends_list[i].get('name') == friend_to_update:
        if new_attribute == 'favorite color':
            friends_list['favorite color'] = new_attribute
        elif new_attribute == 'favorite fruit':
            friends_list['favorite fruit'] = new_attribute
        friends_list.append(friends_list[i])
        break
print(friend_info)
