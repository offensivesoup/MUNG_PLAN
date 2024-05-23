<template>
  <div class="dogs dogs-header">
    <h1 style="text-align: center; font-size: 3rem; padding-top: 10px;">{{ route.query.nickname }}님의 강아지</h1>
  </div>
  <DogList :id="Number(route.query.id)"/>
</template>
  
<script setup>
import { onMounted, ref } from 'vue'
import { useAccountStore } from '@/stores/account'
import DogList from '@/components/accounts/DogList.vue'
import { useRoute } from 'vue-router'

const store = useAccountStore()
const route = useRoute()
</script>

<style scoped>
</style>
