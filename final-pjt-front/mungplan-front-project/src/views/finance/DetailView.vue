<!-- 
  what : 상세 페이지! 
 -->
<template>
  <div class="deposit-detail">
    <h1>DetailView</h1>
    <div v-if="deposit">
      <p>{{ deposit.id }}</p>
      <p>{{ deposit.title }}</p>
      <p>{{ deposit.content }}</p>
      <p>{{ deposit.created_at }}</p>
      <p>{{ deposit.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import { useRoute } from 'vue-router'

const store = useDepositStore()
const route = useRoute()
const deposit = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/`
  })
    .then((response) => {
      deposit.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>

<style scoped>

</style>