const submitButton = document.querySelector('input[type="submit"]')
const submitText = document.querySelector("input[type = 'text']")

const activeList = document.querySelector("#active-list")
const completedList = document.querySelector('#completed-list')

let itemsArray = localStorage.getItem('submitText') ? JSON.parse(localStorage.getItem('submitText')) : [];
console.log(itemsArray)
localStorage.setItem('submitText', JSON.stringify(itemsArray));
const data = JSON.parse(localStorage.getItem('submitText'));
console.log(data)

const addItems = (item) => {
    const listItem = document.createElement('li')
    listItem.innerText = item.name
    const todoCheck = document.createElement('input')
    listItem.appendChild(todoCheck)
    todoCheck.type = 'checkbox'
    activeList.appendChild(listItem)

    todoCheck.addEventListener('change',() => {
        let index = itemsArray.indexOf(item)
        if (!todoCheck.checked) {
            activeList.appendChild(listItem)
            item.isDone = false
            itemsArray.splice(index, 1, item)
            localStorage.setItem('submitText', JSON.stringify(itemsArray))
        } else{
            completedList.appendChild(listItem)
            item.isDone = true
            itemsArray.splice(index, 1, item)
            localStorage.setItem('submitText', JSON.stringify(itemsArray))
        }
       })
}

for (item of data) {
    addItems(item)
}
submitButton.addEventListener('click',()=>{
    const newItem = {
        name : submitText.value,
        isDone: false
    }
    itemsArray.push(newItem)
    localStorage.setItem('submitText', JSON.stringify(itemsArray))
    
    addItems(newItem)
    submitText.value = ''
})


