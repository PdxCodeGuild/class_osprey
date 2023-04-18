

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

        toggleDone(item) {
            {"isDone = !isDone"}
            // change status to true, find it in the todolist, replace
           
        
            for (t in this.todoList) {
                t = this.todoList.indexOf(this.t)
                this.status= !status
                this.todoList[t].splice(index, 1, true)
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