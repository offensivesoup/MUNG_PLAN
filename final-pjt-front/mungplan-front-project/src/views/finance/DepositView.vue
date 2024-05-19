<template>
  <div class="deposit recommendDeposit-banner">
    <div class="banner-content">
      <h1><b>UserName</b>님과 <b>dogName</b>을 위한</h1>
      <h1><b>맞춤 예적금</b>이 있다면~?</h1>
      <p>멍플팬만의 스페셜 알고리즘 추천 받으러 가기 !</p>
      <RouterLink :to="{ name: 'RecommendDepositView'}" type="button" class="recommend-button btn btn-light">
        추천 받기
      </RouterLink>
    </div>
  </div>

  <div class="deposit deposit-header">
    <h1>내 아이를 위한 비상금</h1>
  </div>
  <div class="deposit deposit-main">
    <!-- + : 필터 - 나이, 성별, 중성화, 지역, 품종? 너무 많은가 -->
  </div>
  <div class="deposit deposit-count-info">
    <img src="/deposit/passbook.png" alt="passbook icon" style="width: 40px; height: 40px;">
    <h5 style="margin: 0; font-size: 18px;">{{ store.deposits.length }}개의 상품으로 미리 대비해보세요.</h5>
  </div>
  <DepositList />
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import DepositList from '@/components/finance/DepositList.vue'

const store = useDepositStore()

onMounted(() => {
  store.getDeposits()
})
</script>

<style scoped>
.deposit-count-info {
  display: flex;
  align-items: center;
  margin: 20px 0;
}
.deposit {
  display: flex;
  justify-content: center;
  align-items: center;
}
.recommendDeposit-banner{
  background-image: url('/deposit/happyDog.jpg');
  background-size: auto;
  display: flex;
  justify-content: flex-end;
  padding-right: 8%;
  color: white;
  height: 530px;
  position: relative;
  margin-bottom: 30px;
}
.recommendDeposit-banner::before { 
  position: absolute;
    content: "";
    top:0px;
    left:0px;
    width: 100%;
    height: 100%;
    background-color:rgb(36 29 14 / 22%)
}
.banner-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;  /* 오버레이 위에 요소들이 위치하도록 position을 relative로 설정합니다. */
}
.recommend-button {
  color: rgb(36, 166, 69);
  padding: 10px 20px;
  border: none;
}
</style>