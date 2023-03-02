#convert number to english representation

#ask user for number, 'x':
x = input('Enter a two digit number: ')

#make sure x is an integer, not a string
#this is because we can't do math to strings in the way we want
x = int(x)

#getting those digits
tens_digit = x//10
ones_digit = x%10

#make some DICTIONARY
ones_table = {
    1: ' one',
    2: ' two',
    3: ' three',
    4: ' four',
    5: ' five',
    6: ' six',
    7: ' seven',
    8: ' eight',
    9: ' nine',
    0: '',
}

tens_table = {
    0: 'zero',
    1: 'null',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

#dedicate a segment just for The Teens because english is a sensible language
tenteens_table = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

english_tens = tens_table[tens_digit]
english_ones = ones_table[ones_digit]

if x == 0:
    print('That is a zero')
elif x >= 10 and x <= 19:
    tenteens = tenteens_table[x]
    print(f'That is a {tenteens}')
elif x <10:
    print(f'That is a {english_ones}')
else:
    print(f'That is a {english_tens}{english_ones}')