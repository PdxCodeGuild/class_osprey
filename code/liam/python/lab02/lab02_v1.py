#blackjack suggestion

#request hand info
first_card = input('What is your first card? ')
second_card = input('What is your second card? ')
third_card = input('What is your third card? ')

card_worth = {
    'A': 1,
    'J': 10,
    'Q': 10,
    'K': 10,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

#change from first submission - using dictionary exclusively rather than for loop
first_value = card_worth[first_card]
second_value = card_worth[second_card]
third_value = card_worth[third_card]

#establish the full hand
#add up numerical values on hand
hand = first_value + second_value + third_value

if hand < 17:
    print(f'At {hand} you should hit')
elif hand >= 17 and hand < 21:
    print(f'With a {hand} you should stay')
elif hand == 21:
    print(f'Exactly {hand}! Blackjack!')
else:
    print(f'With a hand of {hand} - you have already busted. :(')