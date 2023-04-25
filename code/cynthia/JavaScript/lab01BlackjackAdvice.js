
const deck = {
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

card1 = prompt("What's your first card?")
card2 = prompt("What's your second card?")
card3 = prompt("What's your third card?")


let handValue = deck[card1] + deck[card2] + deck[card3]

if (handValue < 17) {
    console.log(handValue, 'hit')
} else if (17 == handValue){
    console.log(handValue, 'stay') 

} else if (handValue <21){
    console.log(handValue, 'stay')

} else if (handValue == 21) {
    console.log(handValue, 'Blackjack!')
} else if (handValue > 21){
    console.log(handValue, "Already Busted")
}