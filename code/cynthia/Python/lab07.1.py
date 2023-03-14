#lab07.1
#without using csv import


with open('code/cynthia/addess_book.csv', 'r') as friends_list_file:
    text = friends_list_file.read().split('\n')
    lines = text[1:]
    keys = text[0].split(',')

friends_list = []

for line in lines:
    individuals = line.split(',')
    friends_list.append({keys[0]: individuals[0], keys[1]:individuals[1], keys [2]: individuals[2]})
print(f'Your friends are {friends_list}')