Vue.component('StudentInfo', {
    template: `
        <fieldset class="studentdetails">
        <legend>{{ student.first_name }} {{ student.last_name }}</legend>
        
        <div class="delete">
            <button>✖</button>
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
        <p>First Name: [___] </p>
        <p>Last Name: [___] </p>
        <p>Cohort Name: [___] </p>
        <p>Favorite Topic: [___] </p>
        <p>Favorite Teacher: [___] </p>
        <p>Capstone URL: [___] </p>
        <p> <button>SAVE</button> </p>
        </details>
        </fieldset>
    `,
    props: ['student'],
})

new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        students: [],
        token: '',
        newFirstName: '',
        newLastName: '',
        newCohort: '',
        newFavThing: '',
        newFavTeacher: '',
        newCapstone: '',
    },
    methods: {
        getStudents() {
            axios.get('/api/')
            .then(res => this.students = res.data)
        }
    },
    mounted() {
        this.getStudents()
        this.token = document.querySelector('input[name=csrfmiddlewaretoken]').value
    }
})