new Vue({
    el: '#app',
    data: {
        todoNew: '',
        todoList: [],
        taskType: 'unselected',
        counter: 0,
        doneCounter: 0,
    },

    methods: {
        addItem() {
            this.todoList.push({name: this.todoNew, isDone: false, type: this.taskType })
            this.todoNew = ''
        },
        isComplete(e) {
            e.isDone = !e.isDone
        },
        removeItem(e) {
            let index = this.todoList.indexOf(e)
            this.todoList.splice(index, 1)
        },

    },

    computed: {
        itemsToDo() {
            this.counter = 0
            for (task of this.todoList) {
                if (!task.isDone) {
                    this.counter++
                }
            }
            return this.counter
        },
        itemsDone() {
            this.doneCounter = 0
            for (task of this.todoList) {
                if (task.isDone) {
                    this.doneCounter++
                }
            }
            return this.doneCounter
        }
    }
})