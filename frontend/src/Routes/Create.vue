<template>
	<div class="px-96 space-y-2 text-lg">
		<div class="w-full flex space-x-7 relative">
			<div class="relative h-52 w-96 rounded bg-gray-200 flex items-center justify-center"
			:class="{'border border-red-400': submitted && !image}">
				<label for="upload-photo" class="cursor-pointer absolute" :class="{'top-0 right-0 m-2': image}">
					<UploadImageIcon v-if="!image"></UploadImageIcon>
					<img v-else alt="change" class="h-10" src="@/assets/changeImage.png">
				</label>
				<img v-if="image" :src="image" alt="" class="h-52 rounded">
				<input id="upload-photo" type="file" accept="image/jpeg" @change="uploadImage">
			</div>
			<div>
				<input class="text-2xl text-black w-96 border rounded px-2 py-1" placeholder="Title" v-model="title"
					   :class="{'border-red-400': submitted && title.length === 0}">
				<ul class="list-disc list-inside p-1 text-xl ">
					<li>Description</li>
					<li>Ingredients</li>
					<li>Recipe</li>
				</ul>
			</div>
		</div>
		<div class="space-y-4 w-full">
			<!-- Description -->
			<div>
				<h1 class="text-2xl font-medium">
					Description
				</h1>
				<div class="px-10 mt-2">  <!-- https://stackoverflow.com/questions/13322789/display-a-div-width-100-with-margins -->
					<textarea placeholder="Description of the dish..." class="p-2 w-full h-40 resize-none border rounded" v-model="description"
							  :class="{'border-red-400': submitted && description.length === 0}"></textarea>
				</div>
			</div>
			<!-- Ingredients -->
			<div>
				<h1 class="text-2xl font-medium">
					Ingredients
				</h1>
				<div class="list-none mx-10 w-96 mt-2">
					<div class="w-full flex items-center space-y-2 relative" v-for="(ing, i) of ingredients" :key="i">
						<input class="text-black w-44 border rounded px-2 py-1" placeholder="Name..." v-model="ingredients[i]['name']"
							   :class="{'border-red-400': submitted && (!ing['name'] || ing['name'].length === 0)}">
						<span class="grow border-b mx-2"></span>
						<input class="text-black w-24 border rounded px-2 py-1 text-right" placeholder="Amount..." v-model="ingredients[i]['quantity']"
							   :class="{'border-red-400': submitted && (!ing['quantity'] || ing['quantity'].length === 0)}">
						<img alt="delete" class="h-7 -right-10 absolute hover:cursor-pointer"
							 @click="ingredients.splice(i, 1)"
							 src="@/assets/delete.png">
					</div>
					<div class="w-full flex justify-end">
						<button class="w-44 mt-2 button" @click="ingredients.push({})">Add ingredient</button>
					</div>
				</div>
			</div>
			<!-- Recipe -->
			<div>
				<h1 class="text-2xl font-medium">
					Recipe
				</h1>
				<div class="mx-10">
					<ol class="list-decimal list-outside space-y-5 mt-2">
						<li v-for="(step, i) of recipe" :key="i" class="relative h-20 w-full">
							<textarea class="text-black w-full h-20 border rounded px-2 py-1 resize-none" v-model="recipe[i].text"
									  :class="{'border-red-400': submitted && (!step['text'] || step['text'].length === 0)}"></textarea>
							<img alt="delete" class="h-14 -right-16 top-3 absolute hover:cursor-pointer"
								 @click="recipe.splice(i, 1)"
								 src="@/assets/delete.png">
						</li>
					</ol>
					<div class="w-full flex justify-end mt-2">
						<button class="w-32 button" @click="recipe.push({})">Add step</button>
					</div>
				</div>

			</div>

			<div class="px-10">
				<button class="w-full h-16 mt-10 button" @click="createRecipe">
					SUBMIT
				</button>
			</div>

		</div>
	</div>
</template>

<script>
import UploadImageIcon from "@/components/icons/UploadImageIcon.vue";
import config from "@/config";

export default {
	name: "Create",
	data() {
		return {
			title: "",
			description: "",
			ingredients: [{}],
			recipe: [{}],
			image: null,
			submitted: false
		}
	},
	components: {
		UploadImageIcon
	},
	methods: {
		uploadImage(e){
			const image = e.target.files[0];
			const reader = new FileReader();
			reader.readAsDataURL(image);
			reader.onload = e =>{
				this.image = e.target.result;
			};
		},
		createRecipe(){
			this.submitted = true;
			fetch(`${config.API_URL}/recipe`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				credentials: 'include',
				body: JSON.stringify({
					title: this.title,
					description: this.description,
					ingredients: this.ingredients,
					steps: this.recipe,
					image: this.image
				})
			})
				.then(res => res.json())
				.then(data => {
					if (data['_id'])
						window.location.href = `/recipe/${data['_id']}`;
				}).catch(err => console.log(err));
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