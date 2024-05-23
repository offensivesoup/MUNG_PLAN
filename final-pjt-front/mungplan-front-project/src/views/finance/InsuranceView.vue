<template>
    <h1>펫보험</h1>
    <div class="content">
        <Carousel>
            <Slide v-for="(insurance, index) in store.insurances" :key="index">
                <div class="carousel__item">
                    <div class="short">
                        <div class="info-item">
                            <p class="label">입통원비</p>
                            <p class="value">{{ insurance.admission }}</p>
                        </div>
                        <div class="info-item">
                            <p class="label">예상 보험료</p>
                            <p class="value">{{ insurance.average_pay }}</p>
                        </div>
                        <div class="info-item">
                            <p class="label">상품명</p>
                            <p class="value">{{ insurance.product_name }}</p>
                        </div>
                        <div class="info-item">
                            <p class="label">수술비</p>
                            <p class="value">{{ insurance.liability }}</p>
                        </div>
                        <div class="info-item">
                            <p class="label">가입 조건</p>
                            <p class="value">{{ insurance.join_age }}</p>
                        </div>
                    </div>
                    <div class="long">
                        <div class="info-item">
                            <p class="label">상품 설명</p>
                            <p class="value" v-html="insurance.product_explain"></p>
                        </div>
                        <div class="info-item">
                            <p class="label"></p>
                            <!-- <p class="value" v-html="deposit.special_explain"></p> -->
                        </div>
                    </div>
                </div>
                <div class="carousel_image">
                    <img :src="`${store.API_URL}${store.staticUrl}${insurance.company_image}`" alt="" class="company_image">
                    <div class="info-item">
                        <a :href="insurance.link" target="_blank"><button type="button" class="btn">지금 보기</button></a>
                    </div>
                </div>
            </Slide>
            <template #addons>
                <Pagination />
            </template>
        </Carousel>
        </div>
</template>

<script setup>
import { useDepositStore } from '@/stores/deposit';
import { onMounted } from 'vue'
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'
const store = useDepositStore()

onMounted(() => {
    store.getInsurance()
})


</script>

<style scoped>

.carousel__item {
display: flex;
flex-direction: column;
justify-content: space-between;
align-items: flex-start;
width: 1400px;
}

.carousel_image {
/* margin-top: -250px; */
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
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
margin-left: 20px;
font-size: 15px;
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

.info-item {
  /* display: flex;
  flex-direction: column;
  justify-content: flex-start;
  margin-bottom: 10px; */
  text-align: left;
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

.company_image {
    border: black 2px solid;
    border-radius: 20%;
}
</style>