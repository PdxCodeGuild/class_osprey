#Contact list - v1

with open('code\liam\python\lab07\contacts_og.csv', 'r') as file:
    lines = file.read().split('\n')
    #print(lines) #verify read

#take first list as keys of first dict
headers = lines[0].split(',')
# print(headers) ['name', 'age', 'favorite animal', 'pokemon']

all_contacts = []

for line in lines[1:]:
    contact_info = {}
    contact = line.split(',')
    i = 0  
    for key in headers:
        value = contact[i]
        contact_info[key] = value
        i += 1
    all_contacts.append(contact_info)

print(all_contacts)