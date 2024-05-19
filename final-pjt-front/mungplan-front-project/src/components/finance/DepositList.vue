<template>
  <div class="deposit deposit-list row">
    <DepositListItem
      v-for="deposit in displayedPosts"
      :key="deposit.id"
      :deposit="deposit"
      class="col-4"
    />
  </div>
  <div class="deposit deposit-page">
    <button @click="prevPage">이전 페이지</button>
    <span>{{ currentPage }} / {{ totalPages }}</span>
    <button @click="nextPage">다음 페이지</button>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import DepositListItem from './DepositListItem.vue'
import { useRoute, useRouter } from 'vue-router'

const store = useDepositStore()
const route = useRoute()
const router = useRouter()

// 페이지네이션
const currentPage = ref(parseInt(route.query.page) || 1)
const postsPerPage = 15 // 한 페이지에 보여줄 개수

watch(route, () => {
  currentPage.value = parseInt(route.query.page) || 1
})

const totalPages = computed(() => {
  return Math.ceil(store.deposits.length / postsPerPage)
})

const displayedPosts = computed(() => {
  const startIndex = (currentPage.value - 1) * postsPerPage
  const endIndex = startIndex + postsPerPage
  return store.deposits.slice(startIndex, endIndex)
})

const nextPage = () => {
  router.push({ query: { ...route.query, page: currentPage.value + 1 } })
}

const prevPage = () => {
  router.push({ query: { ...route.query, page: currentPage.value - 1 } })
}
</script>

<style scoped>
/* 카드형식의 컨테이너 스타일 정의 */
.deposit {
  padding: 0 15%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>