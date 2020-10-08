<template>
  <div class="textIcon">
    <div class="text">
      <p> {{ text }} </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TextIcon',
  props: {
      text: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.textIcon{
  color: black;
  width: 100px;
  height: 120px;
  padding: 10px;
}
.text {
  width: 100px;
  height: 100px;
  background-color: black;
  border-radius: 8px;  
  display: flex;
  justify-content: center;
  align-items: center;
}
p {
  font-size: 14px;
  color: white;
  word-break: keep-all;
  flex: 0 0 80px;
}
</style>
