<template>
  <Category />
  <h4 class="title">{{ store.products.length }} 개의 상품이 있습니다</h4>
  <!-- <input v-model="s" class="p-1.5 w-128" placeholder="Search"> -->
  <div class="market market-list row">
    <MarketListItem v-for="product in displayedPosts" :key="product.id" :product="product" class="col-4" />
  </div>
  <div class="market market-page">
    <div class="article-btn">
      <button @click="prevPage" class="page-button">
        <img src="@/assets/left-arrow.png" alt=""> </button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" class="page-button">
        <img src="@/assets/right-arrow.png" alt=""> </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useMarketStore } from '@/stores/market'
import { useRoute, useRouter } from 'vue-router'
import Category from '@/components/market/Category.vue'
import MarketListItem from '@/components/market/MarketListItem.vue'

const store = useMarketStore()
const route = useRoute()
const router = useRouter()
// const searchText = ref(null)
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
.title {
  text-align: center;
  margin: 60px 0px;
}

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


.page-button {
  background-color: transparent;
  border: none;
  margin: 30px;
  font-size: 20px;
  transition: color 0.3s ease;
  /* 색 변화에 대한 transition 효과를 추가합니다. */
}

.page-button>img {
  width: 60px;
  transition: width 1s ease-in;
}

.article-btn>span {
  font-size: 20px;
  margin: 40px;
}
</style>