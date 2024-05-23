<template>
  <div class="adopt adopt-list card-group row">
    <AdoptListItem v-for="dog in displayedPosts" :key="dog.id" :dog="dog" class="col-lg-4 col-md-6" />
  </div>
  <div class="adopt adopt-page">
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
import { useAdoptStore } from '@/stores/adopt'
import AdoptListItem from './AdoptListItem.vue'
import { useRoute, useRouter } from 'vue-router'

const store = useAdoptStore()
const route = useRoute()
const router = useRouter()

// 페이지네이션
const currentPage = ref(parseInt(route.query.page) || 1)
const postsPerPage = 15 // 한 페이지에 보여줄 개수

watch(route, () => {
  currentPage.value = parseInt(route.query.page) || 1
})

const totalPages = computed(() => {
  return Math.ceil(store.shelterDogs.length / postsPerPage)
})

const displayedPosts = computed(() => {
  const startIndex = (currentPage.value - 1) * postsPerPage
  const endIndex = startIndex + postsPerPage
  return store.shelterDogs.slice(startIndex, endIndex)
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
.adopt {
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

.page-button>img {
  width: 60px;
  transition: width 1s ease-in;
}

.article-btn>span {
  font-size: 20px;
  margin: 40px;
}
</style>