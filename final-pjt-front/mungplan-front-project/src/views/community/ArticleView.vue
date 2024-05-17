<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'CreateView' }">
      [CREATE]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/community/ArticleList.vue'
import ArticleCategory from '@/components/community/Category.vue'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style></style>
