<template>
  <div class="category">
    <img alt="ROKAF pictogram" src="../assets/header.jpg" />
    <div class="icons">
      <Icon v-for="icon in categories" :key="icon.id" :icon="icon" />
    </div>
  </div>
</template>

<script>
import Icon from './Icon.vue'

import iconIndex from "../iconIndex.json";

export default {
  name: 'MainList',
  components: {
    Icon
  },
  props: {
  },
  data: function () {
    const categories = iconIndex
      .map(category => ({id: category.id, name: category.name, path:  category.iconPath }));
    
    return {
      categories
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
  width: 720px;
  margin: 0 40px;
}

img{
  width: 800px;
  margin-bottom: 40px;
}
</style>
