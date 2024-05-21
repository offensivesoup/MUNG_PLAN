<!-- 이거 왜 뒤로가기 안 됨? -->

<template>
  <div class="deposit recommendDeposit-header">
    <h1>멍플랜 추천 예적금</h1>
    <!-- <h3>userName과 비슷한 사용자들이 선호한 상품을 기반으로 추천드려요</h3> -->
    <h4>멍플팬만의 스페셜 알고리즘이 추천하는 userName에게 딱 맞는 상품 Top 10 </h4>
  </div>

    <main class="main-content">
      <div id="carouselExampleCaptions" class="carousel slide">
        <div class="carousel-indicators">
          <button type="button" v-for="(deposit, index) in recommendDeposits" :key="index" 
                  data-bs-target="#carouselExampleCaptions" :data-bs-slide-to="index" 
                  :class="{ 'active': index === 0 }" aria-label="Slide {{ index + 1 }}"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item" v-for="(deposit, index) in recommendDeposits" :key="index" 
              :class="{ 'active': index === 0 }">
            <img class="company-image" :src="`${store.API_URL}${store.staticUrl}${deposit.company_image}`">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{ deposit.company_name }}</h5>
              <p>{{ deposit.product_explain }}</p>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </main>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import { useAccountStore } from '@/stores/account';
// import { useRoute } from 'vue-router'

const store = useDepositStore()
const userStore = useAccountStore()
// const route = useRoute()
const recommendDeposits = ref(null)

onMounted(() => {
  console.log(userStore.state.id)
  axios({
    method: 'get',
    // user_id 값 고쳐라
    url: `${store.API_URL}finance/deposits/recommend/${userStore.state.id}`
  })
    .then((response) => {
      recommendDeposits.value = response.data
      console.log(recommendDeposits.value)
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

.main-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>