<template>
  <div class="loading" v-if="store.isLoading">
    <h2>멍플랜이 상품을 준비하고 있습니다.</h2>
    <div class="spinner-grow" role="status">
      <span class="sr-only">Loading...</span>
    </div>
  </div>

  <article v-if="!store.isLoading" class="bank-content">
    <!-- 은행 작성 -->
    <div class="deposit recommendDeposit-banner">
      <div class="banner-content">
        <div class="content-header">
          <div v-if="accountStore.state.isAuthenticated">
            <h1><b style="text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);">{{ accountStore.state.nickname}}</b>님을 위한</h1>
            <h1><b style="text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);">맞춤 예적금</b>이 준비되었습니다</h1>
          </div>
          <div v-else>
            <h1><b>당신을 위한</b></h1>
            <h1><b>맞춤 예적금</b>이 준비되었습니다</h1>
          </div>
        </div>
        <p style="font-size: large;">개인과 강아지 모두를 분석하여 최적의 솔루션을 제공하는 멍플랜의 스페셜 알고리즘</p>
        <RouterLink :to="{ name: 'RecommendDepositView' }" type="button" class="recommend-button btn">
          <b>지금 추천 받으러 가기</b>
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
  </article>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import { useAccountStore } from '@/stores/account'
import DepositList from '@/components/finance/DepositList.vue'
const store = useDepositStore()
const accountStore = useAccountStore()

onMounted(() => {
  store.getDeposits()
})

</script>

<style scoped>
.intro {
  display: flex;
  flex-direction: row;
}

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

.recommendDeposit-banner {
  background-image: url('/deposit/강아지.jpg');
  background-size: auto;
  display: flex;
  justify-content: center;
  color: white;
  height: 600px;
  position: relative;
  margin-bottom: 30px;
  background-position: 50% 50%;
}

.recommendDeposit-banner::before {
  position: absolute;
  content: "";
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  background-color: rgb(36 29 14 / 35%)
}

.banner-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  /* 오버레이 위에 요소들이 위치하도록 position을 relative로 설정합니다. */
}
.content-header{
  padding-bottom: 10px;
  text-align: center;
}
.content-header h1{
  font-size: 3rem;
  font-family: 'Cafe24Ssurround';
  color:#f0e6cd;
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2); /* 그림자 추가 */
  letter-spacing: 1px;
}
.recommend-button {
  color: #1d1101;
  --bs-btn-border-color: #382206;
  padding: 10px 20px;
  border-color: #22150362;
  background-color: rgba(247, 220, 185, 0.452);
  font-size: 1.2rem;
}
.recommend-button:hover {
  border-color: #1d1101c7;
  background-color: rgba(247, 220, 185, 0.808);
}
</style>