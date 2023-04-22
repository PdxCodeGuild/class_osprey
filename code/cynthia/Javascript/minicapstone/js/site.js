// const {Geocoder} = await google.maps.importLibrary("geocoding");


new Vue({
    el: '#app',

    data() {
        return{
            output: {},
            googleResult:{},
            userAddress:'',
            message: 'Have a good day',
            x: document.getElementById('location'),
            lat:'',
            lng:'',

        }
        

       
    },

    methods:{

        getForcast() {
            axios.get('https://api.breezometer.com/pollen/v2/forecast/daily', {
                params: {
                    lat: '38.5815719',
                    lon: '-121.4943996',
                    days: '1',
                    key: appKey,
                    metadata: true,
                    plants: true,
                   
                },
            }).then(response => {this.output = response.data}).catch(err => console.error(err))
            
        },

        getLocation() {
            axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
                params: {
                    address: 'sacramento, california',
                    key: googleKey,
                },
            }).then(response => {this.googleResult = response.data.results[0].geometry.location}).catch(err => console.error(err))
        },
        // onChange(e) {
        //     this.userAddress = this.googleResult.find(l => this.userAddress = l.lat) 
        //     console.log(userAddress)

        // },
      
    }


})
