

new Vue({
    el: '#app',
    data: {
        message: 'todo list',
        todoList: [
            {task:'feed dog', status: false},
            {task: 'water plants', status: false},
        ],

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
            "isDone = !isDone"
            // change status to true, find it in the todolist, replace
            this.status= !this.status
        
            for (this.t in this.todoList) {
                // t = this.todoList.indexOf(this.t)
                this.todoList.splice(t, true)
                this.todoList.appendChild(t)
                console.log(this.todoList)
            }
           
            //  t is one item in todolist, will have to update then save it back
        }
        
    },


    computed: {
        doneClass() {
            return {completed: this.isDone}
        }
    }
})