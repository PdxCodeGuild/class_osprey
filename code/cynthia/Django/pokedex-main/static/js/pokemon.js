
let app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], 

    data: {
      message: 'Hello world!',
      pokemon: [],
    },

    methods: {
      getPokemon() {
        axios.get('api/v1/', {
            headers: {'X-CSRFToken': this.token }

        }).then(res => {this.pokemon = res.data
        console.log(typeof res.data)})

        

        .then( console.log(this.pokemon))

      }
    
    },
    created(){
      this.getPokemon()
     

    }
  })
 