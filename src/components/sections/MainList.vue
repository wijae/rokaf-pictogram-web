<template>
  <IconList :icons="filterdIcons"/>
</template>

<script>
import IconList from '@/components/common/IconList.vue'

import iconIndex from "@/iconIndex.json";

export default {
  name: 'MainList',
  components: {
    IconList
  },
  props:{
    query: String
  },
  data: function () {
    const icons = iconIndex
      .map(category => ({
        id: category.id, name: category.name, path: category.iconPath, to: `/category/${category.id}`
      }))

    return {
      icons
    }
  },
  computed: {
    filterdIcons: function () {
      return this.icons
        .filter(icon => !this.query || icon.name.includes(this.query));
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
