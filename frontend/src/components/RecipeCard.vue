<template>
	<router-link :to="'/recipe/' + recipe['_id']" class="w-full p-5 border rounded-xl hover:bg-[#c1d3fe] hover:text-white bg-white hover:cursor-pointer select-none relative">
		<img :src="recipe['image']" alt="img" class="h-24 float-left mr-2 rounded border">
		<div>
			<h1 class="text-2xl font-semibold">{{ recipe['title'] }}</h1>
			<p>{{ recipe['description'] }}</p>
		</div>
		<span class="absolute right-2 bottom-2" :class="completeness">{{ recipe['completeness'] }}%</span>
	</router-link>
</template>

<script>
export default {
	name: "RecipeCard",
	props: {
		recipe: {
			type: Object,
			default: () => {
				return {}
			}
		}
	},
	computed: {
		completeness() {
			if (this.recipe['completeness'] < 50) return "text-red-500"
			if (this.recipe['completeness'] < 75) return "text-yellow-500"
			return "text-green-500"
		}
	}
}
</script>

<style scoped>

</style>