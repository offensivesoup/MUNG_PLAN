<template>
  <div class="adopt-list-item">
    <div class="card" style="width: 18rem;">
      <img class="dog-image card-img-top" :src="dog.img" alt="shelterDog">
      <div class="card-body">
        <p class="card-text">{{ dog.state }}</p>
        <p class="card-title">{{ dog.kind.replace('[개]', '') }}</p>
        <p class="card-text">{{ dog.gender === 'F' ? '여성' : dog.kind === 'M' ? '남성' : '중성화 완료' }}</p>
        <p class="card-text">{{ dog.center_address.split(' ').slice(0, 2).join(' ') }}</p>
        <RouterLink :to="{ name: 'AdoptDetailView', params: { id: dog.id }}" class="btn btn-primary">
          Detail
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  dog: Object
})
</script>

<style scoped>
.dog-image {
  width: 200px; 
  height: 200px; 
  background-size: cover; /* 이미지가 너비와 높이를 모두 채우게 하려면 cover를 사용 */
  background-position: center; /* 이미지를 중앙에 위치시키려면 center를 사용 */
}
</style>