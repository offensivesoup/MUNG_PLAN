<template>
  <div class="adopt-list">
    <AdoptListItem
      v-for="dog in displayedPosts"
      :key="dog.id"
      :dog="dog"
    />
  </div>
  <div>
    <button v-if="currentPage > 1" @click="currentPage--">이전페이지</button>
    <span>{{ currentPage }} / {{ totalPages }}</span>
    <button v-if="currentPage < totalPages" @click="currentPage++">다음페이지</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAdoptStore } from '@/stores/adopt'
import AdoptListItem from './AdoptListItem.vue'

const store = useAdoptStore()

const currentPage = ref(1)
const postsPerPage = 10

const displayedPosts = computed(() => {
  const startIndex = (currentPage.value - 1) * postsPerPage
  const endIndex = startIndex + postsPerPage
  return store.shelterDog.slice(startIndex, endIndex)
})

const totalPages = computed(() => {
  return Math.ceil(store.shelterDog.length / postsPerPage)
})
</script>

<style scoped>
/* 카드형식의 컨테이너 스타일 정의 */
</style>