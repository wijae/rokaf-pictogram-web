<template>
  <div id="search">
    <input
        type="text"
        class="input"
        v-on="listeners"
        placeholder="픽토그램 검색하기"
    >
  </div>
</template>

<script>
export default {
  computed: {
    listeners () {
      return {
        // Pass all component listeners directly to input
        ...this.$listeners,
        // Override input listener to work with v-model
        input: event => this.$emit('input', event.target.value)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.input {
  width: calc(100% - 42px);
  padding: 8px 10px;
  margin: 0 10px;
  border: 1px solid black;
}
</style>
