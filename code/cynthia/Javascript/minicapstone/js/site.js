// const {Geocoder} = await google.maps.importLibrary("geocoding");


new Vue({
    el: '#app',

    data() {
        return{
            output: {},
            userAddress:'',
            message: 'Summer Breeze',
            latString:'',
            lngString:'',
            displayAddress: '',
            daysString:'',
            startDate: '',
            endDate:'',
            grassTypes: '',
            treeTypes: '',
            weedTypes:'',
            grassSeason:'',
            treeSeason: '',
            weedSeason:'',
            grassSeverity:'',
            treeSeverity:'',
            weedSeverity:'',
            hasResults: false,
            bpi:'',
        }
        

       
    },

    methods:{

        getForcast() {
            console.log(this.latString, this.lngString)
            axios.get('https://api.breezometer.com/pollen/v2/forecast/daily', {
                params: {
                    lat: this.latString,
                    lon: this.lngString,
                    days: this.daysString,
                    key: appKey,
                    metadata: true,
                    plants: true,
                  
                   
                },
            }).then(response => {
             
                this.startDate = response.data.metadata.start_date
                this.endDate = response.data.metadata.end_date
                this.grassTypes = response.data.metadata.types.grass.plants[0]
                this.treeTypes = response.data.metadata.types.tree.plants.join(', ')
                this.weedTypes = response.data.metadata.types.weed.plants.join(', ')
                this.grassSeason = response.data.data[0].types.grass.in_season
                this.treeSeason = response.data.data[0].types.tree.in_season
                this.weedSeason = response.data.data[0].types.weed.in_season
                this.grassSeverity = response.data.data[0].types.grass.index.value
                this.treeSeverity = response.data.data[0].types.tree.index.value
                this.weedSeverity = response.data.data[0].types.weed.index.value
                this.bpi = response.data.data[0].index_id
            }).catch(err => console.error(err))
           
            
        },

        getLocation() {
            axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
                params: {
                    address: this.userAddress,
                    key: googleKey,
                },
            }).then(response => {
                this.googleResult = response.data.results[0].geometry.location
                this.latString = response.data.results[0].geometry.location.lat
                this.lngString = response.data.results[0].geometry.location.lng
                this.displayAddress = response.data.results[0].formatted_address
            }).catch(err => console.error(err))
           
        },


        changeDay(e) {
            this.daysString = e.target.value
        },
      

     
    }


})
