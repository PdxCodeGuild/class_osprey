
new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        pokemon: [],
        token: '',
        currentUser: {},
        caughtPokemon: [],
        type: 'normal',
    },
    methods: {
        getPokemon() {
            axios.get('/api/')
            .then(response => {
                this.pokemon = response.data
            })
        },
        getCurrentUser() {
            axios.get('/api/current/')
            .then(response => {
                this.currentUser = response.data
            })
        },
        catchPokemon(poke) {
            let match = this.currentUser.caught.includes(poke.id)
            if (!match) {
                this.caughtPokemon.push(poke.name)
                this.currentUser.caught.push(poke.id)
                axios.patch(`/api/user/${this.currentUser.id}/`, {
                    'caught': this.currentUser.caught
                }, {
                    headers: { 'X-CSRFToken': this.token }
                })
            }
        },
        releasePokemon(poke) {
            // find indexOf and splice out
            const match = this.currentUser.caught.find(el => el === poke.id)
            const index = this.currentUser.caught.indexOf(match)
            if (index !== -1) {
                this.currentUser.caught.splice(index, 1)
                axios.patch(`/api/user/${this.currentUser.id}/`, {
                    'caught': this.currentUser.caught
                }, {
                    headers: { 'X-CSRFToken': this.token }
                }).then(() => this.getCurrentUser())
            }
            
        },
        hasPokemon(poke) {
            let match = this.currentUser.caught.includes(poke.id)
            return match
        }
    },
    computed: {
        hasCaughtPokemon() {
            if (this.currentUser.caught.length > 0) {
                return true
            }
            return false
        },
    },
    mounted() {
        this.getPokemon()
        this.getCurrentUser()
        this.token = document.querySelector('input[name=csrfmiddlewaretoken]').value
    },
})