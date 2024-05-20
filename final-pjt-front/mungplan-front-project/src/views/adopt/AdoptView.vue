<!--
  what : 입양 정보 제공 view
  use : life nav 누르면 바로 여기로 오도록 (life의 메인 주제니까?)
 -->

<template>
  <div class="adopt adopt-header">
    <h1>유기견 입양</h1>
  </div>
  <div class="adopt adopt-main">
    <!-- + : 필터 - 나이, 성별, 중성화, 지역, 품종? 너무 많은가 -->
  </div>
  <div class="adopt adopt-count-info">
    <img src="/adopt/brownDog1.png" alt="brown dog icon" style="width: 40px; height: 40px;">
    <h5 style="margin: 0; font-size: 18px;">{{ store.shelterDogs.length }}마리의 아이들이 가족을 기다리고 있어요.</h5>
  </div>
  <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
    <button @click="store.getArticles()" type="button" class="btn btn-secondary">전체</button>
    <button @click="store.articleFiltering('고민나누기')" type="button" class="btn btn-secondary">고민나누기</button>
    <button @click="store.articleFiltering('중고장터')" type="button" class="btn btn-secondary">중고장터</button>
    <button @click="store.articleFiltering('동네사람들')" type="button" class="btn btn-secondary">동네사람들</button>
  </div>
  <AdoptList />
</template>

<script setup>
import { onMounted } from 'vue'
import { useAdoptStore } from '@/stores/adopt'
import AdoptList from '@/components/adopt/AdoptList.vue'

const store = useAdoptStore()

onMounted(() => {
  store.getShelterDogs()
})
</script>

<style scoped>
.adopt-count-info {
  display: flex;
  /* justify-content: flex-start !important; */
  /* 카드 시작점이랑 수직정렬하기 */
  align-items: center;
  margin: 20px 0;
}

.adopt {
  display: flex;
  justify-content: center;
  align-items: center;
}

.btn-group {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 80px 0px;
  gap: 150px;
}

.btn-group>button {
  background-color: white;
  border: none;
  color: black;
  text-align: center;
}
</style>