<template>
  <div class="deposit-list-item">
    <img src="#" alt="deposit product img">
    <p>예.적금 상품 정보 출력</p>
    <p>{{ deposit.title }}</p>
    
    <RouterLink :to="{ name: 'DepositDetailView', params: { id: deposit.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
defindProps({
  deposit: Object
})
</script>

<style scoped>
/* 개별 카드의 스타일 정의 */
</style>