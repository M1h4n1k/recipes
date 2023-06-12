<template>
	<div>
		<h1 class="text-2xl font-medium">
			Admin
		</h1>
		<input class="text-black w-96 border rounded px-2 py-1 mt-2" placeholder="Admin key" v-model="adminKey">
	</div>
	<hr class="my-2">
	<div>
		<h1 class="text-2xl font-medium">
			Add ingredient
		</h1>
		<div class="flex h-full items-center space-x-2 mt-2 ml-2">
			<div class="flex flex-col items-end justify-center">
				<div>
					Name: <input class="text-black w-96 h-10 border rounded px-2 py-1 mt-2" placeholder="Name..." v-model="ingredient.name">
				</div>
				<div>
					Unit: <input class="text-black w-96 h-10 border rounded px-2 py-1 mt-2" placeholder="Unit..." v-model="ingredient.unit">
				</div>
				<div class="w-full flex justify-center items-center">
					<button class="w-52 h-12 mt-2 border rounded-lg bg-[#EE4266] text-white font-semibold" @click="addIngredient">Submit</button>
				</div>
			</div>
			<span>{{ response }}</span>
		</div>

	</div>
</template>

<script>
import UploadImageIcon from "@/components/icons/UploadImageIcon.vue";
import config from "@/config";

export default {
	name: "Admin",
	components: {UploadImageIcon},
	data() {
		return {
			adminKey: "",
			ingredient: {
				name: "",
				unit: ""
			},
			response: ''
		}
	},
	methods: {
		addIngredient(){
			fetch(`${config.API_URL}/ingredients?admin_key=${this.adminKey}`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify(this.ingredient)
			}).then(res => res.json()).then(res => {
				this.response = res;
				setTimeout(() => this.response = '', 3000);
				if(res.success){
					this.ingredient = {
						name: "",
						unit: "",
					}
				}
			})
		}
	}
}
</script>

<style scoped>
li > * {
	vertical-align: text-top;
}

#upload-photo {
	opacity: 0;
	position: absolute;
	z-index: -1;
}
</style>