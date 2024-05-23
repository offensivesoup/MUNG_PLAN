<template>
  <div class="liked-deposit liked-deposit-list">
    <LikedDepositListItem 
      v-for="deposit in depositList" 
      :key="deposit.id" 
      :deposit="deposit"
      :id="props.id" 
      @like-toggled="fetchLikedDepositList" 
    />
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import LikedDepositListItem from '@/components/accounts/LikedDepositListItem.vue'
import { useAccountStore } from '@/stores/account'
import { useRouter } from 'vue-router'

const props = defineProps({
  id: Number
})

const store = useAccountStore()
const depositList = ref(null)
const router = useRouter()

// 좋아요한 예금 목록을 가져오는 함수를 정의합니다.
const fetchLikedDepositList = async () => {
  try {
    const response = await axios({
      method: 'get',
      url: `${store.API_URL}accounts/${props.id}/liked-deposit/`,
      headers: {
        'Authorization': `Token ${store.token}`
      }
    })
    depositList.value = response.data
  } catch (error) {
    console.error(error)
  }
}

onMounted(fetchLikedDepositList)


</script>

<style scoped>
</style>