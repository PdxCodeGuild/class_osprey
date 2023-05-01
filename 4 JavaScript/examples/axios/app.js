// https://jsonplaceholder.typicode.com/

new Vue({
    el: '#app',
    data() {
        return {
            output: {}
        }
    },
    created() {
        this.getUsers()
    },
    updated() {
        console.log('app updated');
        // don't do anything that causes an update! 
        // this.getUsers()
    },
    methods: {
        getUsers() {
            // GET REQUEST
            console.log('GET Request');
            // params can be included in the optional second argument
            // which is an object, we call it to the "options arg
            // axios({
            //     method: 'get',
            //     url: 'https://jsonplaceholder.typicode.com/posts',
            //     params: { id: 3 },
            //     headers: {}
            // })
            axios.get('https://jsonplaceholder.typicode.com/posts', {
                params: { id: 3 },
                headers: {}
            }).then(response => {
                // whatever complexity is needed
                this.output = response
            }).catch(err => console.error(err))

        },
        addUser() {
            // POST REQUEST
            console.log('POST Request');
            axios.post('https://jsonplaceholder.typicode.com/posts', {
                userId: 4,
                title: 'new post',
                body: 'this is our new post',
                garbage: ':)'
            }).then(res => this.output = res).catch(err => console.error(err))
        },
        updateUser() {
            // PUT/PATCH REQUEST
            // PUT replaces the entire record
            // PATCH only changes the specified keys on the record
            console.log('PUT Request');
            axios.put('https://jsonplaceholder.typicode.com/posts/1', {
                userId: 4,
                title: 'new post',
                garbage: ':)'
            }).then(res => this.output = res).catch(err => console.error(err))
        },
        removeUser() {
            // DELETE REQUEST
            console.log('DELETE Request');
            axios.delete('https://jsonplaceholder.typicode.com/posts/1')
                .then(res => this.output = res).catch(err => console.error(err))
        }
    }
})
