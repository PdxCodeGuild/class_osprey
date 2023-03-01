import random
#-------------------Pick6-----------------------#

#Generate list of 6 random numbers representing winning tickets
'''Importing random at top to accomodate random choices here and for loop'''
#Start balance at 0
#Loop 100,000 times, for each loop:
#   Generate a list of 6 random numbers representing the ticket
#   Subtract 2 from your balance (you buying a ticket)
#   Find how many numbers match
#   Add to your balance the winnings from your matches
#After loop, print final balannce

def pick6():
    
    generated_ticket = []

    for picks in range(6):
        pick = random.randint(1,99)
        generated_ticket.append(pick)
        #starting these separated for needing to loop player ticket
    return generated_ticket

def num_matches(winning, ticket):

    match_finds = 0

    for search in range(len(ticket)): #search signifies the index of the list
        if ticket[search] == winning[search]:
            match_finds += 1
    return match_finds

#function that takes in matches and returns winnings

def match_to_win(match):
    if match == 0:
        winnings = 0
    elif match == 1:
        winnings = 4
    elif match == 2:
        winnings = 7
    elif match == 3:
        winnings = 100
    elif match == 4:
        winnings = 50000
    elif match == 5:
        winnings = 1000000
    elif match == 6:
        winnings = 25000000

    return winnings
#END OF FUNCTIONS

#Starting balance and winning ticket decided
balance = 0
total_winnings = 0 #start at 0
winning_ticket = pick6()

#how many times are we playing?
play_count = 100000 #change to 100,000 when prints are ready to be removed

for plays in range(play_count):
    ticket = pick6() #captures each returned ticket.
    play_count -= 1
    balance -= 2
    matches = num_matches(winning_ticket, ticket)
    prize = match_to_win(matches)
    total_winnings += prize #compiling match earnings

net_win = total_winnings + balance
print(f'The lottery tickets net you ${net_win} this time.')
