<template>
  <div class="icon">
    <img :alt="icon.name" :src="path">
    <p> {{ icon.name }} </p>
  </div>
</template>

<script>
export default {
  name: 'Icon',
  props: {
      icon: {
          id: String,
          name: String,
          path: String
      }
  },
  data: function () {
    return {
      path: require("../../assets/res/jpg/"+ this.icon.path + ".jpg")
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.icon{
  width: 100px;
  height: 120px;
  padding: 20px 10px;
}
img {
  width: 100px;
  height: 100px;
  filter: invert(1);  
  border-radius: 8px;
}
p {
  margin-top: 2px;
  font-size: 14px;
  font-weight: bold;
  word-break: keep-all;
}
</style>
