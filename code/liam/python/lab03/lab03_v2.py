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
