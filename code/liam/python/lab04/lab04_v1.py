from functools import reduce

credit_input = input('Enter those wacky digits: ')
#Giving a paste option for faster testing: 4556737586899855

#converting input to list of ints
#list comprehending :)
cc_list = [int(num) for num in credit_input]

#slice off last digit, store as check digit
cc_without_check = cc_list[:-1]
check_digit = cc_list[-1:]

#reverse cc_without_check - negative step to reverse
cc_reversed = cc_without_check[::-1]

#double every other element in reversed list starting with index 0
#map here
cc_doubled = map(lambda x: x[1]*2 if not x[0]%2 else x[1], enumerate(cc_reversed))
#enumerate creates tuples of (index, list item) which allows access to indexes in a map

#Subtract nine from numbers over nine.
minus_nines = map(lambda x: x - 9 if x > 9 else x, list(cc_doubled))

#sum those values!
#let's reduce, for fun
def sum_cc_nums(num1, num2):
    return num1 + num2
#smallest reduce on earth? it works.

sum_cc = reduce(sum_cc_nums, list(minus_nines))

#check last digit of sum to see if matches check number
if sum_cc%10 == check_digit[0]:
    print(True)
else:
    print(False)