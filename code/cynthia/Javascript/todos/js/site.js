

new Vue({
    el: '#app',
    data: {
        message: 'Do All the Things!',
        todoList: [{task:'Check off your first task!', status: false}],
        completedList: [],
        inputText: '',
        isDone: false,
    },


    methods:{
        logInput() {
            this.todoList.push(
                {task: this.inputText, 
                    status: false})
                   
        },


        toggleDone(t) {
            // "isDone = !isDone"
            // this.status= !this.status
            let index = this.todoList.indexOf(t)
            this.todoList.splice(index, 1)
            this.completedList.push(t)
            console.log(this.completedList)

        }
    },
})

