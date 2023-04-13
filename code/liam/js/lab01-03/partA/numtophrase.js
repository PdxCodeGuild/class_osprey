let time = prompt('What time is it? Use 12 hour format and \':\' marker: ')

let hour = 1
let minutes = 11

if (time.length === 4) {
    hour = time[0]
    minutes = time[2] + time[3]
} else if (time.length === 5) {
    hour = time[0] + time[1]
    minutes = time[3] + time[4]
} else {
    alert('Your entry was invalid!')
}

let numHour = Number(hour)
let numMinutes = Number(minutes)
let tensDigit = Math.floor(numMinutes/10)
let onesDigit = numMinutes%10

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

if (numHour < 10) {
    englishHour = onesTable[hour]
} else if (numHour >= 10 && numHour <= 12) {
    englishHour = tenteensTable[hour]
}
let englishTens = tensTable[tensDigit]
let englishOnes = onesTable[onesDigit]

if (minutes === '00') {
    alert(`The time is ${englishHour} o\'clock`)
} else if (numMinutes > 59 || numHour > 12) {
    alert(`Invalid entry, please refresh and try again.`)
} else if (numMinutes >= 10 && numMinutes <= 19) {
    let tenTeens = tenteensTable[numMinutes]
    alert(`The time is ${englishHour} ${tenTeens}`)
} else {
    alert(`The time is ${englishHour} ${englishTens} ${englishOnes}`)
}