<template>
  <div class="deposit-list-item">
    <div class="card" style="width: 18rem;">
      <div class="card-body">
        <div class="card-logo-and-title">
          <img class="company-image" :src="`${store.API_URL}${store.staticUrl}${deposit.company_image}`" alt="company logo">
          <div class="card-titles">
            <h5 class="card-title">{{ deposit.product_name }}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{ deposit.company_name }}</h6>
          </div>
          <button @click="toggleLike" class="btn btn-primary">
            {{ liked ? 'Unlike' : 'Like' }}
          </button>
        </div>
        <p class="card-text"> 최고 금리: {{ deposit.maxi_interate_rate }}%</p>
        <p class="card-text"> 기본 금리: {{ deposit.interate_rate }}%</p>
        <RouterLink :to="{ name: 'DepositDetailView', params: { id: deposit.id }}" class="btn btn-primary">
          Detail
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useDepositStore } from '@/stores/deposit'
import { useAccountStore } from '@/stores/account'

// Vue 3의 컴파일러가 defineProps를 통해 정의된 prop을 자동으로 스코프에 포함시키지만, 이 스코프가 함수 내부로 확장되지 않는 거 같아서 함수 따로 만듦
const props = defineProps({
  deposit: Object
})

const store = useDepositStore()
const token = useAccountStore().token 
const liked = ref(false)

// 로그인 하고 테스트 해보기
const toggleLike = async () => {
  if (!props.deposit) {
    console.error('deposit is undefined');
    return
  }

  try {
    await axios.post(
        `${store.API_URL}finance/deposit/${props.deposit.id}/likes/`,
        {},
        {
          headers: {
            Authorization: `Token ${token}`
          }
        }
      )
    liked.value = !liked.value
  } catch (error) {
    console.error(error)
  }
}
</script>

<style scoped>
.deposit-list-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }

  .card {
    width: 100%;
  }

  .card-logo-and-title {
  display: flex;
  align-items: center;
  }

  .company-image {
    width: 50px;  /* 이미지의 너비를 50px로 설정 */
    height: 50px; /* 이미지의 높이를 50px로 설정 */
    object-fit: cover; /* 이미지의 비율을 유지하면서 이미지를 채움 */
  }

  .card-body {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
  }

  .card-text {
    margin-bottom: 0.5rem;
  }

  .btn-primary {
    margin-top: 1rem;
  }
</style>