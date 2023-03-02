number = input("Enter a number: ")
number = int(number)


tens = (int(number) // 10) % 10
ones = int(number) % 10
hundreds = int(number) //100

list = [hundreds, tens, ones]

# dictionary for tens spot
ten_dict = {0 : '', 1 : '', 2 : "twenty", 3 : "thirty", 4 : "forty", 5 : "fifty", 6 : "sixty", 7 : "seventy", 8 : "eighty", 9 : "ninty"}
# dictionary for the ones spot
one_dict = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 0 : ''}

teen_dict = {0 : 'ten', 1 : 'eleven', 2 : 'twelve', 3 : 'thirteen', 4 : 'fourteen', 5 : 'fifteen', 6 :'sixteen', 7 : 'seventeen', 8 : 'eighteen', 9 : 'nineteen'}

while number > 0:
    if hundreds > 0:
        while tens > 1 and ones != 0:
            print(f'{one_dict[hundreds]} hundred {ten_dict[tens]}-{one_dict[ones]}') 
            break
        if tens == 1:
            print(f'{one_dict[hundreds]} hundred {teen_dict[ones]}')
        elif tens == 0:
            print(f'{one_dict[hundreds]} hundred {one_dict[ones]}')
        break
    elif hundreds < 1:
        if tens == 1:
            print(teen_dict[ones])
        elif tens > 1 and ones != 0:
            print(f'{ten_dict[tens]}-{one_dict[ones]}')
        elif tens > 1 and ones == 0:
            print(ten_dict[tens])
        else:
            print(one_dict[ones])
    break
else:
    print('zero')




