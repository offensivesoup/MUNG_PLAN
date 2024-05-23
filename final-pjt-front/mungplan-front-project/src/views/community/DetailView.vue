<template>
  <div class="detail-view">
    <div v-if="article" class="article-card">
      <div class="article-header">
        <div>
          <h2>{{ article.title }}</h2>
          <span class="comment-date">작성 일자 : {{ formatDate(article.created_at) }}</span>
        </div>
        <div>
          <button class="delete-btn" @click="deleteArticle(article.id)"
            v-if="userStore.state.id === article.user">삭제하기</button>
          <button class="edit-btn" @click="changeArticle(article.id)"
            v-if="userStore.state.id === article.user">수정하기</button>
          <button @click="likeArticle(article.id)" v-if="userStore.state.id !== article.user"
            :class="{ 'like-button': true, 'liked': isLiked }">
            <svg class="heart" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
              <path
                d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
            </svg>
          </button>
          <p>좋아요 수 : {{ likeUsers }} 개</p>
        </div>
      </div>
      <div class="article-content">
        <p>{{ article.content }}</p>
      </div>
      <div class="article-dates">
      </div>
    </div>

    <div v-if="comments && comments.length" class="comments-section">
      <h2>Comments</h2>
      <p> 댓글 수 : {{ comments.length }} 개</p>
      <div class="comment" v-for="comment in comments" :key="comment.id">
        <div class="comment-header">
          <span class="comment-author">{{ comment.author }}</span>
          <span class="comment-date">{{ formatDate(comment.created_at) }}</span>
        </div>
        <div class="comment-content">
          <p>{{ comment.content }}</p>
        </div>
      </div>
    </div>
    <div class="create-comment">
      <form @submit.prevent="createComment(article.id)">
        <input type="text" v-model="newComment" />
        <button type="submit">댓글달기</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCommunityStore } from '@/stores/community'
import { useAccountStore } from '@/stores/account'
import { useRoute } from 'vue-router'
import router from '@/router'

const isLiked = ref(false)
const userStore = useAccountStore()
const store = useCommunityStore()
const route = useRoute()
const article = ref(null)
const comments = ref(null)
const newComment = ref(null)
const likeUsers = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}community/article/${route.params.id}/`
  })
    .then((response) => {
      article.value = response.data
      likeUsers.value = article.value.like_users.length
      console.log(response.data)
      checkLike()
      axios({
        method: 'get',
        url: `${store.API_URL}community/article/${route.params.id}/comments/`
      })
        .then((response) => {
          comments.value = response.data
          console.log(comments.value)
        })
        .catch((error) => {
          console.log(error, error.data)
        })
    })
    .catch((error) => {
      console.log(error, error.data)
    })
})

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' }
  return new Date(dateString).toLocaleDateString(undefined, options)
}

const deleteArticle = (id) => {
  axios({
    method: 'DELETE',
    url: `${store.API_URL}community/article/${route.params.id}/`,
    headers: {
      'Authorization': `Token ${userStore.state.token}`
    }
  })
    .then((response) => {
      console.log(response)
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(userStore.state)
      console.log(error, error.data)
    })
}

const checkLike = () => {
  axios({
    method: 'GET',
    url: `${store.API_URL}community/article/${route.params.id}/isliked/`,
    headers: {
      'Authorization': `Token ${userStore.state.token}`
    }
  })
    .then((response) => {
      isLiked.value = true
    })
    .catch(error => {
      isLiked.value = false
      console.log(error, error.data)
    })
}

const likeArticle = (id) => {
  axios({
    method: 'POST',
    url: `${store.API_URL}community/article/${route.params.id}/likes/`,
    headers: {
      'Authorization': `Token ${userStore.state.token}`
    }
  })
    .then((response) => {
      console.log(response)
      isLiked.value = !isLiked.value
      if (isLiked.value) {
        likeUsers.value += 1
      } else {
        likeUsers.value -= 1
      }
    })
    .catch((error) => {
      console.log(userStore.state)
      console.log(error, error.data)
    })
}

const changeArticle = (id) => {
  router.push({ name: 'ArticleUpdateView', params: { id } })
}

const createComment = (id) => {
  if (newComment.value) {
    axios({
      method: 'POST',
      url: `${store.API_URL}community/${route.params.id}/comments/`,
      headers: {
        'Authorization': `Token ${userStore.state.token}`
      },
      data: {
        content: newComment.value
      }
    })
      .then((response) => {
        console.log(response)
        axios({
          method: 'get',
          url: `${store.API_URL}community/article/${id}/comments/`,
          headers: {
            'Authorization': `Token ${userStore.state.token}`
          },
        })
          .then((response) => {
            comments.value = response.data
          })
          .catch((error) => {
            console.log(error, error.data)
          })
      })
      .catch((error) => {
        console.log(error, error.data)
      })
    newComment.value = ''
  }
}

</script>

<style scoped>
.detail-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.article-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-top: 20px;
}

.article-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
  margin-bottom: 10px;
}

.article-header h2 {
  margin: 0;
  font-size: 24px;
  color: #333;
}

.article-id {
  font-size: 14px;
  color: #999;
}

.article-content {
  margin-bottom: 20px;
  font-size: 16px;
  line-height: 1.6;
  color: #555;
}

.article-dates {
  font-size: 14px;
  color: #777;
}

.comments-section {
  margin-top: 40px;
}

.comments-section h2 {
  font-size: 20px;
  color: #333;
  margin-bottom: 20px;
}

.comment {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.comment-author {
  font-weight: bold;
  color: #333;
}

.comment-date {
  font-size: 14px;
  color: #999;
}

.comment-content {
  font-size: 16px;
  color: #555;
}

.create-comment {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background: #f0f0f0;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 20px auto;
}

.create-comment form {
  display: flex;
  flex-direction: row;
  width: 100%;
}

.create-comment input[type="text"] {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.create-comment input[type="text"]:focus {
  border-color: #5a67d8;
  outline: none;
}

.create-comment button {
  padding: 10px 20px;
  background-color: #5a67d8;
  color: white;
  border: none;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.create-comment button:hover {
  background-color: #434190;
}

.like-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 24px;
  transition: transform 0.2s;
  color: #ff5a5f;
  margin-left: 25px;
}

.like-button:hover {
  transform: scale(1.1);
}

.like-button:active {
  transform: scale(0.9);
}

.heart {
  fill: none;
  stroke: #ff5a5f;
  stroke-width: 2px;
  transition: fill 0.3s;
}

.liked .heart {
  fill: #ff5a5f;
  stroke: none;
}

button {
  padding: 10px 15px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  transform: scale(1.05);
}

button:active {
  transform: scale(0.95);
}

.delete-btn {
  background-color: #ff5a5f;
  color: white;
}

.delete-btn:hover {
  background-color: #e04848;
}

.edit-btn {
  background-color: #5a67d8;
  color: white;
  margin-left: 30px;
}

.edit-btn:hover {
  background-color: #434190;
}
</style>
