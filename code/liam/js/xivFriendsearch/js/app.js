new Vue({
    el: '#app',
    data: {
        searchResults: {},
        info: {},
        playerInfo: {},
        dataCenter: 'unselected',
        selectedServer: '',
        servers: {
            aether: ['Adamantoise',
                    'Cactuar',
                    'Faerie',
                    'Gilgamesh',
                    'Jenova',
                    'Midgardsormr',
                    'Sargantas',
                    'Siren'],
            crystal: ['Balmung',
                    'Brynhilder',
                    'Coeurl',
                    'Diabolos',
                    'Goblin',
                    'Malboro',
                    'Mateus',
                    'Zalera'],
            dynamis: ['Halicarnassus',
                    'Maduin',
                    'Marilith',
                    'Seraph'],
            primal: ['Behemoth',
                    'Excalibur',
                    'Exodus',
                    'Famfrit',
                    'Hyperion',
                    'Lamia',
                    'Leviathan',
                    'Ultros']
        },
        characterName: '',
        friendList: [],
        nextPageNum: null,
        prevPageNum: null,
        loading: false,
        showAllMinions: false,
        showAllMounts: false,
    },
    methods: {
        playerSearch(pageNum) {
            this.loading = true
            axios.get('https://xivapi.com/character/search', {
                params: {
                    name: this.characterName,
                    server: this.selectedServer,
                    page: pageNum,
                }
            }).then(response => {
                this.searchResults = response.data.Results
                this.info = response.data
                this.nextPageNum = response.data.Pagination.PageNext
                this.prevPageNum = response.data.Pagination.PagePrev
                this.loading = false
            })
            this.playerInfo = {}
        },
        playerDetails(id) {
            this.playerInfo = {}
            this.loading = true
            axios.get(`https://xivapi.com/character/${id}`, {
                params: {
                    data: 'FC,MIMO'
                }
            }).then(response => {
                this.playerInfo = response.data
                this.loading = false
                this.showAllMinions = false
                this.showAllMounts = false
            })
        },
        addFriend() {
            this.friendList.push(this.playerInfo)
        },
        deleteFriend(player) {
            const match = this.friendList.find(friend => friend.Character.ID === player.Character.ID)
            const index = this.friendList.indexOf(match)
            if (index !== -1) {
                this.friendList.splice(index, 1)
            }
        },
        verifyFriend() {
            let verify = this.friendList.find(friend => friend.Character.ID === this.playerInfo.Character.ID)
            return verify
        },
        nextPage() {
            return this.nextPageNum
        },
        prevPage() {
            return this.prevPageNum
        },
    },
})

Vue.component('PlayerTile', {
    template: `<div class="player-display" @click="$emit('select-tile', player.ID)">
            <span>{{ player.Name }}</span>
            <img :src="player.Avatar" class="player-icon" alt="player avatar">
            </div>`,
    props: ['player'],
})

Vue.component('AllFriends', {
    template: `<button @click="$emit('select-friend', friend.Character.ID)" 
            @mouseover="action = friend.Character.ID" @mouseleave="action = null"
            class="friend-button">
                {{ friend.Character.Name }}
                <div v-show="action === friend.Character.ID">
                    <img :src="friend.Character.Avatar" class="friend-icon" alt="your friend :)">
                </div>
            </button>`,
    props: ['friend'],
    data: () => {
        return {
            action: null,
        }
    }
})

Vue.component('ShowMinions', {
    template: `<img :src="minion.Icon" :alt="minion.Name" :title="minion.Name" class="mimo">`,
    props: ['minion'],
})

Vue.component('ShowMounts', {
    template: `<img :src="mount.Icon" :alt="mount.Name" :title="mount.Name" class="mimo">`,
    props: ['mount'],
})