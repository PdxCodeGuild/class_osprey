#convert number to roman numeral representation

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
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    0: '',
}

tens_table = {
    0: '',
    1: 'X',
    2: 'XX',
    3: 'XXX',
    4: 'XL',
    5: 'L',
    6: 'LX',
    7: 'LXX',
    8: 'LXXX',
    9: 'XC',
}

#Teens conventions removed, not necessary in roman numerals

hundreds_table = {
    0: '',
    1: 'C',
    2: 'CC',
    3: 'CCC',
    4: 'CD',
    5: 'D',
    6: 'DC',
    7: 'DCC',
    8: 'DCCC',
    9: 'CM',
}

roman_hundreds = hundreds_table[hundreds_digit]
roman_tens = tens_table[tens_digit]
roman_ones = ones_table[ones_digit]

if x == 0:
    print('That is a zero')
elif x <10:
    print(f'That is a {roman_ones}')
elif x >= 10 and x <100:
    print(f'That is a {roman_tens}{roman_ones}')
else:
    print(f'That is {roman_hundreds}{roman_tens}{roman_ones}')