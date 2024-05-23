<template>
  <div style="text-align: right; padding-right: 3px;">
    <button class="btn btn-outline-dark add-btn" @click="goToAddDog" v-if="store.state.id == props.id">
      강아지 정보 추가
    </button>
  </div>
  <div class="dogs dogs-list">
    <DogListItem v-for="dog in dogs" :key="dog.id" :dog="dog" />
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import DogListItem from '@/components/accounts/DogListItem.vue'
import { useAccountStore } from '@/stores/account'
import { useRouter } from 'vue-router'

const props = defineProps({
  id: Number
})

const store = useAccountStore()
const dogs = ref(null)
const router = useRouter()

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}accounts/${props.id}/dogs/`
  })
    .then((response) => {
      console.log(response)
      dogs.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})

// 어차피 본인만 갈 수 있으니까 state 써도 되겠지..?
const goToAddDog = () => {
  router.push({ name: 'DogCreateView', params: { username: store.state.nickname } })
}
</script>

<style scoped>
.add-btn{
  --bs-btn-border-color: #B46060;
  color:#B46060;
  --bs-btn-hover-bg: #4D4D4D;
  border: solid;
  font-weight: bold;
}
</style>