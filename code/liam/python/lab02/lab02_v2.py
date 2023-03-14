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
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


#dict keys establish card values
first_value = card_worth[first_card]
second_value = card_worth[second_card]
third_value = card_worth[third_card]


hand_values = [first_value, second_value, third_value]
hand = [first_card, second_card, third_card]
total = sum(hand_values)

for cards in hand:
    if 'A' in hand:
        if total <= 11:
            total += 10


if total < 17:
    print(f'At {total} you should hit')
elif total >= 17 and total < 21:
    print(f'With a {total} you should stay')
elif total == 21:
    print(f'Exactly {total}! Blackjack!')
else:
    print(f'With a hand of {total} - you have already busted. :(')