<template>
  <IconList :text="name" :to="to" :icons="filterdIcons" :showTextAlways="showCategoryAlways"/>
</template>

<script>
import IconList from '@/components/common/IconList.vue'

import iconIndex from "@/iconIndex.json";

export default {
  name: 'Category',
  components: {
    IconList
  },
  props: {
    id: String,
    query: String,
    showCategoryAlways: Boolean
  },
  data: function () {
    const category = iconIndex
      .filter(category => category.id === this.id)[0];

    console.log(this.showCategoryAlways)
    
    return {
      name: category.name,
      to: `/category/${category.id}`,
      icons: category.icons.map(icon => ({...icon, to: `/category/${category.id}/pictogram/${icon.id}`}))
    }
  },
  computed: {
    filterdIcons: function () {
      return this.icons
        .filter(icon => !this.query || this.name.includes(this.query) || icon.name.includes(this.query));
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
