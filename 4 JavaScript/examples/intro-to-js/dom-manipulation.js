const header = document.querySelector('h2')
// returns first instance of an element matching a css selector

header.innerText = 'Class Osprey <i>rules</i>'
header.innerHTML = 'Class Osprey <i>rules</i>'

console.log(header);

const people = document.querySelectorAll('li')
// returns a NodeList containing each element that matches a css selector
console.log(people);

for (person of people) {
    if (person.innerText == 'Danny') {
        person.classList.add('staff')
        person.classList.remove('inactive')
    }
    if (person.innerText == 'James') {
        person.classList.replace('inactive', 'staff')
    }
}

// const staff = document.querySelectorAll('.staff')
const staff = document.getElementsByClassName('staff')

for (el of staff) {
    el.style.fontWeight = '900'
}

// const subHeader = document.querySelector('#people-header')
const subHeader = document.getElementById('people-header')
subHeader.innerText = 'People in Class Osprey'

// Change HTML attributes
console.log(header.hasAttribute('name')) // false
console.log(header.getAttribute('name')) // null
console.log(header.getAttribute('id')) // label

header.setAttribute('name', 'cohort name')
console.log(header.getAttribute('name')) // cohort name

header.removeAttribute('name')
console.log(header.getAttribute('name')) // null


// Create and add a new element

const quote = document.createElement('blockquote')
quote.innerText = "Beer is proof that god loves us -Benjamin Franklin"
console.log(quote);

const body = document.querySelector('body')
console.log(body);

body.appendChild(quote)


const newThing = document.createElement('XYZ-A')
newThing.innerText = 'will THIS show up?'
body.appendChild(newThing)

newThing.remove()