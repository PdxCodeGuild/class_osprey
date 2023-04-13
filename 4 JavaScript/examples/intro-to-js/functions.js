/* FUNCTIONS */

// standard function declaration

function add(x, y) {
    return x + y
}
console.log(add(1, 2))


const subtract = function (x, y) {
    return x - y
}
console.log(subtract(3, 2));
console.log(add)

// ES6 arrow function, rocket function

const multiply = (x, y) => x * y

const divide = (x, y) => {
    // this line introduces complexity
    return x / y
}

console.log(multiply(3, 6));
console.log(divide(3, 6));


// CALLBACKS
// callbacks are functions that are passed as arguments to other functions
// they don't have to be anonymous, but usually are
// (anonymous functions don't have names)

let numArray = [1, 2, 3, 4, 5]

const filterHelper = (x) => {
    if (x > 2) {
        return true
    }
    return false
}

// the function that gets passed to another function is the "callback"
const filteredArray = numArray.filter(filterHelper)
console.log(filteredArray);


// the same thing, written as an anonymous callback
const filteredArray2 = numArray.filter(x => x > 2)
console.log(filteredArray2);

// anonymous callbacks can be as complex as you want
const filteredArray3 = numArray.filter(x => {
    console.log("this function might do more stuff");
    return x > 2
})
console.log(filteredArray3);