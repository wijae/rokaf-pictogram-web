<template>
  <div class="category">
    <h1>{{ categoryId }}. {{ categoryName }}</h1>
    <div class="icons">
      <div class="icon" v-for="icon in icons" :key="icon.id" >
        <img :alt="icon.id" :src="icon.path">
        <p> {{ icon.name }} </p>
      </div>
    </div>
  </div>
</template>

<script>
import iconIndex from "../iconIndex.json";

export default {
  name: 'Category',
  props: {
    id: String
  },
  data: function () {
    const category = iconIndex
      .filter(category => category.id === this.id)[0];

    const icons = category.icons
      .map(icon => ({id: icon.id, name: icon.name, path: require("../assets/res/jpg/"+ icon.path + ".jpg")}))
    
    return {
      icons: icons,
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
