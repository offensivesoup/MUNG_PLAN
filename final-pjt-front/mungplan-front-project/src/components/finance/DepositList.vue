<template>
  <div class="deposit deposit-list row">
    <DepositListItem v-for="deposit in displayedPosts" :key="deposit.id" :deposit="deposit" class="col-4" />
  </div>
  <div class="deposit deposit-page">
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