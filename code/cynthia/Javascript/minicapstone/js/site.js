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
            lat:'',

        }
        

       
    },

    methods:{

        getForcast() {
            axios.get('https://api.breezometer.com/pollen/v2/forecast/daily', {
                params: {
                    lat: '31',
                    lon: '-99',
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
                    address: 'Auburn, California',
                    key: googleKey,
                },
            }).then(response => {this.googleResult = response.data.results[0].location}).catch(err => console.error(err))
        },
        Geocoder(){

        }
      
    }


})
