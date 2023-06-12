<template>
	<div class="px-96 space-y-2 text-lg">
		<div class="w-full flex space-x-7 ">
			<img :src="recipe['image']" alt="img" class="h-52 rounded">
			<div>
				<h1 class="text-2xl font-semibold">
					{{ recipe['title'] }}
				</h1>
				<ul class="list-disc list-inside p-1 text-xl ">
					<li>Description</li>
					<li>Ingredients</li>
					<li>Recipe</li>
				</ul>
			</div>
		</div>
		<div class="space-y-4">
			<div>
				<h1 class="text-2xl font-medium">
					Description
				</h1>
				<p class="mx-10 mt-2 w-full">
					{{ recipe['description'] }}
				</p>
			</div>
			<div>
				<h1 class="text-2xl font-medium">
					Ingredients
				</h1>
				<div class="list-none mx-10 w-96 mt-2">
					<div class="w-full flex items-center" v-for="ing in recipe['ingredients']" :key="ing.name">
						{{ ing['name'] }}<span class="grow border-b mx-2"></span>{{ ing['quantity'] }}
					</div>
				</div>
			</div>
			<div>
				<h1 class="text-2xl font-medium">
					Recipe
				</h1>
				<ol class="list-decimal list-inside mx-10 space-y-5 mt-2 w-full">
					<li v-for="(v, i) of recipe['steps']" :key="i">
						{{ v['text'] }}
					</li>
				</ol>
			</div>
		</div>
	</div>
</template>

<script>
import config from "@/config.js";

export default {
	name: "Recipe",
	data() {
		return {
			recipe: {},
		}
	},
	created() {
		console.log(this.$route)
		if (this.$route['params']['recipe']) {
			this.recipe = this.$route['params']['recipe']
			console.log(this.recipe)
			return
		}
		fetch(`${config.API_URL}/recipe/${this.$route['params'].id}`)
			.then(response => response.json())
			.then(data => {
				this.recipe = data
			})
	}
}
</script>

<style scoped>

</style>