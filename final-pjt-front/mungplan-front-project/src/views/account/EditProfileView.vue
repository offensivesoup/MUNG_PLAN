<template>
    <div>
        <h1>회원정보 수정</h1>
        <form @submit.prevent="updateUser(store.state.id, store.token, form)">
            <div>
                <label for="nickname">Nickname:</label>
                <input id="nickname" v-model="form.nickname" type="text">
            </div>
            <div>
                <label for="phone_number">Phone Number:</label>
                <input id="phone_number" v-model="form.phone_number" type="text">
            </div>
            <div>
                <label for="address">Address:</label>
                <textarea id="address" v-model="form.address"></textarea>
            </div>
            <div>
                <label for="password">Password:</label>
                <input id="password" v-model="form.password" type="password">
            </div>
            <button type="submit">수정</button>
      </form>
    </div>
  </template>
  
<script setup>
import { onMounted } from 'vue'
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'
import { useRouter } from 'vue-router'
import axios from 'axios'

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
      });
      console.log(response.data)

      // 사용자 정보가 성공적으로 변경된 후에 다시 사용자 정보를 가져와서 상태를 업데이트
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

          // 사용자 정보가 state 객체에 성공적으로 저장된 후에 홈 뷰로 이동
          router.push({ name: 'HomeView' })
        })
        .catch((error) => {
          console.error('사용자 정보 가져오기 실패:', error.response ? error.response.data : error.message);
        })
  } catch (error) {
      console.error(error)
  }
}
</script>
  
<style scoped>

</style>