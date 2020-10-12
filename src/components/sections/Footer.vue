<template>
  <div id="footer">
    <a id="github" rel="noopener noreferrer nofollow" href="https://github.com/wijae/rokaf-pictogram-web">
      <img alt="github link" src="@/assets/github.png" />
      ROKAF-pictogram-web
    </a>
    <p>
      본 사이트는 대한민국 공군에서 배포하는 공군 픽토그램을 쉽고 간편하게 찾을 수 있도록 만들어졌습니다.<br/>
    </p>
    <p>
      공군 픽토그램의 저작권은 대한민국 공군에 있으며, 출처 표기 시 누구나 자유롭게 사용할 수 있습니다.<br/>
      픽토그램 원본 파일은 공군 공감블로그 (<a rel="noopener noreferrer nofollow" href="https://afplay.kr/2318">
        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-link-45deg" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path d="M4.715 6.542L3.343 7.914a3 3 0 1 0 4.243 4.243l1.828-1.829A3 3 0 0 0 8.586 5.5L8 6.086a1.001 1.001 0 0 0-.154.199 2 2 0 0 1 .861 3.337L6.88 11.45a2 2 0 1 1-2.83-2.83l.793-.792a4.018 4.018 0 0 1-.128-1.287z"/>
          <path d="M6.586 4.672A3 3 0 0 0 7.414 9.5l.775-.776a2 2 0 0 1-.896-3.346L9.12 3.55a2 2 0 0 1 2.83 2.83l-.793.792c.112.42.155.855.128 1.287l1.372-1.372a3 3 0 0 0-4.243-4.243L6.586 4.672z"/>
        </svg>https://afplay.kr/2318</a>)에서 내려받을 수 있습니다
    </p>
  </div>
</template>

<script>

export default {
  name: 'Footer'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a{
  color: #D2D3D3;
  text-decoration: none;
}

#footer{
  font-size: 12px;
  padding: 40px;
  color: #D2D3D3;
  background-color: black;
}

#github{
  font-size: 24px;
}

#github img{
  width: 24px;
}
</style>
