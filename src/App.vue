<template>
  <div id="app">
    <MainList />
    <Category v-for="id in categoryIds" :id="id" :key="id"/>
  </div>
</template>

<script>
import Category from './components/Category.vue'
import MainList from './components/MainList.vue'

import iconIndex from "./iconIndex.json";

export default {
  name: 'App',
  components: {
    Category,
    MainList
  },
  data: function () {
    const categoryIds = iconIndex
      .map(category => category.id);

    return {
      categoryIds
    }
  }
}
</script>

<style>
#app {
  width: 800px;
  margin:0 auto;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background-color: #D2D3D3;
}
</style>
