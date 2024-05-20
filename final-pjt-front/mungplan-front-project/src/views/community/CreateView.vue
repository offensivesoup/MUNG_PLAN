<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <div>
        <label for="category">카테고리 : </label>
        <select v-model="category" id="category">
          <option disabled value="">카테고리를 선택하세요</option>
          <option>고민나누기</option>
          <option>중고장터</option>
          <option>동네사람들</option>
        </select>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCommunityStore } from '@/stores/community'
import { useAccountStore } from '@/stores/account'
import { useRouter } from 'vue-router'

const store = useCommunityStore()
const token = useAccountStore().token
const title = ref(null)
const content = ref(null)
const category = ref(null)
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}community/articles/create/`,
    headers: {
      'Authorization': `Token ${token}`
    },
    data: {
      title: title.value,
      content: content.value,
      category: category.value
    }
  })
    .then((response) => {
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>

<style>

</style>
