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
      <h1 style="font-size: 3.2rem; padding-top: 20px;">내 아이를 위한 비상금</h1>
    </div>
       <div class="deposit deposit-filters">
      <label for="type-filter">종류</label>
      <select id="type-filter" v-model="selectedFilters.type">
        <option value="">전체</option>
        <option value="예금">예금</option>
        <option value="적금">적금</option>
        <option value="펫상품">펫적금상품</option>
      </select>

      <label for="financial-type-filter">금융권 종류</label>
      <select id="financial-type-filter" v-model="selectedFilters.financialType">
        <option value="">전체</option>
        <option value="1금융권">1금융권</option>
        <option value="2금융권">2금융권</option>
      </select>

      <label for="period-filter">기간</label>
      <select id="period-filter" v-model="selectedFilters.period">
        <option value="">전체</option>
        <option value="12">12개월</option>
        <option value="24">24개월</option>
        <option value="36">36개월</option>
      </select>
    </div>

    <div class="selected-filters">
      <div v-if="selectedFilters.type">
        <span>{{ selectedFilters.type }} <button @click="selectedFilters.type = ''">X</button></span>
      </div>
      <div v-if="selectedFilters.financialType">
        <span>{{ selectedFilters.financialType }} <button @click="selectedFilters.financialType = ''">X</button></span>
      </div>
      <div v-if="selectedFilters.period">
        <span>{{ selectedFilters.period }}개월 <button @click="selectedFilters.period = ''">X</button></span>
      </div>
    </div>

    <div class="deposit deposit-count-info" style="display: flex; justify-content: space-between; padding:0 250.500px; margin: 20px 30px;">
      <div>
        <img src="/deposit/passbook.png" alt="passbook icon" style="width: 30px; height: 30px;">
        <h5 style="margin: 0; font-size: 15px; display: inline;">{{ productCount }}개의 상품으로 미리 대비해보세요.</h5>
      </div>
      <div>
        <select v-model="sortOrder">
          <option value="highest">최고금리순</option>
          <option value="basic">기본금리순</option>
        </select>
      </div>
    </div>
    <DepositList :filteredAndSortedDeposits="filteredAndSortedDeposits"/>
  </article>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import { useAccountStore } from '@/stores/account'
import DepositList from '@/components/finance/DepositList.vue'

const store = useDepositStore()
const accountStore = useAccountStore()

onMounted(() => {
  store.getDeposits()
})

const sortOrder = ref('highest')

// 필터링 옵션
const selectedFilters = ref({
  type: '', // 적금/예금
  financialType: '', // 전체/1금융권
  period: '' // 12/24/36
})

// 필터링된 목록 계산
const filteredDeposits = computed(() => {
  return store.deposits.filter(deposit => {
    console.log(deposit.category)
    // 종류 필터링
    let matchesType = true;
    if (selectedFilters.value.type) {
      if (selectedFilters.value.type === '적금') {
        matchesType = deposit.category.includes('적금')
      } else if (selectedFilters.value.type === '예금') {
        matchesType = deposit.category.includes('예금')
      } else if (selectedFilters.value.type === '펫상품') {
        matchesType = deposit.product_name.includes('펫');
      }
    }

    // 금융권 종류 필터링
    let matchesFinancialType = true;
    const financialKeywords = ['카카오', '케이뱅크', '토스', '국민', '신한', '우리', '하나', '한국스탠다드차타드', '한국씨티', '경남', '광주', '대구', '부산', '전북', '제주', '농협', '수협', '중소기업', '한국산업'];
    if (selectedFilters.value.financialType) {
      matchesFinancialType = financialKeywords.some(keyword => deposit.company_name.includes(keyword));
    } else {
      matchesFinancialType = !financialKeywords.some(keyword => deposit.company_name.includes(keyword));
    }

    // 기간 필터링
    let matchesPeriod = true;
    if (selectedFilters.value.period) {
      matchesPeriod = deposit.save_term == parseInt(selectedFilters.value.period);
    }

    return matchesType && matchesFinancialType && matchesPeriod;
  });
});

// 정렬된 목록 계산
const sortedDeposits = computed(() => {
  return [...store.deposits].sort((a, b) => {
    if (sortOrder.value === 'highest') {
      return b.maxi_interate_rate - a.maxi_interate_rate
    } else {
      return b.interate_rate - a.interate_rate
    }
  })
})

// 필터링 및 정렬된 목록 계산
const filteredAndSortedDeposits = computed(() => {
  const filtered = filteredDeposits.value
  const sorted = sortedDeposits.value

  return sorted.filter(deposit => filtered.includes(deposit))
})

// 상품 수 계산
const productCount = computed(() => {
  return filteredAndSortedDeposits.value.length
})

// 필터 값 변경 시 필터링 및 정렬된 목록 업데이트
watch([filteredDeposits, sortOrder], ([filtered, order]) => {
  // 필터링된 목록
  let filteredList = filtered.slice()

  // 정렬
  if (order === 'highest') {
    filteredList.sort((a, b) => b.maxi_interate_rate - a.maxi_interate_rate)
  } else {
    filteredList.sort((a, b) => a.interate_rate - b.interate_rate)
  }

  // 정렬된 목록 업데이트
  sortedDeposits.value = filteredList

  // 필터링된 목록과 정렬된 목록의 교집합을 찾음
  const intersectedDeposits = filteredList.filter(deposit => sortedDeposits.value.includes(deposit))

  // 교집합을 저장
  filteredAndSortedDeposits.value = intersectedDeposits
})

</script>

<style scoped>
.intro {
  display: flex;
  flex-direction: row;
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