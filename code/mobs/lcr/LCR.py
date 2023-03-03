import random
'''
needs-
input to enter players
each player starts with 3 chips
need chips variable (int)
need pot to move to/from

figure dice mechanic: L, C, R, . , . , . 
weighted chance?
import random

mechanic of chips from last person to next person
conditions for each movement

chips list with matching players list to match indices

or list has sequences, tuple of (player, chips)

win condition when only one person has chips > 0'''


pot = 0

dice_options = ['L', 'C', 'R', '.', '.', '.']

def creating_players():
    players = []
    chips = []
    creating = 'yes'
    while creating == 'yes':
        entry = input('Player name, type Done to finish: ')
        
        if entry == 'Done':
            print(players)
            break

        players.append(entry)
    
    for player in players:
        chips.append(3)


    return players, chips

creating_players()

def LCR_active():
    pass
