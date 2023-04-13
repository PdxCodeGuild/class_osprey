/* LOOPS

There are a LOT of ways to loop in JS
*/

// old school, classic, weird
for (let i = 1; i <= 5; i++) {
    console.log(i);
}

// vanilla while loop
let i = 0
while (i < 5) {
    i++
    console.log(i);
}

// ITERATING OVER AN ARRAY

const numArray = [1, 2, 3, 4, 5]

// old school 
for (let i = 0; i < numArray.length; i++) {
    console.log(numArray[i]);
}

// with a while loop
let x = 0
while (x < numArray.length) {
    x++
    console.log(numArray[x]);
}

// BETTER WAY!!
numArray.forEach(x => console.log(x)) // this is a function being passed in

// ANOTHER BETTER WAY!!
// for..of 
for (x of numArray) {
    console.log(x);
}

// map, filter, reduce
console.log("!!!!!!!!!!!!!!!!!!!!!");

const doubled = numArray.map(x => x * 2)
console.log(doubled);

const evens = numArray.filter((x) => !(x % 2))
console.log(evens);

const sum = numArray.reduce((x, y) => x + y)
console.log(sum);


// ITERATING OVER AN OBJECT

let myObj = {
    1: 'one',
    2: 'two',
    3: 'three'
}

// for..in
// loops over the keys
// this is the most straightforward, elegant way
for (thing in myObj) {
    console.log(thing);
    console.log(myObj[thing]);
}

// loop over keys with Object.keys()
for (thing of Object.keys(myObj)) {
    console.log(thing);
    console.log(myObj[thing]);
}

// loop over both keys and values with Object.entries()
for ([a, b] of Object.entries(myObj)) {
    console.log(a, b);
}

// or do that, using forEach
Object.entries(myObj).forEach(x => console.log(x[0], x[1]))
