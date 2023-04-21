new Vue({
    el:'#app',
   
    data() {
        return {
            output: {},
            newImage: {},
            message: 'Weather Wiz',
            userLocation: {},
            locationString: '',
            
            locations: [
                {location:'Sacramento, Ca', lat: '38', lon: '-122'},
                {location:'Portland, Or', lat:'45', lon: '-122' },
                {location:'Fairbanks, Ak', lat:'64', lon:'-147'}
            ],

        }
  
    },


    methods: {
        getInput() {
            axios.get('https://api.openweathermap.org/data/2.5/weather', {
                params: {
                    lat: this.userLocation.lat,
                    lon: this.userLocation.lon,
                    appid: appkey,
                    units: 'imperial' },
                }).then(response => {this.output = response.data}).catch(err => console.error(err))
              
            },

        onChange(e) {
            this.userLocation = this.locations.find(l => this.locationString == l.location) 
        },

        // getImage() {
        //     axios.get('http://openweathermap.org/img/'), {
        //         params: {
        //             icon: this.output.icon,
        //         },
        //     }.then(response=> {this.newImage = response}).catch(err => console.error(err))
        // }
    }
})



// response.data.weather[0]