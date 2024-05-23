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
import { useRoute, useRouter } from 'vue-router'
import DepositListItem from './DepositListItem.vue'

const props = defineProps({
  filteredAndSortedDeposits: Array
})

const route = useRoute()
const router = useRouter()

const currentPage = ref(parseInt(route.query.page) || 1)
const postsPerPage = 15

watch(route, () => {
  currentPage.value = parseInt(route.query.page) || 1
})

const totalPages = computed(() => {
  return Math.ceil(props.filteredAndSortedDeposits.length / postsPerPage)
})

const displayedPosts = computed(() => {
  const startIndex = (currentPage.value - 1) * postsPerPage
  const endIndex = startIndex + postsPerPage
  return props.filteredAndSortedDeposits.slice(startIndex, endIndex)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    router.push({ query: { ...route.query, page: currentPage.value + 1 } })
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    router.push({ query: { ...route.query, page: currentPage.value - 1 } })
  }
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