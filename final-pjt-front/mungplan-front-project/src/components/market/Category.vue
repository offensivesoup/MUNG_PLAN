<!-- 
  what : life의 nav component
  use : 게시물 보여주는 모든 view에 추가 
-->
<!-- markets/product/<str:category_name>/ -->
  <!-- serach_words = ['영양제', '계단', '장난감', '매트', '수제간식', '샴푸', '배변패드', '크리너', '노즈워크', '침대/해먹'] -->
<template>
  <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
    <button @click="store.getProducts()" type="button" class="btn btn-secondary">전체</button>
    <button @click="store.productFiltering('영양제')" type="button" class="btn btn-secondary">영양제</button>
    <button @click="store.productFiltering('계단')" type="button" class="btn btn-secondary">계단</button>
    <button @click="store.productFiltering('장난감')" type="button" class="btn btn-secondary">장난감</button>
    <button @click="store.productFiltering('매트')" type="button" class="btn btn-secondary">매트</button>
    <button @click="store.productFiltering('수제간식')" type="button" class="btn btn-secondary">수제간식</button>
    <button @click="store.productFiltering('샴푸')" type="button" class="btn btn-secondary">샴푸</button>
    <button @click="store.productFiltering('배변패드')" type="button" class="btn btn-secondary">배변패드</button>
    <button @click="store.productFiltering('노즈워크')" type="button" class="btn btn-secondary">노즈워크</button>
    <button @click="store.productFiltering('침대/해먹')" type="button" class="btn btn-secondary">침대/해먹</button>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useMarketStore } from '@/stores/market';
const store = useMarketStore()
</script>

<style scoped>
.btn-group {
  display: flex;
  gap: 80px;
}

.btn-group>.btn {
  position: relative;
  border: none;
  background-color: transparent;
  color: black;
  text-transform: uppercase;
  height: 50px;
  margin: 50px 0px;
  font-size: 25px;
  opacity: 1;
  transition: all 0.5s ease-in-out;
  overflow: hidden;
}

.btn-group>.btn:focus {
  outline: none;
}

.btn-group>.btn::before {
  content: "";
  height: 100%;
  width: 100%;
  position: absolute;
  background-color: #FFBF9B;
  /* color:white; */
  top: 100%;
  left: 0;
  transition: all 0.4s;
  z-index: -1;
}

.btn-group>.btn:hover::before {
  transform: translateY(-100%);
}

.btn-group>.btn:hover {
  color: #B46060;
}
</style>