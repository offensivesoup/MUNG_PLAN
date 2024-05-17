<!-- 
  what : life의 nav component
  use : 게시물 보여주는 모든 view에 추가 
-->

<template>
  <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
    <button @click="store.getArticles()" type="button" class="btn btn-secondary">전체</button>
    <button @click="store.articleFiltering('고민나누기')" type="button" class="btn btn-secondary">고민나누기</button>
    <button @click="store.articleFiltering('중고장터')" type="button" class="btn btn-secondary">중고장터</button>
    <button @click="store.articleFiltering('동네사람들')" type="button" class="btn btn-secondary">동네사람들</button>
  </div>
  <!-- <nav>
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
  </nav> -->
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useArticleStore } from '@/stores/article';
const store = useArticleStore()
</script>

<style scoped></style>