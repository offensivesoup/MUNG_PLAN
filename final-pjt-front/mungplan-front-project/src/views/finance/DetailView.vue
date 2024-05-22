<template>
  <div class="deposit-detail">
    <h1>DetailView</h1>
    <div v-if="deposit">
      <p>{{ deposit.id }}</p>
      <p>{{ deposit.product_name }}</p>
      <p>{{ deposit.company_name }}</p>
      <p>{{ deposit.special_condition }}</p>
      <p>{{ deposit.save_term }}</p>
      <p>{{ deposit.interate_type }}</p>
      <p>{{ deposit.interate_rate }}</p>
      <p>{{ deposit.maxi_interate_rate }}</p>
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
    url: `${store.API_URL}finance/deposit/${route.params.id}`
  })
    .then((response) => {
      deposit.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>

<style scoped></style>