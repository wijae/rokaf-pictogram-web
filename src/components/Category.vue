<template>
  <div class="category">
    <div class="icons">
      <TextIcon :text="categoryName" />
      <Icon v-for="icon in icons" :key="icon.id" :icon="icon" />
    </div>
  </div>
</template>

<script>
import Icon from './Icon.vue'
import TextIcon from './TextIcon.vue'

import iconIndex from "../iconIndex.json";

export default {
  name: 'Category',
  components: {
    Icon,
    TextIcon
  },
  props: {
    id: String
  },
  data: function () {
    const category = iconIndex
      .filter(category => category.id === this.id)[0];
    
    return {
      icons: category.icons,
      categoryId: category.id,
      categoryName: category.name
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.icons{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-content: space-around;
  padding: 40px 0;
}
</style>
