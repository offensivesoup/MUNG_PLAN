<template>
  <article class="loading-layout">
    <div class="loading" v-if="isLoading">
      <h2>멍플랜이 {{ userStore.state.nickname }}님의 상품을 찾고 있습니다.</h2>
      <div class="spinner-grow" role="status">
      </div>
    </div>
  </article>

  <main v-if="!isLoading" class="main-content">
    <div class="deposit recommendDeposit-header">

      <h2>멍플랜 추천 예적금</h2>
      <h4>멍플팬만의 스페셜 알고리즘이 추천하는 {{ userStore.state.nickname }}님 에게 딱 맞는 상품 Top 10 </h4>

    </div>
    <div class="content">
      <Carousel>
        <Slide v-for="(deposit, index) in recommendDeposits" :key="index">
          <div class="carousel__item">
            <div class="info-title">
              <p class="title">TOP {{ index + 1 }}</p>
            </div>
            <div class="short">
              <div class="info-item">
                <p class="label">구분</p>
                <p class="value">{{ deposit.category }}</p>
              </div>
              <div class="info-item">
                <p class="label">회사명</p>
                <p class="value">{{ deposit.company_name }}</p>
              </div>
              <div class="info-item">
                <p class="label">상품명</p>
                <p class="value">{{ deposit.product_name }}</p>
              </div>
              <div class="info-item">
                <p class="label">방식</p>
                <p class="value">{{ deposit.interate_type }}</p>
              </div>
              <div class="info-item">
                <p class="label">가입 조건</p>
                <p class="value">{{ deposit.join_member }}</p>
              </div>
            </div>
            <div class="long">
              <div class="info-item">
                <p class="label">상품설명</p>
                <p class="value" v-html="deposit.product_explain"></p>
              </div>
              <div class="info-item">
                <p class="label">특별 조건</p>
                <p class="value" v-html="deposit.special_explain"></p>
              </div>
            </div>
          </div>
          <div class="carousel_image">
            <img :src="`${store.API_URL}${store.staticUrl}${deposit.img}`" alt="">
            <div class="info-item">
              <a :href="deposit.link" target="_blank"><button type="button" class="btn">은행 보기</button></a>
            </div>
          </div>
        </Slide>
        <template #addons>
          <Pagination />
        </template>
      </Carousel>
    </div>
  </main>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import { useAccountStore } from '@/stores/account';
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'
// import { useRoute } from 'vue-router'

const store = useDepositStore()
const userStore = useAccountStore()
// const route = useRoute()
const recommendDeposits = ref(null)
const isLoading = ref(true)
const formatText = function (text) {
  return text.replace(/(.{30})/g, '$1<br>');
}
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
      isLoading.value = false
    })
    .catch((error) => {
      console.log(error)
    })
})

</script>

<style scoped>
.recommendDeposit-header {
  display: flex;
  flex-direction: column;
  gap: 40px;
  ;
}

.recommendDeposit-header>h2 {
  font-size: 80px;
  font-weight: bolder;
}

.recommendDeposit-header>h4 {
  font-size: 30px;
  font-weight: bold;
}

.deposit {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.short {
  display: grid;
  grid-template-columns: repeat(2, 2fr);
  column-gap: 100px;
  row-gap: 30px;
}

.short>.info-item {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  gap: 50px;
}

.main-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 70px;
}

.content {
  width: 1500px;
  padding: 100px;
  transition: all 2s ease;
}

.content:hover {
  border-radius: 15%;
  background-color: rgb(255, 191, 155, 0.3);
}

.loading {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 90vh;
  /* Viewport height */
  width: 75vw;
  /* Viewport width */
}

.loading>h2 {
  font-size: 50px;
}

.loading-layout {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 50px;
}

.info-item {
  /* display: flex;
  flex-direction: column;
  justify-content: flex-start;
  margin-bottom: 10px; */
  text-align: left;
}

.carousel__item {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  width: 1400px;
}

.carousel_image {
  margin-top: -250px;
  margin-right: 50px;
}

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}

.label {
  font-size: 25px;
  display: inline-block;
  text-align: left;
}

.value {
  display: inline-block;
  font-size: 20px;
}

.btn {
  background-color: transparent;
  color: #000000;
  font-size: 25px;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  width: 200px;
  transition: all 0.5s ease;
}

.btn:hover {
  font-size: 35px;
  color: #000000;
}

.title {
  font-size: 50px;
}
</style>