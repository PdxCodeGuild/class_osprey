/* Conditionals */

const a = 0
const b = 1
const c = false
const d = true
const isFalse = a == b

console.log(a == b); // checks if values are the same
console.log(a === b); // checks values and types
console.log(a != b);
console.log(a !== b);

// and is &&
// or is ||

console.log(a && b); // 0
console.log(b && c); // false
console.log(b && d); // true
console.log(a || d); // true
console.log(a || c); // false
console.log(b && d || c); // true


if (isFalse) {
    console.log("this won't execute");
} else if (a <= b && true || !isFalse) {
    console.log("this will!");
} else { console.log("but not this") }

// Ternary operator
// [condition] ? [output if true] : [output if false]

let valA
if (a > b) {
    valA = 'thing1'
} else {
    valA = 'thing2'
}

valB = a > b ? 'thing1' : 'thing2'

console.log(valA, valB);


// Assign complex conditions to a variable for readability

isOnSaleToday = a > b && c || !isFalse && a === c

if (isOnSaleToday) {
    console.log('do something based on a complex condition');
}

