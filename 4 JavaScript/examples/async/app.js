const printStrings = () => {
    console.log('thing 1');
    setTimeout(() => console.log('thing 2'), 2000)
    console.log('thing 3');
}

// printStrings()

const examplePromise = new Promise((resolve, reject) => {
    if (true) {
        setTimeout(() => { resolve('promise resolved') }, 1000)
    } else {
        reject('promise rejected :(')
    }
})

const secondPromise = () => {
    return new Promise((rslv, rjct) => rslv('this one always resolves'))
}

console.log(examplePromise);

examplePromise
    .then(result => console.log(result))
    .then(secondPromise)
    .then(msg => console.log(msg))
    .then(() => console.log('you can do anything in a .then'))
    .catch(err => console.log(`caught the error: ${err}`))


// Async / await are syntactic sugar for Promises

// the async keyword makes this function automatically return a Promise
async function exampleAsync() {
    return 1
}

// exampleAsync().then(msg => console.log(msg))

const exampleAwait = async () => {
    try {
        return await exampleAsync()
    } catch (err) {
        return 'something went wrong'
    }
}

console.log(exampleAwait());

exampleAwait()
    .then(msg => console.log(msg))
