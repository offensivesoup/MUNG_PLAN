<!-- 이거 왜 뒤로가기 안 됨? -->

<template>
  <div class="deposit recommendDeposit-header">
    <h1>멍플랜 추천 예적금</h1>
    <!-- <h3>userName과 비슷한 사용자들이 선호한 상품을 기반으로 추천드려요</h3> -->
    <h4>멍플팬만의 스페셜 알고리즘이 추천하는 userName에게 딱 맞는 상품 Top 10 </h4>
  </div>
  <RecommendDepositList 
    :recommendDeposits="recommendDeposits"
  />

</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useDepositStore } from '@/stores/deposit'
// import { useRoute } from 'vue-router'

const store = useDepositStore()
// const route = useRoute()
const recommendDeposits = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    // user_id 값 고쳐라
    url: `${store.API_URL}finance/deposits/recommend/${userStore.state.user.id}`
  })
    .then((response) => {
      recommendDeposits.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>

<style scoped>
.deposit {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>