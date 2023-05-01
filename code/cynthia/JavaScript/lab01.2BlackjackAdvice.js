
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


let card1 = document.querySelector('#card1')
let card2 = document.querySelector('#card2')
let card3 = document.querySelector('#card3')
const submitButton = document.querySelector('#send')




submitButton.addEventListener('click', () => {
    let handValue = deck[card1.value] + deck[card2.value] + deck[card3.value]
    if (handValue < 17) {
        result = (handValue, 'hit')
        
    } else if (17 == handValue){
            result = (handValue, 'stay')

    } else if (handValue <21 ){
        result = (handValue, 'stay')

    } else if (handValue == 21) {
        result = ('Blackjack!')
    } else if (handValue > 21){
        result = (handValue, "Already Busted")
    }
    
    output.innerHTML = result
})






    
