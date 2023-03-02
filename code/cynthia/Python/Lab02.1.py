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


# face_cards = {
#     1: 'A',
#     10: 'J',
#     10: 'K',
#     10:'Q',
# }



# print("Choose three cards from options A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K ")

# card_1 = int(input("What's your first card? "))
# card_2 = int(input("What's your second card? "))
# card_3 = int(input("What's your third card? "))



# def sum(card_1, card_2, card_3):
#     sum = card_1 + card_2 + card_3
#     return sum 
# # print(sum(card_1, card_2, card_3))

# #all of this works, do not touch
# if sum(card_1, card_2, card_3) < 17:
#     print(f"{sum(card_1, card_2, card_3)} Hit")

# elif 17>= sum(card_1, card_2, card_3) < 21:
#     print(f"{sum(card_1, card_2, card_3)} Stay")

# elif sum(card_1, card_2, card_3) == 21:
#     print("Blackjack!")
# else:
#     print("Already Busted")





#################
#list jkq, if ace add 1, if in face cards add ten, else add int cast 
#loop over user_input
#define a hand value

face_cards = ['J', 'Q', 'K']
# face_cards = 10
A = 1
hand_value = 0

card_1 = input("What's your first card? ")
card_2 = input("What's your second card? ")
card_3 = input("What's your third card? ")

user_input = card_1, card_2, card_3

while A in user_input:
    hand_value +=1
    print(hand_value)

    if face_cards in user_input:
        hand_value += 10
    else:
        hand_value += int(sum(user_input))

print(hand_value)





# all of this works, do not touch
# if sum(card_1, card_2, card_3) < 17:
#     print(f"{sum(card_1, card_2, card_3)} Hit")

# elif 17>= sum(card_1, card_2, card_3) < 21:
#     print(f"{sum(card_1, card_2, card_3)} Stay")

# elif sum(card_1, card_2, card_3) == 21:
#     print("Blackjack!")
# else:
#     print("Already Busted")