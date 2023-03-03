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



def LCR_active(chips, player_index):
    dice_options = ['L', 'C', 'R', '.', '.', '.']

    roll_count = 0

    if chips[player_index] >= 3:
        roll_count = 3
    else:
        roll_count = chips[player_index]

    for i in range(roll_count):
        dice_roll = random.choice(dice_options)
        # dice_roll = 'R'
        if dice_roll == "C":

            chips[player_index] -= 1
        elif dice_roll == 'R':
            chips[player_index] -= 1
            if len(chips) == player_index + 1:
                chips[0] += 1
            else:
                chips[player_index + 1] += 1
        elif dice_roll == 'L':
            chips[player_index] -= 1
            chips[player_index - 1] += 1
        else: 
            dice_roll == "."
        print(f'{dice_roll} is in {chips}')
    return chips

players, chips_start = creating_players()


def outcome(players):

    chip_holders = 0

    for score in players:
        if score > 0:
            chip_holders += 1
    if chip_holders > 1:
        return True
    return False

while True:
    for i in range(len(players)):
        if outcome(chips_start):
            chips_start = LCR_active(chips_start, i)
        else:
            break
    if not outcome(chips_start):
        break

high_score = max(chips_start)

score_finder = chips_start.index(high_score)

print(f'The winner is {players[score_finder]}')