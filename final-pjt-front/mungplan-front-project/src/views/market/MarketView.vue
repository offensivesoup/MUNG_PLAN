<template>
  <div class="market market-header">
    <h1>멍마켓</h1>
  </div>
  <div class="maket market-main">
    <!-- + : 필터 - 나이, 성별, 중성화, 지역, 품종? 너무 많은가 -->
  </div>
  <div class="market market-count-info">
    <!-- <img src="/market/brownDog1.png" alt="brown dog icon" style="width: 40px; height: 40px;"> -->
    <!-- <h5 style="margin: 0; font-size: 18px;">{{ store.shelterDogs.length }}명의 아이들이 가족을 기다리고 있어요.</h5> -->
  </div>
  <marketList />
</template>

<script setup>
import { onMounted } from 'vue'
import { useMarketStore } from '@/stores/market'
import MarketList from '@/components/market/MarketList.vue'

const store = useMarketStore()

onMounted(() => {
  store.getProducts()
})
</script>

<style scoped>
.market {
  display: flex;
  flex-direction: column;
  /* 자식 요소를 수직으로 배치 */
  align-items: center;
  /* 자식 요소를 수평 중앙에 배치 */
  justify-content: center;
  /* 자식 요소를 수직 중앙에 배치 */
  margin: 20px 0;
}</style>