#convert number to english representation

#ask user for number, 'x':
x = input('What time is it? Please use the \':\' marker: ')

if len(x) == 4:

    hour = x[0]
    minutes = x[2] + x[3]
#skipping x[1] because expected ':'
elif len(x) == 5:
    hour = x[0] + x[1]
    minutes = x[3] + x[4]
else:
    print('Invalid entry!')

#currently strings
#make sure time is split into integers, not string
#this is because we can't do math to strings in the way we want
hour = int(hour)
minutes = int(minutes)

#getting those digits
m_tens_digit = minutes//10
m_ones_digit = minutes%10

#make some DICTIONARY
ones_table = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: '',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
}

tens_table = {
    0: 'oh',
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

if hour < 10:
    english_hour = ones_table[hour]
elif hour >= 10 and hour <= 12:
    english_hour = tenteens_table[hour]
english_tens = tens_table[m_tens_digit]
english_ones = ones_table[m_ones_digit]


if minutes == 00:
    print(f'The time is {english_hour} o\'clock')
elif minutes > 59 or hour > 12:
    print('Invalid format. Please use the twelve hour system')
elif minutes >= 10 and minutes <= 19:
    tenteens = tenteens_table[minutes]
    print(f'The time is {english_hour} {tenteens}')
else:
    print(f'So the time is {english_hour} {english_tens} {english_ones}')