<template>
  <div class="adopt-list">
    <AdoptListItem
      v-for="dog in store.shelterDogs"
      :key="dog.id"
      :dog="dog"
    />
  </div>
</template>

<script setup>
import { useAdoptStore } from '@/stores/adopt'
import AdoptListItem from './AdoptListItem.vue'

const store = useAdoptStore()
</script>

<style scoped>
/* 카드형식의 컨테이너 스타일 정의 */
</style>