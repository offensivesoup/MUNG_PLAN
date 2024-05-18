<template>
  <header>
    <nav>
      <!-- <RouterLink :to="{name: HomeView}">로고 넣을 건디</RouterLink> -->
      <RouterLink :to="{ name: 'AdoptView' }">입양</RouterLink> |
      <RouterLink :to="{ name: 'ArticleView' }">커뮤니티</RouterLink> |
      <!-- <RouterLink :to="{name: }">Market</RouterLink>-->
      <RouterLink :to="{ name: 'DepositView' }">금융</RouterLink> |
      <RouterLink :to="{ name: 'MapView' }">강아지도</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped></style>
