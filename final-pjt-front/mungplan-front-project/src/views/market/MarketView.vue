<template>
  <article :class="['intro', { 'fade-out': visible }]">
    <img src="@/assets/market-intro.png" alt="">
  </article>

  <article :class="['content', { 'fade-in': visible }]">
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
  </article>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMarketStore } from '@/stores/market'
import MarketList from '@/components/market/MarketList.vue'

const store = useMarketStore()
const visible = ref(false)
onMounted(() => {
  store.getProducts()
  setTimeout(() => {
    visible.value = true
  }, 500)
})
</script>

<style scoped>
.intro {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  opacity: 1;
}

.fade-out {
  opacity: 0;
  transition: opacity 2s ease-in-out;
  z-index: -1;
}

.content {
  opacity: 0;
}

.fade-in {
  opacity: 1;
  transition: opacity 2s ease-in-out;
}

.market {
  display: flex;
  flex-direction: column;
  /* 자식 요소를 수직으로 배치 */
  align-items: center;
  /* 자식 요소를 수평 중앙에 배치 */
  justify-content: center;
  /* 자식 요소를 수직 중앙에 배치 */
  margin: 20px 0;
}
</style>