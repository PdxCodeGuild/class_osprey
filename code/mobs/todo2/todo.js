
const submitButton = document.querySelector('input[type="submit"]')
const submitText = document.querySelector("input[type = 'text']")

const activeList = document.querySelector("#active-list")
const completedList = document.querySelector('#completed-list')





submitButton.addEventListener('click',()=>{
    const listItem = document.createElement('li')
 

    listItem.innerText = submitText.value
    const todoCheck = document.createElement('input')
    listItem.appendChild(todoCheck)
    todoCheck.type = 'checkbox'
    activeList.appendChild(listItem)

    todoCheck.addEventListener('change',() => {
        if (!todoCheck.checked) {
            activeList.appendChild(listItem)
       
        } else{
            completedList.appendChild(listItem)
        }
       })

    todoCheck.id = submitText.value

})




// for (item of AlllistItems){
//     const todoCheck = document.createElement('input')
//     todoCheck.type = 'checkbox'
//     item.appendChild(todoCheck)
// }



