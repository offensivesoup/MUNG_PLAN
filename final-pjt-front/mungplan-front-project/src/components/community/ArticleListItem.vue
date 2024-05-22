<template>
  <div>
    <main>
        <article class="content">
          <h5>{{ article.id }}</h5>
            <RouterLink 
              :to="{ name: 'ProfileView', params: { username: article.user }}"
            >
              <span>{{ article.user }}</span>
            </RouterLink>
          <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
            <span>{{ article.title }}</span>
          </RouterLink>
          <span class="article-content"> 내용 : {{ article.content }}</span>
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

article {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  gap: 150px;
}

article > h5 { 
  font-size: 20px;
  font-weight: bold;
}

a {
  text-decoration: none;
  color: black;
  font-size: 20px;
  opacity: 1;
  transition: all 0.3s ease-in-out;
}

a:hover {
  opacity: 0.5;
}

a > span {
  font-size: 20px;
  font-weight: bold;
  color: black;
  text-decoration: none;
}
.user-profile {
  font-weight: bold;
  font-size: 20px;
  color:black;
}
</style>