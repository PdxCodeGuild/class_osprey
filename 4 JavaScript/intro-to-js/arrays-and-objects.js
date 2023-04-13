/*
ARRAYS

JS arrays are like Python lists
*/

let colors = ['red', 'blue', 'green']
colors.push('magenta', 'orange') // push appends to the end of an array

let popped = colors.pop() // pop removes from the end by default
console.log(colors, popped);

let shifted = colors.shift() // shift removes from the beginning
console.log(colors, shifted);

colors.unshift('pink')
console.log(colors);

console.log(colors[1]); // access by index just like python
// console.log(colors[1: 3]); // Uncaught SyntaxError: Unexpected token ':'
console.log(colors.slice(1, 3));
console.log(colors.slice(1)); // equivalent to colors[1:]

colors[1] = 'cerulean' // assign by index
colors[7] = 'brown' // will add empty indexes

console.log(colors);
console.log(colors.length);

delete colors[2] // delete a value and leave its index empty
console.log(colors);

let subList = colors.splice(1, 2, 'violet')
// remove 2 items starting at index 1, replace with 'violet', return the removed items
console.log(subList, colors);

magentaIndex = colors.indexOf('magenta')
// remove something from an array by its value
console.log(magentaIndex);
colors.splice(magentaIndex, 1)
console.log(colors);


console.log(colors.indexOf('green')); // indexOf returns -1 if it doesn't find it
if (colors.indexOf('green') !== -1) {
    colors.splice(colors.indexOf('green'), 1)
}

if (colors.indexOf('violet') !== -1) {
    colors.splice(colors.indexOf('violet'), 1)
}

console.log(colors);

/* 
OBJECTS

A JS objects is like a python dictionary AND like a python object
*/

const person = { firstName: 'Danny', lastname: 'Burrow' }

console.log(person['firstName'])
console.log(person.lastname)

person.title = 'instructor'
person['favFood'] = 'beans'
person['firstName'] = 'Dan'

console.log(person);

let pizza = {
    toppings: ['pineapple', 'death', 'olives', { sausage: 'chorizo' }],
    pizzeria: {
        name: 'EGPL',
        'phone number': 1234567890, // use a string for keys if the key is illegal
        staff: {
            owner: 'Mr. Bossman',
            chef: 'Remy',
            signWaver: 'Greg'
        }
    }
}

console.log(pizza.pizzeria.staff.chef); // Remy
// use bracket notation when the key is a string
console.log(pizza.pizzeria["phone number"]); //1234567890


//use bracket notation when using a variable in the path
const restaurant = 'pizzeria'
console.log(pizza[restaurant].staff.signWaver); // Greg

pizza.toppings.push('mushrooms')
console.log(pizza);

console.log(pizza.toppings[3].sausage);


// accessing keys of an object
const pizzaKeys = Object.keys(pizza.pizzeria.staff)
console.log(pizzaKeys);

for (const prop in pizza) {
    console.log(`${prop}: ${pizza[prop]}`);
}