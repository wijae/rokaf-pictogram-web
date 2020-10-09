<template>
  <div class="icons" v-if="icons.length">
    <template v-if="text">
      <TextIcon :text="text" />
    </template>
    <Icon v-for="icon in icons" :key="icon.id" :icon="icon" />
  </div>
</template>

<script>
import Icon from './Icon.vue'
import TextIcon from './TextIcon.vue'

export default {
  name: 'IconList',
  components: {
    Icon,
    TextIcon
  },
  props: {
    text: String,
    icons: [Object],
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
  padding: 40px 0;
}
</style>
