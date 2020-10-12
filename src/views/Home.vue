<template>
  <div class="home">
    <SearchBar 
      v-model="query"
      @keydown.enter="search"
    />
    <MainList :query="query"/>
    <Category v-for="id in categoryIds" :id="id" :key="id" :query="query"/>
  </div>
</template>

<script>
import Category from '@/components/sections/Category'
import MainList from '@/components/sections/MainList'
import SearchBar from '@/components/sections/SearchBar'

import iconIndex from "@/iconIndex.json";

export default {
  name: 'Home',
  components: {
    Category,
    MainList,
    SearchBar
  },
  data: function () {
    const categoryIds = iconIndex
      .map(category => category.id);

    return {
      query: '',
      categoryIds
    }
  },
	methods: {
		search () {
      this.query = this.query.trim();
		}
	}
}
</script>
