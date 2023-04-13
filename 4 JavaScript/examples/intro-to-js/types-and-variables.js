console.log('this is how you print stuff')
console.error('this is an error')
console.log('stuff still happens after errors');

// snake_case
// kebab-case
// WordCase or PascalCase
// camelCase // JS uses this one


/* 
Declaring Variables
*/

var varName = 'whatever' // var is outdated, don't use it

let firstName = 'Danny' // let is for variables that might change
const lastName = 'Burrow' // const is for variables that won't change

firstName = 'Dan'
// lastName = 'something else' //Uncaught TypeError: Assignment to constant variable

let newVar
console.log(newVar);
// console.log(newThing) // Uncaught ReferenceError: newThing is not defined

/* 
TYPES
*/

// Primitive Types
let a = 'string'
let b = `template literals are like python's f-${a}s`
console.log(b);
let c = 1 // number
let d = 1.5 // number
let e = 309834509345098345098309458309458309458304958n //bigint
let f = true
let g = false
let h = null // there is a value, it's nothing
let i = undefined // there is no value 

// Reference Types

let j = [1, 2, 'three', { 'key': 'val' }, true] // array
let k = { key: 'this is the value', key2: [1, 2, 3] } //object
console.log(j);
console.log(k);

let l = new Set() // create an empty set, and then add things to it
l.add(1)
l.add('beans')
l.add(1)
console.log(l);

function myFunc(param1, param2) {
    return param1 + param2
}


/*
Type Conversion and Type Coercion

dynamically typed: variables can change types (type is determined at runtime)
weakly typed: types can be coerced, JS will try to interpret any operation on any type
*/

let m = parseInt('2')
let n = parseFloat('2.5')
let o = m.toString()

console.log(m == o) // true: these have equivalent values
console.log(m === o) // false: these (don't) have equivalent values AND the same type

console.log(m != o) // false
console.log(m !== o) // true
