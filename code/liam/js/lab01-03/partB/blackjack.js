const submitButton = document.querySelector('input[type="submit"]')
const selections = document.getElementsByTagName('select')
const decision = document.querySelector('#decision')

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

for (each of selections) {
    for (pick in cardWorth) {
        const userChoices = document.createElement('option')
        userChoices.value = pick
        userChoices.innerText = pick
        each.appendChild(userChoices)
    }
}

let hand = [2,2,2]

const firstOptions = document.querySelector('select[name="first-card"]')
const secondOptions = document.querySelector('select[name="second-card"]')
const thirdOptions = document.querySelector('select[name="third-card"]')

firstOptions.addEventListener('change', (event) => {
    hand[0] = event.target.value
    console.log(hand)
})
secondOptions.addEventListener('change', (event) => {
    hand[1] = event.target.value
    console.log(hand)
})
thirdOptions.addEventListener('change', (event) => {
    hand[2] = event.target.value
    console.log(hand)
})

const totalCalcs = () => {
    let firstCard = hand[0]
    let secondCard = hand[1]
    let thirdCard = hand[2]

    let firstValue = cardWorth[firstCard]
    let secondValue = cardWorth[secondCard]
    let thirdValue = cardWorth[thirdCard]

    let handValues = [firstValue, secondValue, thirdValue]

    let total = handValues.reduce((adding, a) => adding + a, 0)

    if (hand.includes('A')) {
        if (total <= 11) {
            total += 10
        }
    }
    return total
}

submitButton.addEventListener('click', () => {
    total = totalCalcs()
    if (total < 17) {
        decision.innerText = `At ${total}, you should hit`
    } else if (total >= 17 && total < 21) {
        decision.innerText = `With ${total}- stay.`
    } else if (total === 21) {
        decision.innerText = `${total}!!! Blackjack!`
    } else {
        decision.innerText = `At ${total}, you've already busted.`
    }
})
