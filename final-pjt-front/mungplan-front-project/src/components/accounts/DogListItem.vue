<template>
  <div>
    <div class="row row-first text-white">
      <div class="row-first-image col-md-6">
        <img :src="`${store.API_URL}${dog.dog_img}`" alt="강아지 프로필 이미지">
      </div>
      <div class="row-first-info col-md-6">
        <h3> NAME: {{ dog.name }}</h3>
        <h3> BREED: <span v-if="dog.breed">{{ dog.breed }}</span><span v-else>기타</span></h3>
        <h3> AGE: {{ dog.age }}살</h3>
        <h3> GENDER: <span v-if="dog.gender === 'M'">남아</span><span v-else-if="dog.gender === 'F'">여아</span><span v-else>중성화 완료</span></h3>
        <!-- <button class="btn follow-btn btn-primary" @click="toggleFollow" v-if="store.state.id && store.state.id !== profileUserId">
          {{ isFollowing ? 'Unfollow' : 'Follow' }}
        </button>
        <button class="btn add-btn btn-primary" @click="goToAddDog" v-else-if="store.state.id">
          강아지 정보 추가
        </button> -->
      </div>
    </div>
  </div>    
</template>

<script setup>
import { useAccountStore } from '@/stores/account'

const store = useAccountStore()
defineProps({
  dog: Object
})
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
    margin: 0 10px; /* margin을 조절하여 요소의 위치를 조절합니다. */
    display: flex; /* flexbox 모델을 사용합니다. */
  }
  .row-first-info {
    flex: 5; /* row-first-first 요소가 row-first의 70%를 차지하도록 합니다. */
    flex-direction: column;
    justify-content: left;
  }
  
  .row-first-image {
    flex: 6; /* row-first-imagea 요소가 row-first의 30%를 차지하도록 합니다. */
    display: flex; /* flexbox 모델을 사용합니다. */
    justify-content: center; /* 가로 방향으로 중앙에 위치하도록 합니다. */
    align-items: center; /* 세로 방향으로 중앙에 위치하도록 합니다. */
  
  }
  .row-first-image img {
    width: auto; /* 이미지의 가로 크기를 조절합니다. */
    height: 200px; /* 이미지의 세로 크기를 원본 비율에 맞게 조절합니다. */
  }

  h3{
    color: black;
    padding: 2px;
  }
</style>