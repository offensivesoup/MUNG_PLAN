<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'ArticleCreateView' }">
      [CREATE]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCommunityStore } from '@/stores/community'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/community/ArticleList.vue'
import ArticleCategory from '@/components/community/Category.vue'

const store = useCommunityStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style></style>
