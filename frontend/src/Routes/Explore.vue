<template>
	<div class="grid grid-cols-4 h-full gap-5">
		<RecipeCard v-for="r in recipes" :key="r['_id']" :recipe="r"></RecipeCard>
	</div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard.vue";
import config from "@/config.js";

export default {
	name: "Explore",
	props: {
		search: {
			type: String,
			default: ""
		}
	},
	components: {
		RecipeCard
	},
	data() {
		return {
			originalRecipes: []
		}
	},
	created() {
		fetch(`${config.API_URL}/recipes`, {
			credentials: 'include'
		})
			.then(res => res.json())
			.then(data => this.originalRecipes = data)
	},
	computed: {
		recipes() {
			if (this.search === "") return this.originalRecipes.sort((a, b) => b['completeness'] - a['completeness'])
			return this.originalRecipes.filter(r => r['title'].toLowerCase().includes(this.search.toLowerCase())).sort((a, b) => b['completeness'] - a['completeness'])
		}
	}
}
</script>

<style scoped>

</style>