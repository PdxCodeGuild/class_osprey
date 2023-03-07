
address_book = {}

with open('code/cynthia/address_book_labo7.csv', 'w') as file:
    lines = file.read().split('\n')
    address_book = file.read()
    address_book = {rows[0]:rows[0] for rows in address_book}
print(address_book)

