<template>
  <div class="adopt-list-item">
    <img src="#" alt="shelterDog">
    <p>강아지 정보 출력</p>
  </div>

  <RouterLink :to="{ name: 'AdoptDetailView', params: { id: dog.id }}">
      [Detail]
  </RouterLink>
  <hr>
</template>

<script setup>
defineProps({
  dog: Object
})
</script>

<style scoped>
/* 개별 카드의 스타일 정의 */
</style>