# Lab 3: Pick6
# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'. 
# Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff.
# Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
# If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match.
# Calculate your net winnings (the sum of all expenses and earnings).

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets.
# Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

# Steps
# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance


#creates 6 computer generated random numbers 
import random

winning_numbers = random.sample(range(0,20),6)
print(winning_numbers)
user_numbers = random.sample(range(0,20),6)
# print(user_numbers)


#this is the function if we want the user to input their own numbers 
# user_numbers = []
# x = 6
# for numbers in range(x):
#     numbers = int(input('enter numbers: '))
#     user_numbers.append(numbers)
#     # return user_numbers
# print(user_numbers)


money = 0

def pick6():
    game = input('would you like to pick6?')
    if game == 'y':
        print(user_numbers)
    return pick6
pick6()


if pick6 == True:
    money = money - 2
    print (money)
else:
     print(f'Remaining money {money}')

#compare the list with the computer number/ needs to be modified to only show consecutive matches?


result= []
def num_matches(winning_numbers, user_numbers):
    for number in winning_numbers:
        if number in user_numbers:
            if number not in result:
                result.append(number)
            print(result)
    return num_matches
num_matches(winning_numbers, user_numbers)



#determine how many match in order
def matches():
    if len(result) == 0:
        print("there are no matching numbers")

    elif len(result) == 1:
        print('there is one matching number')
        money = money + 4
        print(money)

    elif len(result) == 2:
        print('there are two matching numbers')
        money = money + 7
        print(money)

    elif len(result) == 3:
        print('there are three matching numbers')
        money = money + 100
        print(money) 

    elif len(result) == 4:
        print('there are four matching numbers')
        money = money + 50000
        print(money)

    elif len(result) == 5:
        print('there are five matching numbers')
        money = money + 1000000
        print(money)

    elif len(result) == 6:
        print('there are six matching numbers')
        money = money + 25000000
        print(money)
    return matches 

matches()

