<template>
  <div>
    <h1>Create Dog</h1>
    <form @submit.prevent="createDog">
      <label for="name">Name:</label>
      <input type="text" id="name" v-model="dog.name" required>
      <br>
      <label for="age">Age:</label>
      <input type="number" id="age" v-model="dog.age" required>
      <br>
      <label for="gender">Gender:</label>
      <select id="gender" v-model="dog.gender" required>
        <option value="M">남아</option>
        <option value="F">여아</option>
        <option value="Q">중성화 수술 완료</option>
      </select>
      <br>
      <label for="birth_date">Birth Date:</label>
      <input type="date" id="birth_date" v-model="dog.birth_date" required>
      <br>
      <label for="type">Type:</label>
      <select id="type" v-model="dog.Type" required>
        <option value="1">말티즈</option>
        <option value="2">푸들</option>
        <option value="3">포메라니안</option>
        <option value="4">시츄</option>
        <option value="5">비숑프리제</option>
        <option value="6">요크셔테리어</option>
        <option value="7">진도견</option>
        <option value="8">치와와</option>
        <option value="9">스피츠</option>
        <option value="10">닥스훈트</option>
        <option value="11">리트리버</option>
        <option value="12">기타</option>
      </select>
      <br>
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/account'
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const store = useAccountStore()
const router = useRouter()
const dog = ref({
    name: '',
    age: null,
    gender: '',
    birth_date: '',
    Type: '',
})

const createDog = () => {
  axios({
    method: 'POST',
    url: `${store.API_URL}accounts/${store.state.id}/dogs/create/`,
    data: dog.value,
    headers: {
      'Authorization': `Token ${store.token}`
    }
  })
  .then(response => {
    console.log(response.data)
    router.push({ name: 'ProfileView', params: { 'username': store.state.username }})
  })
  .catch(error => {
    console.error(error.response ? error.response.data : error.message)
  })
}
</script>

<style scoped>
/* 스타일을 여기에 추가할 수 있습니다 */
</style>
