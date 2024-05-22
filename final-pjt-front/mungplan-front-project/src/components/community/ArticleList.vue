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
      <ArticleListItem v-for="article in store.articles" :key="article.id" :article="article" />
  </article>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCommunityStore } from '@/stores/community'
import ArticleListItem from '@/components/community/ArticleListItem.vue'
import Cateogry from '@/components/community/Category.vue'
const store = useCommunityStore()

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
  color: black; /* 글자 색을 검은색으로 변경 */
  text-decoration: none; /* 밑줄을 제거 */
  font-size:25px;
  padding: 10px 20px;
  transition: color 0.3s, transform 0.3s;
}

.create-link a:hover {
  color: rgba(0, 0, 0, 0.7); /* 색상을 조금 연하게 변경 */
  transform: translateY(-20px); /* 위로 살짝 이동 */
}

.writing-icon {
  width:50px;
  height: 50px;
  margin-right:20px;
  transition: transform 0.5s;
}

.create-link a:hover .writing-icon {
  transform: translateY(-20px); /* 아이콘도 위로 살짝 이동 */
}

.article > h3{
  margin-bottom: 40px;
  font-size: 40px;
  text-align: center;

}
</style>
