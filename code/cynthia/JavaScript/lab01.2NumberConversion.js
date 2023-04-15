const numberConversion ={

    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eightteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninty",
};



const userNumberInput = document.querySelector('#userNumber')
const submitButton = document.querySelector('button[id="convert"]')


submitButton.addEventListener('click', () => {
    let userNumber= userNumberInput.value

    let tensDigit = Math.floor((userNumber % 100)/10) * 10 
    let onesDigit = userNumber % 10

    // tensText = numberConversion[tensDigit]
    // onesText =numberConversion[onesDigit]
    // let tensText = ''
    // let onesText = ''


// if branching issue
    if (userNumber < 100){ 
        if (userNumber <= 9) {
            newOutput = numberConversion[onesDigit]
        } else if ( 11 <= userNumber <= 19) {
                newOutput = numberConversion[userNumber]
        } else if (onesDigit == 0) {
            newOutput = numberConversion[tensDigit]
        } else { 
            newOutput= numberConversion[tensDigit] + ' ' + numberConversion[onesDigit]
        }
    }
    else if (userNumber >= 100) {
        if (tensDigit == 10){
            newOutput = ((numberConversion[Math.floor(userNumber/100)])+ 'hundred'+ (numberConversion[onesDigit + tensDigit]))
        } else if (20 <= tensDigit && onesDigit == 0){
            newOutput = ((numberConversion[Math.floor(userNumber/100)])+ 'hundred'+ (numberConversion[tensDigit]))

        } else {
            
            if (tensDigit == 0){
                tensText = ''
                onesText = numberConversion[onesDigit]
            } 
            if (onesDigit == 0){
                onesText = ''
                tensText = numberConversion[tensDigit]
            }
                newOutput = ((numberConversion[Math.floor(userNumber/100)])+ 'hundred'+ tensText, onesText)
        }
}
    output.innerHTML = newOutput
})