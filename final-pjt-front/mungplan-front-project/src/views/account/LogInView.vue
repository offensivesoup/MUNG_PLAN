<template>
  <div class="sign">
    <h1>로그인</h1>
    <form @submit.prevent="logIn" class="form">
      <div class="input-group">
        <label for="username" class="label">Username</label>
        <input type="text" v-model.trim="username" id="username" class="input-field">
      </div>
      <div class="input-group">
        <label for="password" class="label">Password</label>
        <input type="password" v-model.trim="password" id="password" class="input-field">
      </div>
      <button type="submit" class="submit-button">로그인</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

const username = ref(null)
const password = ref(null)
const store = useAccountStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>
.sign {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-top: 100px;
}

.form {
  border: 2px solid #333;
  padding: 30px;
  border-radius: 50px;
  max-width: 500px;
  margin: 0 auto;
  text-align: center;
}

.input-group {
  margin-bottom: 30px;
}

.label {
  font-weight: bold;
}

.input-field {
  width: 100%;
  padding: 15px;
  margin-top: 10px;
  border: 1px solid #ccc;
  border-radius: 30px;
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
