<template>
  <IconList :text="name" :icons="filterdIcons"/>
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
    query: String
  },
  data: function () {
    const category = iconIndex
      .filter(category => category.id === this.id)[0];
    
    return {
      name: category.name,
      icons: category.icons
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
