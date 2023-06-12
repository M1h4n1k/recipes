import Explore from "@/Routes/Explore.vue";
import Create from "@/Routes/Create.vue";
import Recipe from "@/Routes/Recipe.vue";
import Fridge from "@/Routes/Fridge.vue";

import {createRouter, createWebHistory} from "vue-router";
import Admin from "@/Routes/Admin.vue";

const routes = [
	{ path: '/', component: Explore },
	{ path: '/recipe/:id', component: Recipe },
	{ path: '/create', component: Create },
	{ path: '/fridge', component: Fridge },
	{ path: '/admin', component: Admin }
]

const router = createRouter({
	history: createWebHistory(),
	routes,
})

export default router
