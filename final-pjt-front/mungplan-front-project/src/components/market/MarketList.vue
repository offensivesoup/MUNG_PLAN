<template>
  <div class="market market-list row">
    <MarketListItem v-for="product in displayedPosts" :key="product.id" :product="product" class="col-4" />
  </div>
  <div class="market market-page">
    <button @click="prevPage" class="page-button">
      << </button>
        <span>{{ currentPage }} / {{ totalPages }}</span>
        <button @click="nextPage" class="page-button">
          >> </button>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useMarketStore } from '@/stores/market'
import MarketListItem from './MarketListItem.vue'
import { useRoute, useRouter } from 'vue-router'

const store = useMarketStore()
const route = useRoute()
const router = useRouter()

// 페이지네이션
const currentPage = ref(parseInt(route.query.page) || 1)
const postsPerPage = 15 // 한 페이지에 보여줄 개수

watch(route, () => {
  currentPage.value = parseInt(route.query.page) || 1
})

const totalPages = computed(() => {
  return Math.ceil(store.products.length / postsPerPage)
})

const displayedPosts = computed(() => {
  const startIndex = (currentPage.value - 1) * postsPerPage
  const endIndex = startIndex + postsPerPage
  return store.products.slice(startIndex, endIndex)
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
.market {
  padding: 0 15%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.page-button {
  background-color: transparent;
  border: none;
  margin: 30px;
  font-size: 20px;
  transition: color 0.3s ease;
  /* 색 변화에 대한 transition 효과를 추가합니다. */
}

.page-button:hover {
  color: darkgray;
  /* 마우스를 올렸을 때의 색상을 지정합니다. */
}
</style>