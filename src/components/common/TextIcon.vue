<template>
  <div class="textIcon">
    <template v-if="to">
      <router-link :to="to">
        <div class="text">
          <p> {{ text }} </p>
        </div>
      </router-link>
    </template>    
    <template v-else>
      <div class="text">
        <p> {{ text }} </p>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  name: 'TextIcon',
  props: {
      text: String,
      to: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.textIcon{
  color: black;
  width: 100px;
  height: 120px;
  padding: 20px 10px;
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
  font-weight: bold;
  color: white;
  word-break: keep-all;
  flex: 0 0 80px;
}

a {
  text-decoration: none;
}
</style>
