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
print(f'Your friends are {friends_list}')


while True:
    create = input('Would you like to add a new friend?:')
    if create != 'y':
        break

    while create == 'y':
        new_friend = input("new friends name: ")
        new_color = input("their favorite color: ")
        new_fruit = input("their favorite fruit: ")
        add_friends_list=[{'name': new_friend, 'favorite color': new_color, 'favorite fruit':new_fruit}]
        break
    friends_list.extend(add_friends_list)
    print(friends_list)

    friend_info = []

    retrieve = input('Would you like to retrieve friend?:')
    if retrieve != 'y':
        break
    info = input('Name of friend for info: ')

    for i in range(len(friends_list)):
        if friends_list[i]['name'] == info:
            friend_info.append(friends_list[i])
            break
    print(friend_info)


    update = input("Would you like to update a friend? ")
    if update != 'y':
        break
    friend_to_update = input('Name of the friend you want to update: ')
    attribute_key= input('What attribute do you want to update? ')
    new_attribute = input('New attribute: ')

    for i in range(len(friends_list)):
        if friends_list[i]['name'] == friend_to_update:
            friends_list[i][attribute_key] = new_attribute
    print(friends_list)

    delete = input("Would you like to delete a friend? ")
    if delete != 'y':
        break
    delete_a_friend = input("What is the name of the person to remove? ")
    for i in range(len(friends_list)):
        if friends_list[i]['name'] == delete_a_friend:
            del friends_list[i]
    print(friends_list)
