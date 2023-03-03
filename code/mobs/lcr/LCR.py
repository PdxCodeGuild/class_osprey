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

# def creating_players():
#     players = []
#     chips = []
#     creating = 'yes'
#     while creating == 'yes':
#         entry = input('Player name, type Done to finish: ')
        
#         if entry == 'Done':
#             print(players)
#             break

#         players.append(entry)
#     for player in players:
#         chips.append(3)
#     return players, chips

# creating_players()

chips = [3, 3]

def LCR_active(chips, player_index):
    dice_options = ['L', 'C', 'R', '.', '.', '.']
    # dice_roll = random.sample(dice_options)
    pot = 0
    for i in range(chips[player_index]):
        dice_roll = "C" #random.sample(dice_options)
        if dice_options.count(dice_roll): 
            if dice_roll == "C":
                pot += 1 
                chips[player_index] -= 1
            else: 
                dice_roll == "."
            print(f'{dice_roll} is in {chips} and the pot is {pot}')
        return chips, pot
        '''if chips[i] >= 3:
            dice_roll * 3
        else:
            dice_roll == chips
        
        '''
LCR_active(chips, 1)
print(chips)