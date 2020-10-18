<template>
  <div>
    <SearchBar 
      v-model="query"
      @keydown.enter="search"
    />
    <MainList :query="query"/>
    <template v-if="query">
      <Category v-for="id in categoryIds" :id="id" :key="id" :query="query"/>
    </template>
  </div>
</template>

<script>
import Category from '@/components/sections/Category'
import MainList from '@/components/sections/MainList'
import SearchBar from '@/components/sections/SearchBar'

import iconIndex from "@/iconIndex.json";

export default {
  name: 'MainPage',
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
