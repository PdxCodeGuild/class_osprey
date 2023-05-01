// import string
// string.ascii_lowercase

// alphabet = {
//     1:'a',
//     2:'b',
//     3:'c',
//     4:'d',
//     5:'e',
//     6:'f',
//     7:'g',
//     8:'h',
//     9:'i',
//     10:'j',
//     11:'k',
//     12:'l',
//     13:'m',
//     14:'n',
//     15:'o',
//     16:'p',
//     17:'q',
//     18:'r',
//     19:'s',
//     20:'t',
//     21:'u',
//     22:'v',
//     23:'w',
//     24:'x',
//     25:'y',
//     26:'z',

// }

alphabet = ['a','b','c', 'd','e','f','g','h','i','j','k','l', 'm', 'n','o', 'p', 'q','r','s','t','u','v','w','x','y','z',]

let userInput = prompt('What is your secret message?')
var userNumber = prompt('Rotate the alphabet by (enter a number)')

var rotation = parseInt(userNumber)

let newMessage = '';
for (item of userInput){
    index = alphabet.indexOf(item)
    newMessage += alphabet[(rotation + index) % 26]
}
console.log(newMessage)

