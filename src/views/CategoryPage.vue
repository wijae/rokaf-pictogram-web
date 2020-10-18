<template>
  <div>
    <SearchBar :onChange="onChangeQuery"/>
    <Category :id="id" :key="id" :query="query" showCategoryAlways="true" />
  </div>
</template>

<script>
import Category from '@/components/sections/Category'
import SearchBar from '@/components/sections/SearchBar'

export default {
  name: 'CategoryPage',
  components: {
    Category,
    SearchBar
  },
  data: function () {
    return {
      query: '',
      id: this.$route.params.id
    }
  },
	methods: {
		onChangeQuery (query) {
      this.query = query;
		}
	}
}
</script>
