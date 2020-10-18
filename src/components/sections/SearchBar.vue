<template>
  <div id="search">
    <input
        type="text"
        v-model="query"
        @keydown.enter="search"
        placeholder="픽토그램 검색하기"
    >
    <img v-if="query" class="btn" @click="reset" :src="xMarkPath" />
  </div >
</template>

<script>
export default {
  props: {
    onChange: () => {}
  },
  data: function () { 
    return {
      query: "",
      xMarkPath: require("@/assets/x-mark.png")
    }
  },
  methods: {
    reset(){
      this.query = "";
      this.search()
    },
    search(){
      this.onChange(this.query)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  position: relative;
  margin: 0 10px;
}

div input{
  width: calc(100% - 22px);
  padding: 8px 10px;
  margin: 0;
  border: 1px solid black;
}

div img {
  position: absolute;
  display: block;
  top: 0px;
  right: 0px;
  width: 15px;
  height: 15px;
  border: 0px;
  margin: 9px;
  cursor: pointer;
}
</style>
