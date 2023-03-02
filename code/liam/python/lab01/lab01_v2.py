#convert number to english representation

#ask user for number, 'x':
x = input('Enter a one to three digit number: ')

#make sure x is an integer, not a string
#this is because we can't do math to strings in the way we want
x = int(x)

#getting those digits
hundreds_digit = x//100
tens_digit = int((x/10)%10)
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
    0: '',
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

hundreds_table = {
    0: '',
    1: 'one hundred ',
    2: 'two hundred ',
    3: 'three hundred ',
    4: 'four hundred ',
    5: 'five hundred ',
    6: 'six hundred ',
    7: 'seven hundred ',
    8: 'eight hundred ',
    9: 'nine hundred ',
}

english_hundreds = hundreds_table[hundreds_digit]
english_tens = tens_table[tens_digit]
english_ones = ones_table[ones_digit]

if x == 0:
    print('That is a zero')
elif x >= 10 and x <= 19:
    tenteens = tenteens_table[x]
    print(f'That is a {tenteens}')
elif x <10:
    print(f'That is a {english_ones}')
elif x >= 10 and x <100:
    print(f'That is {english_tens}{english_ones}')
else:
    print(f'That is {english_hundreds}{english_tens}{english_ones}')