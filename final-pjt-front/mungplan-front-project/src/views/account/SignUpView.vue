<template>
  <div class="signup">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" class="form">
      <div class="input-group">
        <label for="username" class="label">아이디</label>
        <input type="text" v-model.trim="username" id="username" class="input-field">
      </div>
      <div class="input-group">
        <label for="password1" class="label">비밀번호</label>
        <input type="password" v-model.trim="password1" id="password1" class="input-field">
      </div>
      <div class="input-group">
        <label for="password2" class="label">비밀번호 확인</label>
        <input type="password" v-model.trim="password2" id="password2" class="input-field">
      </div>
      <div class="input-group">
        <label for="nickname" class="label">닉네임</label>
        <input type="text" v-model.trim="nickname" id="nickname" class="input-field">
      </div>
      <div class="input-group">
        <label for="phoneNumber" class="label">전화번호</label>
        <input type="text" v-model.trim="phoneNumber" id="phoneNumber" class="input-field">
      </div>
      <div class="input-group">
        <label for="address" class="label">주소</label>
        <input type="text" v-model.trim="address" id="address" class="input-field">
      </div>
      <div class="input-group">
        <label for="profileImg" class="label">프로필 이미지</label>
        <input type="file" accept="image/png, image/jpeg" @change="onFileChange" id="profileImg" class="input-field">
      </div>
      <div class="input-group">
        <label for="birthDate" class="label">생년월일</label>
        <input type="date" v-model.trim="birthDate" id="birthDate" class="input-field">
      </div>
      <div class="input-group">
        <label for="firstName" class="label">이름</label>
        <input type="text" v-model.trim="firstName" id="firstName" class="input-field">
      </div>
      <div class="input-group">
        <label for="lastName" class="label">성</label>
        <input type="text" v-model.trim="lastName" id="lastName" class="input-field">
      </div>
      <button type="submit" class="submit-button">가입하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const phoneNumber = ref(null)
const address = ref(null)
const profileImg = ref(null)
const birthDate = ref(null)
const firstName = ref(null)
const lastName = ref(null)

const store = useAccountStore()

const onFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    profileImg.value = file;
  }
}

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    phoneNumber: phoneNumber.value,
    address: address.value,
    profileImg: profileImg.value,
    birthDate: birthDate.value,
    firstName: firstName.value,
    lastName: lastName.value
  }
  store.signUp(payload)
}

</script>

<style scoped>
.signup {
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
