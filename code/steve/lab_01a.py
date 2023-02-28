# converting text to string

number = input("Enter a number: ")

tens = int(number) // 10
ones = int(number) % 10

# dictionary for tens spot
ten_dict = {0 : '', 1 : '',2 : "twenty-", 3 : "thirty-", 4 : "forty-", 5 : "fifty-", 6 : "sixty-", 7 : "seventy-", 8 : "eighty-", 9 : "ninty-"}
# dictionary for the ones spot
one_dict = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 0 : ''}

if int(number) == 10:
    print("ten")

elif int(number) == 0:
    print('zero')

elif int(number) == 11:
    print("eleven")

elif int(number) == 12:
    print("twelve")

elif int(number) == 13:
    print('thirteen')

elif int(number) == 15:
    print ('fifteen')

elif tens == 1:
    print(f"{one_dict[number]}teen")
else:
    print(f'{ten_dict[tens]}{one_dict[ones]}')