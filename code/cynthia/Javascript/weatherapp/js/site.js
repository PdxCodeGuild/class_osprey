new Vue({
    el:'#app',
   
    data() {
        return {
            output: {},
            message: 'check the weather!',
            userLocation: {},
            locationString: '',
            
            locations: [
                {location:'Sacramento, Ca', lat: '38', lon: '-122'},
                {location:'Portland, Or', lat:'45', lon: '-122' },
                {location:'Fairbanks, Ak', lat:'64', lon:'-147'}
            ],
        
            // latitude: '38',
            // longitude:'-122',


        }
  
    },


    methods: {
        getInput() {
            console.log(this.latitude)
            axios.get('https://api.openweathermap.org/data/2.5/weather', {
                params: {
                    lat: this.userLocation.lat,
                    lon: this.userLocation.lon,
                    appid: appkey,
                    units: 'imperial' },
                }).then(response => {this.output = response.data.weather[0]}).catch(err => console.error(err))
              
            },
        onChange(e) {
            this.userLocation = this.locations.find(l => this.locationString == l.location) 
        

        },
        // weather() {
        //     this.getInput()
        // },
    }
})



// response.data.weather[0]