<template>
  <div class="category">
    <h1>ROKAF pictogram</h1>
    <div class="icons">
      <div class="icon" v-for="category in categories" :key="category.id" >
        <img :alt="category.id" :src="category.path">
        <p> {{ category.id }}. {{ category.name }} </p>
      </div>
    </div>
  </div>
</template>

<script>
import iconIndex from "../iconIndex.json";

export default {
  name: 'MainList',
  props: {
  },
  data: function () {
    const categories = iconIndex
      .map(category => ({id: category.id, name: category.name, path: require("../assets/res/jpg/"+ category.iconPath + ".jpg")}));

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
}
.icon{
  width: 160px;
}
img {
  width: 96px;
  height: 96px;
  filter: invert(1);  
  border-radius: 8px;
}
p {
  word-break: keep-all
}
</style>
