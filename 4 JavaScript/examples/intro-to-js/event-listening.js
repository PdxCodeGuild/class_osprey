const box = document.getElementById('box')
box.classList.add('red')

// use event listeners to detect user interactions with an element
box.addEventListener('mouseover', () => console.log('this happened'))
box.addEventListener('click', () => box.classList.toggle('red'))


const button = document.querySelector('input[value="Vote"]')
const checkboxes = document.querySelectorAll('input[type="checkbox"]')
const nameInput = document.querySelector('input[type=text]')
const people = document.querySelectorAll('li')
const names = Array.from(people).map(el => el.innerText)
let valid = false
let voters = []

// check whether button should be disabled
const checkValidity = () => {
    const alreadyVoted = voters.includes(nameInput.value)
    const checked = Array.from(checkboxes).filter(el => el.checked)
    if (names.includes(nameInput.value) && checked.length > 0 && !alreadyVoted) {
        button.removeAttribute('disabled')
        valid = true
    } else {
        button.setAttribute('disabled', 'true')
        valid = false
    }
}

// add event listeners to check validity when input field changes
nameInput.addEventListener('input', checkValidity)
checkboxes.forEach(el => el.addEventListener('change', checkValidity))

button.addEventListener('click', () => {
    if (valid) {
        // detect checked boxes on button click
        const checked = Array.from(checkboxes).filter(el => el.checked)
        checked.forEach(el => {

            // increment vote tally for each checked item
            const tallyBox = document.getElementById(el.value)
            tallyBox.innerText++
        })
        voters.push(nameInput.value)
    }

    // clear values
    checkboxes.forEach(el => el.checked = false)
    nameInput.value = ''
})
