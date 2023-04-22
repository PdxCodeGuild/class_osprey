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
            latString:'',
            lngString:'',
            daysString:'',
          
        }
        

       
    },

    methods:{

        getForcast() {
            axios.get('https://api.breezometer.com/pollen/v2/forecast/daily', {
                params: {
                    lat: this.latString,
                    lon: this.lngString,
                    days: this.daysString,
                    key: appKey,
                    metadata: true,
                    plants: true,
                   
                },
            }).then(response => {this.output = response.data}).catch(err => console.error(err))
            console.log(this.daysString)
            
        },

        getLocation() {
            axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
                params: {
                    address: this.userAddress,
                    key: googleKey,
                },
            }).then(response => {this.googleResult = response.data.results[0].geometry.location}).catch(err => console.error(err))
           
        },


        // onChange(e) {
        //     this.userAddress = this.googleResult.find(l => this.userAddress = l.latString) 
        //     this.userAddress = this.googleResult.find(l => this.userAddress = l.lngString) 

        // },

        changeDay(e) {
            this.daysString = e.target.value
            
        },
      
     
    }


})
