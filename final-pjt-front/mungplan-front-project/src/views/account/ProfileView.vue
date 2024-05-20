<template>
  <div>
    <template v-if="loading">
      <p>Loading...</p>
    </template>
    <template v-else>
      <p> 생년월일 : {{ birthDate }}</p>
      <p> 이름 : {{ firstName }}</p>
      <p> 닉네임 : {{ nickName }}</p>
      <p> 전화번호 : {{ phone_number }}</p>
      <p> 주소 : {{ address }}</p>
      <p> 프로필 : <img :src="`${store.API_URL}${profile}`" alt="프로필이미지"></p>
      <p> 팔로잉 : {{ followings }}</p>
    </template>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/account';
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'

const $route = useRoute()
const store = useAccountStore()

const loading = ref(false)
const username = ref('')
const birthDate = ref('')
const firstName = ref('')
const nickName = ref('')
const phone_number = ref('')
const address = ref('')
const profile = ref('')
const followings = ref('')

onMounted(async () => {
  try {
    loading.value = true
    const userData = await store.userDetail($route.params.username)
    console.log(userData)
    username.value = userData.username
    birthDate.value = userData.birth_date
    firstName.value = userData.first_name
    nickName.value = userData.nickname
    phone_number.value = userData.birth_date
    address.value = userData.address
    profile.value = userData.profile_img.substring(1)
    followings.value = userData.followings
  } catch (error) {
    console.log(error)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped></style>
