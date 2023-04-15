



let userInput = document.querySelector('input[type=text]')
let userNumber = document.querySelector('input[type=number]')
const submitButton = document.querySelector('button[id="sendmessage"]')



alphabet = ['a','b','c', 'd','e','f','g','h','i','j','k','l', 'm', 'n','o', 'p', 'q','r','s','t','u','v','w','x','y','z',]



submitButton.addEventListener('click', () => {
    let rotation = parseInt(userNumber.value)

    let newMessage = '';
    for (item of userInput.value){
        index = alphabet.indexOf(item)
        newMessage += alphabet[(rotation + index) % 26]
    }
    output.innerHTML = newMessage
 
})



