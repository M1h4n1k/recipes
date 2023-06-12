<template>
	<div class="grid grid-cols-4 h-full gap-5 px-96">
		<IngredientCard v-for="(ing, i) of fridge" v-model:ingredient="fridge[i]" @delete="fridge.splice(i, 1)" :key="i"></IngredientCard>
		<div class="w-full h-20 p-5 border rounded-xl hover:bg-[#ccdbfd] hover:text-white hover:cursor-pointer select-none" @click="fridge.push({})">
			<img src="@/assets/add.png" alt="img" class="h-full w-auto float-left rounded mr-2">
			<div class="flex justify-between items-center h-full">
				Add new
			</div>
		</div>
	</div>
</template>

<script>
import IngredientCard from "@/components/IngredientCard.vue";
import IngredientNoLogo from "@/components/icons/UnknownIngredientIcon.vue";
import config from "@/config";

export default {
	name: "Fridge",
	components: {
		IngredientNoLogo,
		IngredientCard
	},
	data() {
		return {
			fridge: [null, null, null],
		}
	},
	async created() {
		if (this.$store.getters.getKnownIngredients.length === 0){
			await fetch(`${config.API_URL}/ingredients`)
				.then(response => response.json())
				.then(data => {
					this.$store.dispatch('updateKnownIngredients', data)
				})
		}

		await fetch(`${config.API_URL}/fridge`, {
			credentials: 'include'
		})
			.then(response => response.json())
			.then(data => {
				this.fridge = data
			})
	}
}
</script>

<style scoped>

</style>