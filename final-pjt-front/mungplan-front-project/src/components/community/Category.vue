<!-- 
  what : life의 nav component
  use : 게시물 보여주는 모든 view에 추가 
-->

<template>
  <nav>
    <RouterLink :to="{ name: 'ArticleView' }">
      전체
    </RouterLink>
    <RouterLink :to="{ name: 'ArticleShareView' }">
      고민나누기
    </RouterLink>
    <RouterLink :to="{ name: 'ArticleUsedView' }">
      중고장터
    </RouterLink>
    <RouterLink :to="{ name: 'ArticleTownView' }">
      동네사람들
    </RouterLink>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>

</style>