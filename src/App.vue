<template>
  <div id="app">
    <div id="wrapper">
      <router-link to="/">
        <Header />
      </router-link>
      <div id="content">
        <router-view/>
      </div>
      <Footer />
    </div>
  </div>
</template>

<script>
import Header from '@/components/sections/Header'
import Footer from '@/components/sections/Footer'

export default {
  name: 'App',
  components: {
    Header,
    Footer
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
  color: #2c3e50;
  padding: 0 40px 40px;
}

@media screen and (max-width: 1200px) {
  #wrapper {
    width: calc(720px + 80px);
  }
}

@media screen and (max-width: 960px) {
  #wrapper {
    width: calc(480px + 80px);
  }
}

@media screen and (max-width: 600px) {
  #wrapper {
    width: calc(240px + 40px);
  }
  #content {
    padding: 0 20px 20px;
  }
}

</style>
