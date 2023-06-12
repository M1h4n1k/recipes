<template>
	<div class="w-full h-20 p-5 border rounded-xl hover:bg-[#ccdbfd] hover:text-white hover:cursor-pointer select-none relative">
		<img alt="delete" class="absolute w-3 top-0 right-0 m-2"
			 src="@/assets/delete.png"
			 @click="deleteIngredient"
		>
		<div class="flex justify-between items-center h-full" :class="{'animate-pulse': !ingredient}">
			<div v-if="!ingredient" class="h-3 w-32 bg-gray-300 rounded-lg"></div>
			<p v-else-if="ingredient['name'] && !changeName" class="text-lg" @dblclick="changeName = true">{{ ingredient['name'] }}</p>
			<div v-else>
				<input list="knownIngredients" id="ingredientName" class="text-black w-32 px-2 py-1 border rounded"
					   v-model="ingredient['name']"
					   @focusout="updateName"
				/>
				<datalist class="bg-red-100" id="knownIngredients">
					<option class="bg-red-100" v-for="ing in knownIngredients">{{ ing['name'].toString() }}</option>
				</datalist>
			</div>
			<div class="flex space-x-1">
				<div v-if="!ingredient" class="h-3 w-12 bg-gray-300 rounded-lg"></div>
				<p v-else-if="ingredient['quantity'] && !changeQuantity" @dblclick="changeQuantity = true">{{ ingredient['quantity'] }}</p>
				<input v-else :value="ingredient['quantity']" class="text-black w-14 text-right border rounded px-2 py-1" @focusout="updateQuantity">
				<span v-if="ingredient">{{ ingredient['unit'] }}</span>
			</div>

		</div>
	</div>
</template>

<script>
import UnknownIngredientIcon from "@/components/icons/UnknownIngredientIcon.vue";
import config from "@/config";

export default {
	name: "IngredientCard",
	emits: ["delete", "update:ingredient"],
	components: {UnknownIngredientIcon},
	props: {
		ingredient: {
			type: Object,
			default: null
		}
	},
	data() {
		return {
			knownIngredients: [],
			changeName: false,
			changeQuantity: false,
		}
	},
	created() {
		if (this.$store.getters.getKnownIngredients.length === 0){
			this.loadKnownIngredients()
		}
		this.knownIngredients = this.$store.getters.getKnownIngredients

		if(!this.ingredient)
			return
		this.changeName = !this.ingredient['name']
		this.changeQuantity = !this.ingredient['quantity']
	},
	methods: {
		loadKnownIngredients(){
			fetch(`${config.API_URL}/ingredients`)
				.then(response => response.json())
				.then(data => {
					this.$store.dispatch('updateKnownIngredients', data)
				})
		},
		updateName(e){
			if(this.knownIngredients.find(ing => ing['name'] === e.target.value)) {
				const knownIngredient = this.knownIngredients.find(ing => ing['name'] === e.target.value)
				this.ingredient['unit'] = knownIngredient['unit']
			}
			this.ingredient['name'] = e.target.value
			this.changeName = false
			this.updateIngredient()
		},
		updateQuantity(e){
			this.ingredient['quantity'] = e.target.value
			this.changeQuantity = false
			this.updateIngredient()
		},
		updateIngredient(){
			if(!this.ingredient['name'] || !this.ingredient['quantity'])
				return
			fetch(`${config.API_URL}/fridge`, {
				method:  this.ingredient['_id'] ? 'PATCH' : 'POST',
				credentials: 'include',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					_id: this.ingredient['_id'],
					name: this.ingredient['name'],
					quantity: this.ingredient['quantity'],
					unit: this.ingredient['unit'],
				})
			})
				.then(response => response.json())
				.then(data => {
					this.$emit('update:ingredient', this.ingredient)
				})
		},
		deleteIngredient(){
			fetch(`${config.API_URL}/fridge?_id=${this.ingredient['_id']}`, {
				method: 'DELETE',
				credentials: 'include'
			})
				.then(response => response.json())
				.then(data => {
					this.$emit('delete')
				})
		}
	},
}
</script>

<style scoped>

</style>