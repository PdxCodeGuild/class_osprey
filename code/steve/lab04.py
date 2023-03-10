# Credit card validation

cc_number = list(input("What is your credit card number? "))
cc_number = [int(i) for i in cc_number]
# check digit
check_digit = int(cc_number.pop())
print(cc_number)
# reversing list order
cc_number.reverse() 
doubled_list = cc_number.copy()
'''to_double = cc_number[0::2]
stay = cc_number[1::2]

single = []
for _ in stay:
    single.append(int(_) * 1)

double = []


for _ in to_double:
    if int(_) < 5:
        double.append(int(_) * 2)
    else:
        double.append(int(_) * 2 - 9)

total = sum(single) + sum(double)'''
for i in range(len(doubled_list)):
    if i % 2 == 0:
        doubled_list[i] = doubled_list[i] * 2

subtracted_list = [i - 9 if i > 9 else i for i in doubled_list]

print(cc_number)
print(doubled_list)
print(subtracted_list)
total = sum(subtracted_list)
number_to_verify = (total % 10)

if number_to_verify == check_digit:
    print("Valid number") 
else:
    print("Invalid number")

print(number_to_verify, check_digit)

