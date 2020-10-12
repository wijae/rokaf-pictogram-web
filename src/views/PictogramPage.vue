<template>
  <div v-if="icon">
    <Icon :key="icon.id" :icon="icon" />
  </div>
</template>

<script>
import Icon from '@/components/common/Icon.vue'

import iconIndex from "@/iconIndex.json";

export default {
  name: 'PictogramPage',
  components: {
    Icon
  },
  data: function () {
    const category = iconIndex
      .filter(category => category.id === this.$route.params.categoryId)[0];

    const icon = category && category.icons.filter(icon => icon.id === this.$route.params.iconId)[0];

    return {
      category,
      icon
    }
  },
}
</script>
