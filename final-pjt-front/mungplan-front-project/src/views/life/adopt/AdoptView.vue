<!--
  what : 입양 정보 제공 view
  use : life nav 누르면 바로 여기로 오도록 (life의 메인 주제니까?)
 -->

<template>
  <div class="adopt-header">
    <h1>유기견 입양</h1>
  </div>
  <div class="adopt-main">
    <!-- + : 필터 - 나이, 성별, 중성화, 지역, 품종? 너무 많은가 -->
  </div>
  <div class="adopt-count-info">
    <img src="/adopt/brownDog1.png" alt="brown dog icon" style="width: 40px; height: 40px;">
    <h5 style="margin: 0; font-size: 18px;">{{ store.shelterDogs.length }}명의 아이들이 가족을 기다리고 있어요.</h5>
</div>
  <AdoptList />
</template>

<script setup>
import { onMounted } from 'vue'
import { useAdoptStore } from '@/stores/adopt'
import AdoptList from '@/components/life/AdoptList.vue'

const store = useAdoptStore()

onMounted(() => {
  store.getShelterDogs()
})
</script>

<style scoped>
.adopt-count-info {
  display: flex;
  align-items: center;
  margin: 20px 0;
}
</style>