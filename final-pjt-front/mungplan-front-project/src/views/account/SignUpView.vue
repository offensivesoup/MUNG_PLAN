<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">아이디 : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password1">비밀번호 : </label>
        <input type="password" v-model.trim="password1" id="password1">
      </div>
      <div>
        <label for="password2">비밀번호 확인 : </label>
        <input type="password" v-model.trim="password2" id="password2">
      </div>
      <div>
        <label for="nickname">닉네임 : </label>
        <input type="text" v-model.trim="nickname" id="nickname">
      </div>
      <div>
        <label for="phone_number">전화번호 : </label>
        <input type="text" v-model.trim="phoneNumber" id="phoneNumber">
      </div>
      <div>
        <label for="address">주소 : </label>
        <input type="text" v-model.trim="address" id="address">
      </div>
      <div>
        <label for="profile_img">프로필이미지 : </label>
        <input type="file" accept="image/png, image/jpeg" @change="onFileChange" id="profileImg">
      </div>
      <div>
        <label for="birthdate">생년월일 : </label>
        <input type="date" v-model.trim="birthDate" id="birthDate">
      </div>
      <div>
        <label for="first_name">이름 : </label>
        <input type="text" v-model.trim="firstName" id="first_name">
      </div>
      <div>
        <label for="last_name">성 : </label>
        <input type="text" v-model.trim="lastName" id="last_name">
      </div>
      <input type="submit">
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

<style></style>
