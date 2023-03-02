# Blackjack

# Card inputs
card1 = input("What is your first card? ")
card2 = input("What is your second card? ") 
card3 = input("And what is your third card? ")

# Card Value library
card = {"a":1, "k":10, "q":10, "j":10, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}


# Card total
total = (card[card1] + card[card2] + card[card3])

# output
if total < 17:
    print(f'{total} Hit')

elif total >= 17 and total < 21:
    print(f'{total} Stay')

elif total > 21:
    print(f'{total} Busted')

else:
    print(f'{total} Blackjack!')
