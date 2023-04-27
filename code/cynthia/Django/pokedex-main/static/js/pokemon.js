
let app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], 

    data: {
      message: 'Hello world!',
      pokemon: [],
      types: [],
      caughtList:[],
    },

    methods: {
      getPokemon() {
        axios.get('api/v1/', {
            headers: {'X-CSRFToken': this.token }

        }).then(res => {
          this.pokemon = res.data
       
          // this.types = res.data.pokemon.type
        })
      },
      userCaught(p) {
        let index = this.pokemon.indexOf(p)
        this.pokemon.splice(index, 1)
        this.caughtList.push(p)

      }

      
    
    },
    created(){
      this.getPokemon()
    },
    computed:{
      getImgUrlFront(){
          console.log(this.pokemon)
    
          return `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${this.pokemon[0].number}.png`
        
      },
      getImgUrlBack(){
        console.log(this.pokemon)
        
        return `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/${this.pokemon[0].number}.png`
      }
    }
  })
 