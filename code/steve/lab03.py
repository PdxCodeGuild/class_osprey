# Lottery game
import random

# number match dictionary, counter for while loop and pot to collect winnings
match_dict = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
counter = 0
pot = 0

# make a ticket function
def make_ticket():
    return random.sample(range(1, 100), 6)

# find matches function
def find_matches(ticket):
    return 0 + bool(winner[0] == ticket[0]) + bool(winner[1] == ticket[1]) + bool(winner[2] == ticket[2]) + bool(winner[3] == ticket[3]) + bool(winner[4] == ticket[4]) + bool(winner[5] == ticket[5])

# used to calculate winnings
def calculate_winnings(matches):
    return match_dict[matches]

 # winning numbers
winner = make_ticket()

# n is the number of tickets purchased
n = 100000
# picking tickets at random
while counter < n:
    counter += 1
    ticket = make_ticket()
    matches = find_matches(ticket)
    winnings = calculate_winnings(matches)
    pot += winnings

# winnings is equal to the sum of the pot minus the cost of tickets, which is 2n
winnings = pot - (2 * n)


print(f'${winnings}')
