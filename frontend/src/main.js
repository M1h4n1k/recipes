import { createApp } from 'vue'
import { createStore } from 'vuex'

import App from './App.vue'
import router from './router'

import './index.css'

const store = createStore({
	state: {
		knownIngredients: []
	},
	mutations: {
		setKnownIngredients (state, ki) {
			state.knownIngredients = ki
		}
	},
	actions: {
		updateKnownIngredients({ commit }, data) {
			commit('setKnownIngredients', data)
		},
	},
	getters: {
		getKnownIngredients: (state) => state.knownIngredients
	}
})


createApp(App).use(store).use(router).mount('#app')
