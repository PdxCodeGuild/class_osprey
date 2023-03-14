#Lab 2.1
# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. 
# At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.


deck = {
    'A' : 1,
    'J': 10,
    'K': 10,
    'Q': 10,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
}

card_1 = input("What's your first card? ")
card_2 = input("What's your second card? ")
card_3 = input("What's your third card? ")

hand_value = deck.get(card_1) + deck.get(card_2) + deck.get(card_3)


if hand_value < 17:
    print(f"{hand_value} Hit")

elif 17>= hand_value < 21:
    print(f"{hand_value} Stay")

elif hand_value == 21:
    print("Blackjack!")
else:
    print("Already Busted")