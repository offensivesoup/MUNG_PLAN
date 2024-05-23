<template>
  <Cateogry />
  <div class="create-link">
    <RouterLink :to="{ name: 'ArticleCreateView' }">
      <img src="@/assets/writing-icon.png" alt="" class="writing-icon">
      지금 글쓰러 가기
    </RouterLink>
  </div>
  <article class="article">
    <h3>글 목록</h3>
    <ArticleListItem v-for="article in displayedPosts" :key="article.id" :article="article" />
  </article>
  <div class="article-btn">
    <button @click="prevPage" class="page-button">
      <img src="@/assets/left-arrow.png" alt=""> </button>
    <span>{{ currentPage }} / {{ totalPages }}</span>
    <button @click="nextPage" class="page-button">
      <img src="@/assets/right-arrow.png" alt=""> </button>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import { useCommunityStore } from '@/stores/community'
import { useRoute, useRouter } from 'vue-router'
import ArticleListItem from '@/components/community/ArticleListItem.vue'
import Cateogry from '@/components/community/Category.vue'

const route = useRoute()
const router = useRouter()
const store = useCommunityStore()
const currentPage = ref(parseInt(route.query.page) || 1)
const postsPerPage = 15 // 한 페이지에 보여줄 개수

watch(route, () => {
  currentPage.value = parseInt(route.query.page) || 1
})

const totalPages = computed(() => {
  return Math.ceil(store.articles.length / postsPerPage)
})

const displayedPosts = computed(() => {
  const startIndex = (currentPage.value - 1) * postsPerPage
  const endIndex = startIndex + postsPerPage
  return store.articles.slice(startIndex, endIndex)
})

const nextPage = () => {
  router.push({ query: { ...route.query, page: currentPage.value + 1 } })
}

const prevPage = () => {
  router.push({ query: { ...route.query, page: currentPage.value - 1 } })
}

onMounted(() => {
  store.getArticles()
})

console.log(store.articles)

</script>

<style scoped>
.create-link {
  text-align: left;
  margin-left: 50px;
  margin-bottom: 70px;
}

.create-link a {
  color: black;
  /* 글자 색을 검은색으로 변경 */
  text-decoration: none;
  /* 밑줄을 제거 */
  font-size: 25px;
  padding: 10px 20px;
  transition: color 0.3s, transform 0.3s;
}

.create-link a:hover {
  color: rgba(0, 0, 0, 0.7);
  /* 색상을 조금 연하게 변경 */
  transform: translateY(-20px);
  /* 위로 살짝 이동 */
}

.writing-icon {
  width: 50px;
  height: 50px;
  margin-right: 20px;
  transition: transform 0.5s;
}

.create-link a:hover .writing-icon {
  transform: translateY(-20px);
  /* 아이콘도 위로 살짝 이동 */
}

.article>h3 {
  margin-bottom: 40px;
  font-size: 40px;
  text-align: center;

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
