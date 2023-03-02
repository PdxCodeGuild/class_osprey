import random
#-------------------Pick6-----------------------#

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
#updated to swap if/elif conditions for a dictionary

def match_to_win(match):

    prize_pool = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000,
    }

    winnings = prize_pool[match]

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
    balance += 2
    matches = num_matches(winning_ticket, ticket)
    prize = match_to_win(matches)
    total_winnings += prize #compiling match earnings

net_win = total_winnings - balance
roi = net_win / balance
print(f'''The lottery tickets net you ${net_win} this time.
After spending ${balance}, your ROI is {roi}.''')

#changes foe v2- to simplify math, balance is set up to be a negative number we can subtract instead.
#no need to create a positive number out of it for the ROI division
