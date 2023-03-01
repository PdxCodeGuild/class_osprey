#blackjack suggestion

#request hand info
first_card = input('What is your first card? ')
second_card = input('What is your second card? ')
third_card = input('What is your third card? ')

face_values = {
    'A': 1,
    'J': 10,
    'Q': 10,
    'K': 10,
}

for keys in face_values:
    if first_card == keys:
        first_card = face_values[keys]
    if second_card == keys:
        second_card = face_values[keys]
    if third_card == keys:
        third_card = face_values[keys]

#now we want all integers to add up, converting too early loses face card value

first_card = int(first_card)
second_card = int(second_card)
third_card = int(third_card)

#establish the full hand
#add up numerical values on hand
hand = first_card + second_card + third_card

if hand < 17:
    print(f'At {hand} you should hit')
elif hand >= 17 and hand < 21:
    print(f'With a {hand} you should stay')
elif hand == 21:
    print(f'Exactly {hand}! Blackjack!')
else:
    print(f'With a hand of {hand} - you have already busted. :(')