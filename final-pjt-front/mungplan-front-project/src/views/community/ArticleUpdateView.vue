<template>
    <div class="form-container">
      <h1>게시글 작성</h1>
      <form @submit.prevent="updateArticle(id)" class="article-form">
        <div class="form-group">
          <label for="category">카테고리 </label>
          <select v-model="category" id="category" class="form-control">
            <option disabled value="">카테고리를 선택하세요</option>
            <option>고민나누기</option>
            <option>중고장터</option>
            <option>동네사람들</option>
          </select>
        </div>
        <div class="form-group">
          <label for="title">{{ title }} </label>
          <input type="text" v-model.trim="title" id="title" class="form-control">
        </div>
        <div class="form-group">
          <label for="content">{{ content }} </label>
          <textarea v-model.trim="content" id="content" class="form-control"></textarea>
        </div>
        <input type="submit" value="게시글 작성" class="submit-button">
      </form>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref, onMounted } from 'vue'
  import { useCommunityStore } from '@/stores/community'
  import { useAccountStore } from '@/stores/account'
  import { useRouter, useRoute } from 'vue-router'
  
  const store = useCommunityStore()
  const token = useAccountStore().token
  const title = ref(null)
  const content = ref(null)
  const category = ref(null)
  const router = useRouter()
  const id = useRoute().params.id

    onMounted(()=>{
        if (id) {
        axios({
            method: 'get',
            url: `${store.API_URL}community/article/${id}/`,
            headers: {
            'Authorization': `Token ${token}`
            }
        })
        .then((response) => {
            title.value = response.data.title
            content.value = response.data.content
            category.value = response.data.category
            })
        .catch((error) => {
            console.log(error)
            })
        }
    })

  const updateArticle = function (article) {
    axios({
      method: 'PUT',
      url: `${store.API_URL}community/article/${article}/`,
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
        router.push({ name: 'ArticleDetailView' , parmas : {'id' : id}})
      })
      .catch((error) => {
        console.log(error)
      })
  }
  </script>
  
  <style scoped>
  .form-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: rgb(255, 192, 156, 0.5);
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-top: 100px;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
  }
  
  .article-form {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
  }
  
  .form-control {
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 5px;
    transition: border-color 0.3s;
  }
  
  .form-control:focus {
    border-color: #007bff;
    outline: none;
  }
  
  textarea.form-control {
    resize: vertical;
    height: 150px;
  }
  
  .submit-button {
    padding: 10px;
    font-size: 16px;
    color: white;
    background-color: rgb(180, 95, 95, 0.5);
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .submit-button:hover {
    background-color: rgb(180, 95, 95, 1);
  }
  </style>
  