new Vue({
    el: '#app',
    data: {
        cohortName: 'Class Osprey',
        gradDate: 'June 9',
        repo: 'https://github.com/PdxCodeGuild/class_osprey',
        clicks: 0,
        inputText: 'something',
        inputText2: '',
        students: [
            'Cynthia',
            'Liam',
            'Steve'
        ],
        staff: [
            {
                name: 'Danny',
                title: 'instructor',
                isActive: true
            },
            {
                name: 'James',
                title: 'TA',
                isActive: false
            }
        ],
        seasons: {
            spring: ['March', 'April', 'May'],
            summer: ['June', 'July', 'August'],
            fall: ['September', 'October', 'November'],
            winter: ['December', 'January', 'February']
        },
        a: 0,
        b: 0,
        isRed: false,
        isTransparent: false,
    },
    methods: {
        clicker(count) {
            this.clicks += count
        },
        logInput(e) {
            // e.target.value is the value of the element that generated the event
            this.inputText = e.target.value
        }
    },
    computed: {
        scoreA() {
            // do whatever JS you need to compute your property here
            return 42 + this.a
        },
        scoreB() {
            return 100 + this.b
        },
        activeStaff() {
            return this.staff.filter(x => x.isActive)
        },
        boxClasses() {
            return { boxRed: this.isRed, transparent: this.isTransparent }
        }
    }
})