#Version 1
#convert a given number into a phrase
#Hint: you can use modulus to extract the ones and tens digit.
#Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.


x = 81
tens_digit = x//10 * 10
# print(tens_digit)
ones_digit = x%10
# print(ones_digit)


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
}


if x < 9:
    print(number_conversion.get(ones_digit))

elif 11 <= x <= 19:
    print(number_conversion[x]) 
elif ones_digit == 0:
    print((number_conversion.get(tens_digit)))

else:
    print(number_conversion.get(tens_digit) + '-' +(number_conversion.get(ones_digit)))
