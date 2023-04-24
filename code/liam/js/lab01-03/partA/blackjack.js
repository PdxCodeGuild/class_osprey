alert('Blackjack suggestions :)')
let firstCard = prompt('What is your first card?').toUpperCase()
let secondCard = prompt('What is your second card?').toUpperCase()
let thirdCard = prompt('What is your third card?').toUpperCase()

const cardWorth = {
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

let firstValue = cardWorth[firstCard]
let secondValue = cardWorth[secondCard]
let thirdValue = cardWorth[thirdCard]

console.log(firstValue, secondValue, thirdValue)

let handValues = [firstValue, secondValue, thirdValue]
let hand = [firstCard, secondCard, thirdCard]
let total = handValues.reduce((adding, a) => adding + a, 0)

alert(`Got it- You have ${firstCard}, ${secondCard}, and ${thirdCard}`)

console.log(total)

if (hand.includes('A')) {
    if (total <= 11) {
        total += 10
    }
}

if (firstValue == undefined || secondValue == undefined || thirdValue == undefined) {
    alert(`Invalid entry included. Please try again.`)
} else if (total < 17) {
    alert(`At ${total}, you should hit`)
} else if (total >= 17 && total < 21) {
    alert(`With ${total}- stay.`)
} else if (total === 21) {
    alert(`${total}!!! Blackjack!`)
} else {
    alert(`At ${total}, you've already busted.`)
}