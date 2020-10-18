<template>
  <div class="iconList" v-if="icons.length || showTextAlways">
    <template v-if="text" >
      <TextIcon v-if="text" :text="text" :to="to" />
    </template>
    <template v-if="icons.length" >
      <Icon v-for="icon in icons" :key="icon.id" :icon="icon" />
    </template>
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
    to: String,
    icons: [Object],
    showTextAlways: Boolean
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.iconList {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-content: space-around;
  padding: 20px 0;
}
</style>
