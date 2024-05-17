<template>
  <div class="deposit-list">
    <DepositListItem
      v-for="deposit in store.deposits"
      :key="deposit.id"
      :deposit="deposit"
    />
  </div>
</template>

<script setup>
import { useDepositStore } from '@/stores/deposit'
import DepositListItem from './DepositListItem.vue'

const store = useDepositStore()
</script>

<style scoped>
/* 카드형식의 컨테이너 스타일 정의 */
</style>