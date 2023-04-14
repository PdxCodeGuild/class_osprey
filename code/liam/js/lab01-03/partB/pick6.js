const playCount = document.querySelector('#plays')
const playDisplay = document.querySelector('#playdisplay')
const submitButton = document.querySelector('input[type="submit"]')
const results = document.querySelector('#results')

const pick6 = function () {
    let ticketPlaceholder = [1,2,3,4,5,6]
    let generatedTicket = []

    for (x of ticketPlaceholder) {
        let x = generatedTicket.push(Math.floor(Math.random() * 99) + 1)
    }
    return generatedTicket
}

const numMatches = function(winning, ticket) {
    let matchFinds = 0
    for (search of ticket) {
        if (winning.indexOf(search) === ticket.indexOf(search)) {
            matchFinds +=1
        }
    }   
    return matchFinds
}

const matchToWin = function(match) {
    prizePool = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000,
    }
    let winnings = prizePool[match]
    return winnings
}

let balance = 0
let totalWinnings = 0

playCount.addEventListener('change', () => {
    playDisplay.innerText = `Looking at ${playCount.value} tickets.`
})

const playGame = () => {
    let winningTicket = pick6()
    console.log(winningTicket)
    console.log(playCount.value)
    let plays = playCount.value

    while (plays > 0) {
        let playerTicket = pick6()
        plays -= 1
        balance += 2
        let finds = numMatches(winningTicket, playerTicket)
        let prize = matchToWin(finds)
        totalWinnings += prize
    }
    let netWin = totalWinnings - balance
    let roi = netWin / balance
    results.innerText = `This batch of lottery tickets nets you $${netWin}. After spending $${balance}, your ROI is ${roi}.`
}

submitButton.addEventListener('click', playGame)