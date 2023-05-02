Vue.component('BookItem', {
    template: `
            <p class="bookcard" @click="checkOut" :class="{out: isCheckedOut}">
                <strong>{{ book.title }}</strong><br>
                {{ book.author }}<br>
                checked out {{ book.times_checked_out }} times
                <button @click="$emit('delete-book', book)">❌</button>
            </p>
    `,
    props: ['book'], // props are passed in from the parent
    methods: {
        checkOut() {
            this.$parent.checkOutBook(this.book)
        },
    },
    computed: {
        isCheckedOut() {
            // TODO: why doesn't this work?
            // return this.book.is_checked_out()
            return this.book.check_out_date > this.book.check_in_date
        }
    }
})

new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        info: 'this is in the vue state data',
        books: [],
        token: '',
        newTitle: '',
        newAuthor: '',
    },
    methods: {
        getBooks() {
            axios.get('/api/v1/').then(res => this.books = res.data)
        },
        removeBook(book) {
            axios.delete(`api/v1/${book.id}`, {
                headers: { 'X-CSRFToken': this.token }
            }).then(() => this.getBooks())
            console.log('remove')
        },
        addBook() {
            axios.post('api/v1/new/', {
                'title': this.newTitle,
                'author': this.newAuthor
            }, {
                headers: { 'X-CSRFToken': this.token }
            }).then(() => this.getBooks())
        },
        checkOutBook(book) {
            axios.patch(`/api/v1/${book.id}/checkout`, {
                'title': book.title,
                'author': book.author
            }, {
                headers: { 'X-CSRFToken': this.token }
            }).then(() => this.getBooks())
        }
    },
    mounted() {
        this.getBooks()
        this.token = document.querySelector('input[name=csrfmiddlewaretoken]').value

        // this is how you would get the info from your hidden input fields
        // if you were going to... but do you REALLY need to?
        console.log(document.querySelector('#data').value)
    }
})