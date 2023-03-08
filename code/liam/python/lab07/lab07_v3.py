#Contact list - v3 REWRITE time

with open('code\liam\python\lab07\contacts_og.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines) #verify read

#take first list to use as list of keys
headers = lines[0].split(',')

all_contacts = []

for line in lines[1:]: #index 0 not popped, use 1 and onward for info
    contact_info = {}
    contact = line.split(',')
    i = 0  
    for key in headers:
        value = contact[i]
        contact_info[key] = value
        i += 1
    all_contacts.append(contact_info)

# print(all_contacts) hold if needed

#crud begins
while True:  
    current_list = [x for x in all_contacts]
    choice = input('''For your contacts, would you like to:
Create, Retrieve, Update, or Delete a record?
Enter "C", "R", "U", "D", or "done" to exit: ''')

#-----------------------CREATE
    while choice == 'C':
        print('''You have chosen to create!
        We'll need some information for the new file.
        What is the new entry\'s... ''')
        c_name = input('name: ')
        c_age = input('age: ')
        c_favanimal = input('favorite animal: ')
        c_pokemon = input('favorite pokemon: ')
        
        new_list = [c_name, c_age, c_favanimal, c_pokemon]

        for entry in new_list:
            contact_info = {}
            i = 0  
            for key in headers:
                value = new_list[i]
                contact_info[key] = value
                i += 1
        all_contacts.append(contact_info)

        break

#-----------------------RETRIEVE    
    while choice == 'R':
        print(f'''You have chosen to retrieve the records.
        Currently, your list of contacts is: 
        {current_list}''')
        break

#-----------------------UPDATE
    while choice == 'U':
        print('Update process confirmed.')
        u_name = input('Whose information are you updating? ')
        u_att = input('And which attribute needs changing? ')
        edit = input('What will we be changing that to? ')
        for match in range(len(all_contacts)): #need to find index
            if u_name == all_contacts[match]['name']:
                all_contacts[match][u_att] = edit
            break
        print('All done! We hope this person agreed to this.')
        break

#-----------------------DELETE
    while choice == 'D':
        print('You have selected to delete a record.')
        d_name = input('Whose record would you like to remove? ')
        for match in range(len(all_contacts)):
            if d_name == all_contacts[match]['name']:
                all_contacts.pop(match)
                break
        print(f'{d_name} is no longer on record. We are sorry for whatever happened between you and them.')
        break

    if choice == 'done':
        print('Understood. Updating files...')
        #TURN ALL DATA BACK INTO CSV FORMAT#
        output = []
        header_out = ','.join(headers)

        for people in range(len(all_contacts)):
            holdlist = []
            holdstring = ''
            for values in all_contacts[people].values():
                holdstring = ''.join(values)
                holdlist.append(holdstring)
            holdstring = ','.join(holdlist)
            output.append(holdstring)
        output.insert(0, header_out)

        with open('code\liam\python\lab07\contacts_new.csv', 'w') as file:
            file.write('\n'.join(output)) 
        break
