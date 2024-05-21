<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>
      <RouterLink 
        :to="{ name: 'ProfileView', params: { username: article.user }}"
      >
        {{ article.user }}
      </RouterLink>
    </p>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink 
      :to="{ name: 'ArticleDetailView', params: { id: article.id }}"
    >
      [DETAIL]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
