const time = document.querySelector('input[type="text"]')
const submitButton = document.querySelector('input[type="submit"]')

const answerBox = document.querySelector('#answer-box')
const displayPhrase = document.createElement('p')
displayPhrase.innerText = ''
answerBox.appendChild(displayPhrase)

let hour = 1
let minutes = 11
let valid = false

const validTime = () => {
    if (time.value.length === 4 && time.value[1] === ':') {
        valid = true
        hour = time.value[0]
        minutes = time.value[2] + time.value[3]
    } else if (time.value.length === 5 && time.value[2] === ':') {
        valid = true
        hour = time.value[0] + time.value[1]
        minutes = time.value[3] + time.value[4]
    } else {
        displayPhrase.innerText = 'Your entry was invalid!'
        time.value = ''
    }
}

onesTable = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: '',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
}
tensTable = {
    0: 'oh',
    1: 'null',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}
tenteensTable = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

submitButton.addEventListener('click', validTime)
submitButton.addEventListener('click', () => {

    if (valid) {
        let numHour = Number(hour)
        let numMinutes = Number(minutes)
        let tensDigit = Math.floor(numMinutes/10)
        let onesDigit = numMinutes%10

        if (numHour < 10) {
            englishHour = onesTable[hour]
        } else if (numHour >= 10 && numHour <= 12) {
            englishHour = tenteensTable[hour]
        }
        let englishTens = tensTable[tensDigit]
        let englishOnes = onesTable[onesDigit]

        if (minutes === '00' && numHour < 13) {
            displayPhrase.innerText = `The time is ${englishHour} o\'clock`
        } else if (numMinutes > 59 || numHour > 12) {
            displayPhrase.innerText = `Invalid entry, please try again.`
        } else if (numMinutes >= 10 && numMinutes <= 19) {
            let tenTeens = tenteensTable[numMinutes]
            displayPhrase.innerText = `The time is ${englishHour} ${tenTeens}`
        } else {
            displayPhrase.innerText = `The time is ${englishHour} ${englishTens} ${englishOnes}`
        }
    }
    validTime()
})