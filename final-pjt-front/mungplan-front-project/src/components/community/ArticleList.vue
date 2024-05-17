<template>
  <div>
    <Cateogry />
    <h3>Article List</h3>
    <ArticleListItem v-for="article in store.articles" :key="article.id" :article="article" />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/article'
import ArticleListItem from '@/components/community/ArticleListItem.vue'
import Cateogry from '@/components/community/Category.vue'
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

console.log(store.articles)

</script>
