Vue.component('StudentInfo', {
    template: `
        <fieldset class="studentdetails">
        <legend class="name">{{ student.first_name }} {{ student.last_name }}</legend>
        
        <div class="delete">
            <button @click="$emit('delete-student', student)">✖</button>
        </div>

        <dl class="info">
            <dt>Cohort</dt>
                <dd>{{ student.cohort }}</dd>
            <dt>Favorite Topic</dt>
                <dd>{{ student.favorite_topic }}</dd>
            <dt>Favorite Teacher</dt>
                <dd>{{ student.favorite_teacher }}</dd>
            <dt>Capstone URL</dt>
                <dd><a :href="student.capstone">Click!</a></dd>
        </dl>
        
        <details class="edit">
        <summary>EDIT THIS INFO</summary>
        <p>First Name: <input type="text" v-model="$parent.changeFirst"> </p>
        <p>Last Name: <input type="text" v-model="$parent.changeLast"> </p>
        <p>Cohort Name: <input type="text" v-model="$parent.changeCohort"> </p>
        <p>Favorite Topic: <input type="text" v-model="$parent.changeFavThing"> </p>
        <p>Favorite Teacher: <input type="text" v-model="$parent.changeFavTeacher"> </p>
        <p>Capstone URL: <input type="text" v-model="$parent.changeCapstone"> </p>
        <p> <button @click="edit">SAVE</button> </p>
        </details>
        </fieldset>
    `,
    props: ['student'],
    methods: {
        edit() {
            this.$parent.editStudent(this.student)
        },
    }
})

new Vue({
    el: '#app',
    data: {
        students: [],
        token: '',
        newFirstName: '',
        newLastName: '',
        newCohort: '',
        newFavThing: '',
        newFavTeacher: '',
        newCapstone: '',
        changeFirst: undefined,
        changeLast: undefined,
        changeCohort: undefined,
        changeFavThing: undefined,
        changeFavTeacher: undefined,
        changeCapstone: undefined,
        searchPhrase: undefined
    },
    methods: {
        getStudents() {
            axios.get('/api/')
            .then(res => this.students = res.data)
        },
        addStudent() {
            axios.post('api/new/', {
                'first_name': this.newFirstName,
                'last_name': this.newLastName,
                'cohort': this.newCohort,
                'favorite_topic': this.newFavThing,
                'favorite_teacher': this.newFavTeacher,
                'capstone': this.newCapstone,
            }, {
                headers: { 'X-CSRFToken': this.token }
            }).then(() => this.getStudents())
            this.newFirstName = '',
            this.newLastName = '',
            this.newCohort = '',
            this.newFavThing = '',
            this.newFavTeacher = '',
            this.newCapstone = ''
        },
        editStudent(student) {
            console.log(student)
            axios.patch(`api/${student.id}/${student.first_name}/`, {
                'first_name': this.changeFirst,
                'last_name': this.changeLast,
                'cohort': this.changeCohort,
                'favorite_topic': this.changeFavThing,
                'favorite_teacher': this.changeFavTeacher,
                'capstone': this.changeCapstone,
            }, {
                headers: { 'X-CSRFToken': this.token }
            }).then(() => this.getStudents())
            this.changeFirst = undefined,
            this.changeLast = undefined,
            this.changeCohort = undefined,
            this.changeFavThing = undefined,
            this.changeFavTeacher = undefined,
            this.changeCapstone = undefined
        },
        deleteStudent(student) {
            axios.delete(`api/${student.id}/${student.first_name}`, {
                headers: { 'X-CSRFToken': this.token }
            }).then(() => this.getStudents())
        },
        searchStudents(search) {
            axios.get(`api/search`, {
                params: { first_name: search },
                headers: { 'X-CSRFToken': this.token }
            }).then(res => this.students = res.data)
            this.searchPhrase = undefined
        }
    },
    mounted() {
        this.getStudents()
        this.token = document.querySelector('input[name=csrfmiddlewaretoken]').value
    }
})