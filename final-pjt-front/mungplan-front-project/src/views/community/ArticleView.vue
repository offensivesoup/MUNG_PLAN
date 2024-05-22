<template>
  <article :class="['intro', { 'fade-out': visible }]">
    <img src="@/assets/community-intro.png" alt="">
  </article>

  <article :class="['content', { 'fade-in': visible }]">
    <div>
      <h1>Article Page</h1>
      <RouterLink :to="{ name: 'ArticleCreateView' }">
        [CREATE]
      </RouterLink>
      <ArticleList />
    </div>
  </article>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCommunityStore } from '@/stores/community'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/community/ArticleList.vue'
import ArticleCategory from '@/components/community/Category.vue'

const visible = ref(false)
const store = useCommunityStore()

onMounted(() => {
  store.getArticles()
  setTimeout(() => {
    visible.value = true
  }, 500)
})

</script>

<style scoped>
.intro {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  opacity: 1;
}

.fade-out {
  opacity: 0;
  transition: opacity 2s ease-in-out;
}

.content {
  opacity: 0;
}

.fade-in {
  opacity: 1;
  transition: opacity 2s ease-in-out;
}
</style>
