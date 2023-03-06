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

    while True:
        entry = input('Player name, type Done to finish: ')
        if entry == 'Done' or entry == 'done':
            print(players)
            break
        players.append(entry)
        chips.append(3)

    return players, chips


def LCR_round(chips, players, player_index):
    dice_options = ['L', 'C', 'R', '.', '.', '.']

    # ternary operator
    # variable = val1 if condition else val2
    roll_count = 3 if chips[player_index] >= 3 else chips[player_index]

    for _ in range(roll_count):
        dice_roll = random.choice(dice_options)
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
        print(f'{players[player_index]}\'s turn: {dice_roll} -- {chips}')
    return chips


def is_game_continuing(players):
    chip_holders = 0
    for score in players:
        if score > 0:
            chip_holders += 1
    return chip_holders > 1


player_list, chips_tracker = creating_players()

while True:
    for i in range(len(player_list)):
        if is_game_continuing(chips_tracker):
            chips_tracker = LCR_round(chips_tracker, player_list, i)
        else:
            break
    if not is_game_continuing(chips_tracker):
        break

winner_index = chips_tracker.index(max(chips_tracker))

print(f'The winner is {player_list[winner_index]}!')
