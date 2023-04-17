const submitButton = document.querySelector('input[type="submit"]')
const submitText = document.querySelector("input[type = 'text']")
const activeList = document.querySelector("#active-list")
const completedList = document.querySelector('#completed-list')

let itemsArray = localStorage.getItem('submitText') ? JSON.parse(localStorage.getItem('submitText')) : [];

const addItems = (item) => {
    const listItem = document.createElement('li')
    listItem.innerText = item.name
    const todoCheck = document.createElement('input')
    todoCheck.type = 'checkbox'
    todoCheck.checked = item.isDone
    listItem.appendChild(todoCheck)

    if (!item.isDone) {
        activeList.appendChild(listItem)
    } else {
        completedList.appendChild(listItem)
    }

    todoCheck.addEventListener('change', () => {
        let index = itemsArray.indexOf(item)
        if (!todoCheck.checked) {
            activeList.appendChild(listItem)
        } else {
            completedList.appendChild(listItem)
        }
        item.isDone = !item.isDone
        itemsArray.splice(index, 1, item)
        localStorage.setItem('submitText', JSON.stringify(itemsArray))
    })
}

for (item of itemsArray) {
    addItems(item)
}

submitButton.addEventListener('click', () => {
    const newItem = {
        name: submitText.value,
        isDone: false
    }
    itemsArray.push(newItem)
    localStorage.setItem('submitText', JSON.stringify(itemsArray))

    addItems(newItem)
    submitText.value = ''
})


