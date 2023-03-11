'''
Fritz is a baker, he makes donuts and sells them by the dozen.
For a given number of donuts that he has:
- how many dozens can he sell?
- how many will he have leftover?
'''

total_donuts = 1365
dozen_size = 12

# using straight math
number_of_dozens = int(total_donuts / dozen_size)
leftover_donuts = total_donuts - (number_of_dozens * dozen_size)

# using floor division and modulus
number_of_dozens = total_donuts // dozen_size
leftover_donuts = total_donuts % dozen_size

output = f'Fritz can sell {number_of_dozens} dozen donuts and will have {leftover_donuts} donuts left over'
print(output)
