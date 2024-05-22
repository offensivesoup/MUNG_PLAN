<template>
  <div class="liked-deposit liked-deposit-header">
    <h1 style="text-align: center; font-size: 3rem; padding-top: 10px;">{{ route.query.nickname }}님이 고른 예적금 상품</h1>
  </div>
  <LikedDepositList :id="Number(route.query.id)"/>
</template>
  
<script setup>
import { onMounted, ref } from 'vue'
import { useAccountStore } from '@/stores/account'
import LikedDepositList from '@/components/accounts/LikedDepositList.vue'
import { useRoute } from 'vue-router'

const store = useAccountStore()
const route = useRoute()
</script>

<style scoped>
</style>
