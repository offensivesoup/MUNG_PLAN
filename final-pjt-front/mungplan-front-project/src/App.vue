<template>
  <header>
    <nav>
      <!-- <RouterLink :to="{name: HomeView}">로고 넣을 건디</RouterLink> -->
      <RouterLink :to="{ name: 'AdoptView' }">Life</RouterLink> |
      <RouterLink :to="{name: 'ArticleView'}">Community</RouterLink> |
      <!-- <RouterLink :to="{name: }">Market</RouterLink>-->
      <RouterLink :to="{name: 'DepositView'}">Finance</RouterLink>
    </nav>
  </header>
  <RouterView />
 </template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped></style>
