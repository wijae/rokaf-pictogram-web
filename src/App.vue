<template>
  <div id="app">
    <div id="content">
      <img id="header" alt="ROKAF pictogram" src="./assets/header.jpg" />
      <SearchBar 
        v-model="query"
        @keydown.enter="search"
      />
      <MainList :query="query"/>
      <Category v-for="id in categoryIds" :id="id" :key="id" :query="query"/>
    </div>
  </div>
</template>

<script>
import Category from './components/sections/Category.vue'
import MainList from './components/sections/MainList.vue'
import SearchBar from './components/sections/SearchBar.vue'

import iconIndex from "./iconIndex.json";

export default {
  name: 'App',
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
      console.log("!");
		}
	}
}
</script>

<style>
#app {
  background-color: #e0e0e0;
}

#content {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  width: 960px;
  padding: 0 40px 40px;
  margin:0 auto;
  background-color: #D2D3D3;
}

#header{
  width: 1040px;

  margin: 0 -40px 40px;
  margin-bottom: 40px;
}

@media screen and (max-width: 1200px) {
  #content {
    width: 720px;
  }
  #header{
    width: 800px;
  }
};

@media screen and (max-width: 960px) {
  #content {
    width: 480px;
  }
  #header{
    width: 560px;
  }
};

@media screen and (max-width: 600px) {
  #content {
    width: 240px;
    padding: 0 20px 20px;
  }
  #header{
    width: 280px;
    margin: 0 -20px 20px;
  }
};

</style>
