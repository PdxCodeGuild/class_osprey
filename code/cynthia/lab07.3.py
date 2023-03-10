#lab07.2
#without using csv import

#implement a CRUD REPL

with open('code/cynthia/addess_book.csv', 'r') as friends_list_file:
    text = friends_list_file.read().split('\n')
    text[0] #becomes headers
    
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

    make_changes = input('''
Enter 'create', 'retrieve', 'update', 'delete' or none to exit. 
Enter the change you would like to make:
''')
    if make_changes == 'none':
        print(friends_list)
        break

    add_friends_list = []
    if make_changes == 'create':
        new_friend = input("new friends name: ").capitalize()
        new_color = input("their favorite color: ")
        new_fruit = input("their favorite fruit: ")
        add_friends_list=[{'name': new_friend, 'favorite color': new_color, 'favorite fruit':new_fruit}]
        
        friends_list.extend(add_friends_list)
        print()
        print(f'Your updated friends are: {friends_list}')


    friend_info = []

    if make_changes == 'retrieve':
        info = input('Name of friend you want to retrieve: ').capitalize()
        for i in range(len(friends_list)):
            if friends_list[i]['name'] == info:
                friend_info.append(friends_list[i])
        print()
        print(f"{info}'s information is {friend_info}")

    
    if make_changes == 'update':
        friend_to_update = input('Name of the friend you want to update: ').capitalize()

        attribute_key= input('''Choose from "name", "favorite color", or "favorite fruit".
What information do you want to update? ''')
                             
        new_attribute = input('New attribute: ')
        for i in range(len(friends_list)):
            if friends_list[i]['name'] == friend_to_update:
                friends_list[i][attribute_key] = new_attribute
        print()        
        print(f'Your updated friend is: {friends_list}')

    if make_changes == 'delete':
        delete_a_friend = input("What is the name of the person to remove? ").capitalize()
        for i in range(len(friends_list)):
            if friends_list[i]['name'] == delete_a_friend:
                del friends_list[i]
                break
        print()
        print(f"Your friends list is now: {friends_list}")


    lines = []
    comma = ','

    with open('code/cynthia/addess_book.csv', 'a') as friends_list_file:
            for line in friends_list:
                lines = f'\n{line}\n'
                friends_list_file.write(lines)


       