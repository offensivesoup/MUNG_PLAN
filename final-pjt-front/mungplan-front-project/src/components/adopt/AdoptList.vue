<template>
  <div class="adopt adopt-list card-group row">
    <AdoptListItem v-for="dog in displayedPosts" :key="dog.id" :dog="dog" class="col-lg-4 col-md-6" />
  </div>
  <div class="adopt adopt-page">
    <button @click="prevPage">이전 페이지</button>
    <span>{{ currentPage }} / {{ totalPages }}</span>
    <button @click="nextPage">다음 페이지</button>
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
</style>