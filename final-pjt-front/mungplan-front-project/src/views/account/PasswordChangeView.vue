<template>
  <div class="change-password">
    <h1>비밀번호 변경</h1>
    <form @submit.prevent="changePassword" class="form">
      <div class="input-group">
        <label for="new_password1" class="label">새 비밀번호</label>
        <input type="password" v-model.trim="new_password1" id="new_password1" class="input-field">
      </div>
      <div class="input-group">
        <label for="new_password2" class="label">새 비밀번호 확인</label>
        <input type="password" v-model.trim="new_password2" id="new_password2" class="input-field">
      </div>
      <button type="submit" class="submit-button">비밀번호 변경</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'
import axios from 'axios'
import { useRouter } from 'vue-router'

const store = useAccountStore()
const router = useRouter()

const new_password1 = ref(null)
const new_password2 = ref(null)

const changePassword = async () => {
  if (new_password1.value !== new_password2.value) {
    alert('비밀번호가 일치하지 않습니다.')
    return
  }

  const payload = {
    new_password1: new_password1.value,
    new_password2: new_password2.value
  }

  try {
    const response = await axios.post(`${store.API_URL}auth/password/change/`, payload, {
      headers: {
        'Authorization': `Token ${store.token}`
      }
    })
    console.log(response.data)
    alert('비밀번호가 성공적으로 변경되었습니다.')
    router.push({ name: 'HomeView' })
  } catch (error) {
    console.error(error)
    alert('비밀번호 변경 중 오류가 발생했습니다.')
  }
}
</script>

<style scoped>
.change-password {
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
