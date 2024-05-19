<template>
  <div class="deposit recommendDeposit-list row">
    <RecommendDepositListItem
      v-for="deposit in recommendDeposits"
      :key="deposit.id"
      :deposit="deposit"
      class="col-4"
    />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import RecommendDepositListItem from './RecommendDepositListItem.vue'
import { useRoute, useRouter } from 'vue-router'

// 호옥시나~ 안될까봐!
// const props = defineProps({
//   recommendDeposits: Object
// })

defineProps({
  recommendDeposits: Object
})
const store = useDepositStore()
// const route = useRoute()
// const router = useRouter()

// // 페이지네이션
// const currentPage = ref(parseInt(route.query.page) || 1)
// const postsPerPage = 15 // 한 페이지에 보여줄 개수

// watch(route, () => {
//   currentPage.value = parseInt(route.query.page) || 1
// })

// const totalPages = computed(() => {
//   return Math.ceil(props.recommendDeposits.length / postsPerPage)
// })

// const displayedPosts = computed(() => {
//   const startIndex = (currentPage.value - 1) * postsPerPage
//   const endIndex = startIndex + postsPerPage
//   return props.recommendDeposits.slice(startIndex, endIndex)
// })

// const nextPage = () => {
//   router.push({ query: { ...route.query, page: currentPage.value + 1 } })
// }

// const prevPage = () => {
//   router.push({ query: { ...route.query, page: currentPage.value - 1 } })
// }
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