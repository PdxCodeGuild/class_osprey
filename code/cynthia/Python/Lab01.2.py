# Version 2
# Handle numbers from 100-999.


x = 168
# hundreds_digit =
# print(hundreds_digit)
tens_digit = x//10 * 10
print(tens_digit)
ones_digit = x%10
print(ones_digit)


number_conversion = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three", 
    4: "four",
    5: "five", 
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eightteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"fourty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninty",
    100:"onehundred",
    200:'twohundred',
    300: 'threehundred',
    400:'fourhundred',
    500:'fivehundred',
    600:'sixhundred',
    700:"sevenhundred",
    800:'eighthundred',
    900:"ninehundred",

    
}


# if x < 9:
#     print(number_conversion.get(ones_digit))

# elif 11 <= x <= 19:
#     print(number_conversion[x]) 
# elif ones_digit == 0:
#     print((number_conversion.get(tens_digit)))
# elif x> 100:
#     print(number_conversion.get(hundreds_digit) + ' ' +number_conversion.get(tens_digit) + '-' + (number_conversion.get(ones_digit)))
# else:
#     print(number_conversion.get(tens_digit) + '-' + (number_conversion.get(ones_digit)))


