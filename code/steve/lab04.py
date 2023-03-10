# Credit card validation

cc_number = list(input("What is your credit card number? "))

# check digit
check_digit = int(cc_number.pop())

# reversing list order
cc_number.reverse() 

to_double = cc_number[0::2]
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

total = sum(single) + sum(double)



number_to_verify = (total % 10) % 10

if number_to_verify == check_digit:
    print("Valid number") 
else:
    print("Invalid number")

print(number_to_verify, check_digit)

