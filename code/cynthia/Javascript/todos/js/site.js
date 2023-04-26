

new Vue({
    el: '#app',
    data: {
        message: 'Do All the Things!',
        todoList: [
            {task:'Check off your first task!', status: false}
        ],
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
            "isDone = !isDone"
            // this.status= !this.status
            for (this.t in this.todoList) {
                if (this.status= !this.status){
                    this.todoList.splice(t, true)
                    this.completedList.push(t)}
               
            }
        }
        
    },


    computed: {
        doneClass() {
            return {completed: this.isDone}
        }
    }
   
})

