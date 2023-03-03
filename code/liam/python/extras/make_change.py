#convert a dollar amount into a number of coins

'''example:
input: 1.37

output:

quarters: 5
dimes: 1
nickels: 0
pennies: 2
'''
#CHANGE MATH TO INTS
#take input from user-
money = float(input('How much money do you need change for? '))

in_pennies = money * 100

print(money) 
print(in_pennies) #DELETE LATER

#dictionary not necessary for simple math but why not practice
coin_values = {
    'quarters' : 25,
    'dimes' : 10,
    'nickels': 5,
    'pennies' : 1
}

quarters = int(in_pennies // coin_values['quarters'])
remainder = in_pennies % coin_values['quarters']

dimes = int(remainder // coin_values['dimes'])
second_remainder = remainder % coin_values['dimes']

nickels = int(second_remainder // coin_values['nickels'])
third_remainder = second_remainder % coin_values['nickels']

pennies = int(third_remainder // coin_values['pennies'])


print(f'''The amount of ${money} can be converted into:
quarters = {quarters}
dimes = {dimes}
nickels = {nickels}
pennies = {pennies}
''')