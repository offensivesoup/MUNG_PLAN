<template>
  <div>
    <div class="row row-first text-white">
      <div class="row-first-image col-md-6">
        <img :src="`${depositStore.API_URL}${depositStore.staticUrl}${deposit.company_image}`" alt="은행 로고">
      </div>
      <div class="row-first-info col-md-6">
        <h4> COMPANY NAME: {{ deposit.company_name }}</h4>
        <h4> PRODUCT NAME: {{ deposit.product_name }}</h4>
        <h4> MAX INTEREST RATE: {{ deposit.maxi_interate_rate }}%</h4>
        <h4> INTEREST RATE: {{ deposit.interate_rate }}%</h4>
        <button v-if="props.id === accountStore.state.id" @click="toggleLike" class="btn btn-primary" style="width: 500px;">
            {{ liked ? 'Unlike' : 'Like' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { useDepositStore } from '@/stores/deposit'
import { useAccountStore } from '@/stores/account'
import { ref } from 'vue'

const depositStore = useDepositStore()
const accountStore = useAccountStore()
const props = defineProps({
  deposit: Object,
  id: Number
})

const emit = defineEmits(['like-toggled'])

const liked = ref(true)

const toggleLike = async () => {
  if (!props.deposit) {
    console.error('deposit is undefined')
    return
  }

  try {
    await axios.post(
      `${depositStore.API_URL}finance/deposit/${props.deposit.id}/likes/`,
      {},
      {
        headers: {
          Authorization: `Token ${accountStore.token}`
        }
      }
    )
    liked.value = !liked.value

    // 'like-toggled' 이벤트를 발생시킵니다.
    emit('like-toggled')
  } catch (error) {
    console.error(error)
  }
}
</script>

<style scoped>
.row {
  margin: 30px 0; /* row 클래스 간의 간격을 20px로 설정합니다. */
}
.row-first {
  display: flex;
  align-items: center;
  background-color: #F7CCAC;
  border-radius: 20px;
  height: 300px;
}
.row-first-info, .row-first-image {
  flex: 1; /* flex 속성을 사용하여 요소의 크기를 조절합니다. */
  margin: 0 20px; /* margin을 조절하여 요소의 위치를 조절합니다. */
  display: flex; /* flexbox 모델을 사용합니다. */
}
.row-first-info {
  flex: 7; /* row-first-first 요소가 row-first의 70%를 차지하도록 합니다. */
  flex-direction: column;
  justify-content: left;
}
.row-first-image {
  flex: 6; /* row-first-image 요소가 row-first의 30%를 차지하도록 합니다. */
  display: flex; /* flexbox 모델을 사용합니다. */
  justify-content: center; /* 가로 방향으로 중앙에 위치하도록 합니다. */
  align-items: center; /* 세로 방향으로 중앙에 위치하도록 합니다. */
}
.row-first-image img {
  width: auto; /* 이미지의 가로 크기를 조절합니다. */
  height: 150px; /* 이미지의 세로 크기를 원본 비율에 맞게 조절합니다. */
}
h4 {
  color: black;
  padding: 2px;
}
</style>
