<template>
  <div>
    <div v-if="icon && path">
      <div class="section">
        <div>
          <p> {{category.name}} - {{ icon.name }} </p>
          <img class="dark" :alt="icon.name" :src="path.jpg">
          <img :alt="icon.name" :src="path.jpg">
        </div>
        <div class="download">
          <button class="btn" @click="downloadWithVueResource(path.jpg, category.name+'-'+icon.name+'.jpg')">
            JPG 다운로드
          </button>
          <button class="btn" @click="downloadWithVueResource(path.png, category.name+'-'+icon.name+'.png')">
            PNG 다운로드
          </button>
       </div>
      </div>
    </div>
  </div>
</template>

<script>
import iconIndex from "@/iconIndex.json";

export default {
  name: 'PictogramPage',
  data: function () {
    const category = iconIndex
      .filter(category => category.id === this.$route.params.categoryId)[0];

    const icon = category && category.icons.filter(icon => icon.id === this.$route.params.iconId)[0];
    
    return {
      category,
      icon,
      path: icon && {
        jpg: require("@/assets/res/jpg/"+ icon.path + ".jpg"),
        png: require("@/assets/res/png/"+ icon.path + ".png")
      },
      clip: require("@/assets/res/jpg/26. 웹 · 모바일/03. 첨부파일.jpg"),
    }
  },
  methods: {
    forceFileDownload(response, fileName){
      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', fileName)
      document.body.appendChild(link)
      link.click()
    },
    downloadWithVueResource(path, fileName) {
      this.$http({
        method: 'get',
        url: path,
        responseType: 'arraybuffer'
      })
      .then(response => {
        this.forceFileDownload(response, fileName)  
      })
      .catch(() => console.log('error occured'))
      
    },
  }
}
</script>

<style scoped>
.btn {
  background-color: black;
  color: white;
  font-size: 11px;
  width: 100px;
  margin: 10px;
  border-radius: 8px;
  border-color: black;
}

img {
  width: 100px;
  height: 100px;
  border-radius: 20px;
  padding: 10px;
}

.dark {
  filter: invert(1);  
}

p {
  margin-top: 2px;
  font-size: 14px;
  font-weight: bold;
  word-break: keep-all;
}

</style>
