<template>
  <div>
    <main>
      <article class="content">
        <h6>{{ article.id }} 번째 글</h6>
        <div class="user">
          <RouterLink :to="{ name: 'ProfileView', params: { username: article.user } }">
            <span>{{ article.user }}</span>
          </RouterLink>
        </div>
        <div class="title">
          <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id } }">
            <span>{{ article.title }}</span>
          </RouterLink>
        </div>
        <div class="writing">
          <span class="article-content"> 내용 : {{ article.content }}</span>
        </div>
        <div class="like">
          <span class="article-likes"> 좋아요 수 : {{ article.like_users.length }} 개</span>
        </div>
      </article>
      <hr>
    </main>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>

<style scoped>
article.content {
  display: grid;
  grid-template-columns: 100px 1fr;
  gap: 10px 30px;
  /* 줄 간격을 조절할 수 있습니다 */
  align-items: start;
}

article.content>h5 {
  grid-column: 1 / 2;
  font-size: 20px;
  font-weight: bold;
}

article.content>.user,
article.content>.title,
article.content>.writing,
article.content>.like {
  grid-column: 2 / 3;
}

article.content>.user,
article.content>.title,
article.content>.writing,
article.content>.like {
  display: flex;
  align-items: center;
}

article.content>.user a,
article.content>.title a {
  font-size: 20px;
  font-weight: bold;
  color: black;
  text-decoration: none;
  transition: opacity 0.3s ease-in-out;
}

article.content>.user a:hover,
article.content>.title a:hover {
  opacity: 0.5;
}

.article-content,
.article-likes {
  font-size: 20px;
}

.page-button {
  background-color: transparent;
  border: none;
  margin: 30px;
  font-size: 20px;
  transition: color 0.3s ease;
  /* 색 변화에 대한 transition 효과를 추가합니다. */
}

.page-button>img {
  width: 60px;
  transition: width 1s ease-in;
}

.article-btn>span {
  font-size: 20px;
  margin: 40px;
}
</style>