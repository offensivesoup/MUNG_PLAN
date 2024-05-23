<template>
  <div class="create-dog">
    <h1>강아지 정보 추가</h1>
    <form @submit.prevent="createDog" class="form">
      <div class="input-group">
        <label for="name" class="label">이름:</label>
        <input type="text" id="name" v-model="dog.name" class="input-field" required>
      </div>
      <div class="input-group">
        <label for="age" class="label">나이:</label>
        <input type="number" id="age" v-model="dog.age" class="input-field" required>
      </div>
      <div class="input-group">
        <label for="gender" class="label">성별:</label>
        <select id="gender" v-model="dog.gender" class="input-field" required>
          <option value="M">남아</option>
          <option value="F">여아</option>
          <option value="Q">중성화 수술 완료</option>
        </select>
      </div>
      <div class="input-group">
        <label for="birth_date" class="label">생년월일:</label>
        <input type="date" id="birth_date" v-model="dog.birth_date" class="input-field" required>
      </div>
      <div class="input-group">
        <label for="type" class="label">종:</label>
        <select id="type" v-model="dog.Type" class="input-field" required>
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
      </div>
      <button type="submit" class="submit-button">저장</button>
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
      router.push({ name: 'ProfileView', params: { 'username': store.state.username } })
    })
    .catch(error => {
      console.error(error.response ? error.response.data : error.message)
    })
}
</script>

<style scoped>
.create-dog {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
}

.form {
  border: 2px solid #333;
  padding: 30px;
  border-radius: 10px;
  max-width: 500px;
  margin: 0 auto;
  text-align: center;
}

.input-group {
  margin-bottom: 20px;
}

.label {
  font-weight: bold;
}

.input-field {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.submit-button {
  background-color: rgb(255, 166, 0, 0.3);
  color: black;
  padding: 15px 30px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 1.2rem;
  margin-top: 20px;
}

.submit-button:hover {
  background-color: rgb(255, 166, 0, 1);
}
</style>
