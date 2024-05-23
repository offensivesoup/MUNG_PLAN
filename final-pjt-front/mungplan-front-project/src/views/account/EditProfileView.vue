<template>
  <div class="update-user">
    <h1>회원정보 수정</h1>
    <form @submit.prevent="updateUser(store.state.id, store.token, form)" class="form">
      <div class="input-group">
        <label for="nickname" class="label">Nickname:</label>
        <input id="nickname" v-model="form.nickname" type="text" class="input-field">
      </div>
      <div class="input-group">
        <label for="phone_number" class="label">Phone Number:</label>
        <input id="phone_number" v-model="form.phone_number" type="text" class="input-field">
      </div>
      <div class="input-group">
        <label for="address" class="label">Address:</label>
        <textarea id="address" v-model="form.address" class="input-field"></textarea>
      </div>
      <button class="submit-button" @click="goToChangePassword">비밀번호 변경</button>
      <button type="submit" class="submit-button">수정</button>
    </form>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'
import { useRouter, useRoute, RouterLink } from 'vue-router'
import axios from 'axios'
const route = useRoute()
const store = useAccountStore()
const form = ref({
  nickname: '',
  phone_number: '',
  address: '',
  password: '',
})
const router = useRouter()

onMounted(async () => {
  try {
    const response = await axios.get(`${store.API_URL}accounts/api/users/${store.state.id}/`, {
      headers: {
        'Authorization': `Token ${store.token}`
      }
    })
    form.value = response.data
  } catch (error) {
    console.error(error)
  }
})

const updateUser = async (userId, token, userData) => {
  try {
    const response = await axios.put(`${store.API_URL}accounts/api/users/${userId}/`, userData, {
      headers: {
        'Authorization': `Token ${token}`
      }
    })
    console.log(response.data)

    await axios.get(`${store.API_URL}accounts/userinfo/`, {
      headers: {
        'Authorization': `Token ${token}`
      }
    })
      .then((response) => {
        console.log(response)
        store.state.id = response.data.id
        store.state.username = response.data.username
        store.state.nickname = response.data.nickname
        store.state.profileImg = response.data.profile_img
        store.state.dogs = response.data.dogs
        store.state.articles = response.data.articles

        router.push({ name: 'HomeView' })
      })
      .catch((error) => {
        console.error('사용자 정보 가져오기 실패:', error.response ? error.response.data : error.message)
      })
  } catch (error) {
    console.error(error)
  }
}

const goToChangePassword = () => {
  router.push({ name: 'PasswordChangeView', params: { username: route.params.username } })
}
</script>

<style scoped>
.update-user {
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
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 1.2rem;
  margin-top: 20px;
  margin-left: 20px;
  margin-right: 20px;
}

.submit-button:hover {
  background-color: rgb(255, 166, 0, 1);
}
</style>
