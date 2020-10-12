<template>
  <div id="app">
    <div id="wrapper">
      <Header />
      <div id="content">
        <SearchBar 
          v-model="query"
          @keydown.enter="search"
        />
        <MainList :query="query"/>
        <Category v-for="id in categoryIds" :id="id" :key="id" :query="query"/>
      </div>
      <Footer />
    </div>
  </div>
</template>

<script>
import Category from './components/sections/Category'
import MainList from './components/sections/MainList'
import SearchBar from './components/sections/SearchBar'
import Header from './components/sections/Header'
import Footer from './components/sections/Footer'

import iconIndex from "./iconIndex.json";

export default {
  name: 'App',
  components: {
    Category,
    MainList,
    SearchBar,
    Header,
    Footer
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

#wrapper {
  width: calc(960px + 80px);
  margin:0 auto;
  background-color: #D2D3D3;
}

#content {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  padding: 0 40px 40px;
}

@media screen and (max-width: 1200px) {
  #wrapper {
    width: calc(720px + 80px);
  }
};

@media screen and (max-width: 960px) {
  #wrapper {
    width: calc(480px + 80px);
  }
};

@media screen and (max-width: 600px) {
  #wrapper {
    width: calc(240px + 40px);
  }
  #content {
    padding: 0 20px 20px;
  }
};

</style>
