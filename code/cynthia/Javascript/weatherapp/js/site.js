new Vue({
    el:'#app',
   
    data() {
        return {
            output: {},
            
            message: 'Weather Wiz',
            userLocation: {},
            locationString: '',
            
            locations: [
                {location:'Sacramento, Ca', lat: '38', lon: '-122'},
                {location:'Portland, Or', lat:'45', lon: '-122' },
                {location:'Fairbanks, Ak', lat:'64', lon:'-147'}
            ],
            newIcon: '',

        }
  
    },


    methods: {
        getInput() {
            axios.get('https://api.openweathermap.org/data/2.5/weather', {
                params: {
                    lat: this.userLocation.lat,
                    lon: this.userLocation.lon,
                    appid: appkey,
                    units: 'imperial', 
                },
                }).then(response => {this.output = response.data}).catch(err => console.error(err))
              
            },

        onChange(e) {
            this.userLocation = this.locations.find(l => this.locationString == l.location) 
           
        },



    },
    computed:{
        getImgUrl(){
            console.log(this.output.weather)
            return `http://openweathermap.org/img/wn/${this.output.weather[0].icon}.png`
            
        }

    }
})



