Vue.component('WeatherDetail', {
    template: `<div id="weather-display">
    <fieldset class="weather-card">
        <legend><h2>{{ output.name }} Weather [ {{ output.sys.country }} ]</h2></legend>
        <div id='weathertime'>
            <div>
                <img :src="getImg" alt="weather icon">
            </div>
            <div class="timelog">
                as of {{ getDate }}
            </div>
        </div>
        <div id='weather-details'>
            <div id="description">
                <p>
                    <span class="title">{{ weather.main }}: </span> {{ weather.description }}
                </p>
                <p>
                    <span class="title">Wind: </span> {{ output.wind.speed }}mph
                </p>
                <p>
                    <span class="title">Humidity: </span> {{ output.main.humidity }}%
                </p>
            </div>
            <fieldset id="temp-details">
                <legend><span class="title">Temp: {{ output.main.temp }}° </span></legend>
                <p>
                    <span class="title">Feels like: </span> {{ output.main.feels_like }}°
                        <li> low: {{ output.main.temp_min }}° </li>
                        <li> high: {{ output.main.temp_max }}° </li>
                </p>
            </fieldset>
        </div>
    </fieldset>
</div>`,
    props: ['output', 'weather'],
    data: () => {
        return {
            getImg: getImg(),
            todayDate: getDate(),
        }
    },
    computed: {
        getImg() {
            let code = this.weather.icon
            return `http://openweathermap.org/img/wn/${code}.png`
        },
        getDate() {
            let datetime = new Date()
            return this.todayDate = datetime.toLocaleDateString()
        }
    }
})

new Vue({
    el: '#app',
    data() {
        return {
            output: {},
            weather: {},
            city: 'portland',
        }
    },
    methods: {
        getWeather() {
            let latitude = 45.5152
            let longitude = -122.6784
            if (this.city === 'boston') {
                latitude = 42.3601
                longitude = -71.0589
            } else if (this.city === 'chicago') {
                latitude = 41.8781
                longitude = -87.6298
            } else if (this.city === 'sydney') {
                latitude = -33.8688
                longitude = 151.2093
            } 
            axios.get('https://api.openweathermap.org/data/2.5/weather', {
                params: { 
                    lat: latitude,
                    lon: longitude,
                    appid: '24b0de213ece79dc6fc5a352f5904e7c',
                    units: 'imperial'
                },
            }).then(response => {
                this.output = response.data
                this.weather = response.data.weather[0]
            }).catch(err => console.error(err))
        }
    },
    created() {
        this.getWeather()
    },
})