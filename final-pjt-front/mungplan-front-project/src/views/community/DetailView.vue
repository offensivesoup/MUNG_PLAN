<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="article">
      <p>{{ article.id }}</p>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <p>{{ article.created_at }}</p>
      <p>{{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCommunityStore } from '@/stores/community'
import { useRoute } from 'vue-router'

const store = useCommunityStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    // url: `${store.API_URL}${route.params.id}`
  })
    .then((response) => {
      article.value = response.data
    })
    .catch((error) => {
      console.log(error, error.data)
    })
})

</script>

<style>

</style>
