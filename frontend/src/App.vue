<template>
  <header class="p-3 bg-[#ccdbfd] flex space-x-2 items-center">
    <router-link to="/">
      <img alt="logo" src="@/assets/logo.png" class="w-[50px]" />
    </router-link>
    <input v-model="search" @input="$router.push('/')"
           class="h-10 rounded-lg p-2 border-2 border-[#F3FCF0] bg-transparent text-white focus:text-black w-56 focus:w-96 focus:bg-white" placeholder="Search...">
    <router-link to="/" class="button border-[2px] border-[#F3FCF0]">Explore</router-link>
    <router-link to="/fridge" class="button  border-[2px] border-[#F3FCF0]">Fridge</router-link>
<!--    <button class="button  border-[2px] border-[#F3FCF0]">Random generator</button>-->
    <router-link to="/create" class="button  border-[2px] border-[#F3FCF0]">New recipe</router-link>
  </header>

  <main class="p-10">
    <router-view :search="search"></router-view>
  </main>
</template>


<script>
import RecipeCard from "@/components/RecipeCard.vue";

export default {
  name: "App",
  components: {
    RecipeCard
  },
  data() {
    return {
      search: ""
    }
  }
}
</script>

<style scoped>
input::placeholder {
  color: white;
  opacity: 1;
}

input:focus::placeholder {
  color: gray;
  opacity: 1;
}

</style>
