# Version 2 - Version for HTML Lab05 Flask Form
# Handle numbers from 100-999.

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
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eightteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninty",

}


def convert_number(x):

    tens_digit = (x % 100)//10 * 10
    ones_digit = x % 10


    if x < 100:

        if x <= 9:
            return number_conversion.get(ones_digit)

        elif 11 <= x <= 19:
                return number_conversion[x]

        elif ones_digit == 0:
            return (number_conversion.get(tens_digit))
        else:
            return number_conversion.get(tens_digit) +' ' + number_conversion.get(ones_digit)


    elif x >= 100:
        if tens_digit == 10:
            return f'{number_conversion.get(x//100)} hundred {number_conversion[ones_digit + tens_digit]}'

        elif 20 <= tens_digit and ones_digit == 0:
            return f'{number_conversion.get(x//100)} hundred {number_conversion.get(tens_digit)}'

        else:
            tens_text = number_conversion.get(tens_digit)
            if tens_digit == 0:
                tens_text = ''
            ones_text = number_conversion.get(ones_digit)
            if ones_digit == 0:
                ones_text = ''
            return f'{number_conversion.get(x//100)} hundred {tens_text} {ones_text}'


 

