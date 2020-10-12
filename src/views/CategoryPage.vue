<template>
  <div class="cat">
    <Category :id="id" :key="id"/>
  </div>
</template>

<script>
import Category from '@/components/sections/Category'

export default {
  name: 'CategoryPage',
  components: {
    Category
  },
  data: function () {
    return {
      id: this.$route.params.id
    }
  },
}
</script>
