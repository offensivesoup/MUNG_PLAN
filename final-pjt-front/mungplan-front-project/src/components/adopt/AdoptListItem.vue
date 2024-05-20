<template>
  <div class="adopt-list-item">
    <div class="card col-lg-4 col-md-6">
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
  .adopt-list-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
    /* box-sizing: content-box; */
  }

  .card {
    width: 100%;
    height: 26rem; /* 세로 길이를 조정합니다. */
    border-radius: 15px; /* 테두리를 둥글게 만듭니다. */
    overflow: hidden; /* 둥근 테두리 내부의 내용이 넘치지 않도록 합니다. */
    border: 0;
  }
  .dog-image {
    height: 200px;
    background-size: cover; /* 이미지를 가능한 한 크게 확장하되, 이미지의 일부가 잘릴 수 있게 하려면 cover를 사용 */
    background-position: center; /* 이미지를 중앙에 위치시키려면 center를 사용 */
    /* object-fit: cover; */
  }
  .card-body {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    font-size: 1rem;
    color: #333;
  }

  .card-text {
    margin-bottom: 0.5rem;
  }

  .btn-primary {
    margin-top: 1rem;
  }
</style>