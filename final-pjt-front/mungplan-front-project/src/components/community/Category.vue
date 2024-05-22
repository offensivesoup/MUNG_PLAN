<!-- 
  what : life의 nav component
  use : 게시물 보여주는 모든 view에 추가 
-->

<template>
  <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
    <button @click="store.getArticles()" type="button" class="btn btn-secondary">전체</button>
    <button @click="store.articleFiltering('고민나누기')" type="button" class="btn btn-secondary">고민나누기</button>
    <button @click="store.articleFiltering('중고장터')" type="button" class="btn btn-secondary">중고장터</button>
    <button @click="store.articleFiltering('동네사람들')" type="button" class="btn btn-secondary">동네사람들</button>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useCommunityStore } from '@/stores/community'
const store = useCommunityStore()
</script>

<style scoped>
.btn-group {
  display: flex;
  gap: 80px;
  
}
.btn-group > .btn {
  position:relative;
  border:none;
  background-color:transparent;
  color: black;
  text-transform: uppercase;
  height: 50px;
  margin: 50px 0px;
  font-size:25px;
  opacity: 1;
  transition: all 0.5s ease-in-out;
  overflow: hidden;
}

.btn-group > .btn:focus {
  outline:none;
}

.btn-group > .btn::before {
  content:"";
  height: 100%;
  width: 100%;
  position: absolute;
  background-color:#FFBF9B;
  /* color:white; */
  top:100%;
  left:0;
  transition: all 0.4s;
  z-index: -1;
}

.btn-group > .btn:hover::before {
  transform : translateY(-100%);
}

.btn-group > .btn:hover {
  color:#B46060;
}

</style>