<!--
  what : 입양 정보 제공 view
  use : life nav 누르면 바로 여기로 오도록 (life의 메인 주제니까?)
 -->

<template>
  <article class="select-category">

    <div>
      <p>
        <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseWidthExample"
          aria-expanded="false" aria-controls="collapseWidthExample">
          필터
        </button>
      </p>
    </div>

    <div style="min-height: 120px;">
      <div class="collapse collapse-horizontal" id="collapseWidthExample">
        <div class="btn-group">

          <div class="button1">
            <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
              상태
            </button>
            <ul class="dropdown-menu">
              <li><button class="btn-dropdown" @click="store.filteringDogs('stateEnd')">보호 종료</button></li>
              <li><button class="btn-dropdown" @click="store.filteringDogs('state')">보호 중</button></li>
            </ul>
          </div>

          <div class="button2">
            <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
              성별
            </button>
            <ul class="dropdown-menu">
              <li><button class="btn-dropdown" @click="store.filteringDogs('femail')">여아</button></li>
              <li><button class="btn-dropdown" @click="store.filteringDogs('mail')">남아</button></li>
            </ul>
          </div>

          <div class="button3">
            <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
              중성화
            </button>
            <ul class="dropdown-menu">
              <li><button class="btn-dropdown" @click="store.filteringDogs('finall')">완료</button></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </article>

  <div class="adopt adopt-header">
    <h1>유기견 입양</h1>
  </div>
  <div class="adopt adopt-main">
    <!-- + : 필터 - 나이, 성별, 중성화, 지역, 품종? 너무 많은가 -->
  </div>
  <div class="adopt adopt-count-info">
    <img src="/adopt/brownDog1.png" alt="brown dog icon" style="width: 40px; height: 40px;">
    <h5 style="margin: 0; font-size: 18px;">{{ store.shelterDogs.length }}마리의 아이들이 가족을 기다리고 있어요.</h5>
  </div>

  <AdoptList />
</template>

<script setup>
import { onMounted } from 'vue'
import { useAdoptStore } from '@/stores/adopt'
import AdoptList from '@/components/adopt/AdoptList.vue'

const store = useAdoptStore()

onMounted(() => {
  store.getShelterDogs()
})
</script>

<style scoped>
.adopt-count-info {
  display: flex;
  /* justify-content: flex-start !important; */
  /* 카드 시작점이랑 수직정렬하기 */
  align-items: center;
  margin: 20px 0;
}

.adopt {
  display: flex;
  justify-content: center;
  align-items: center;
}

.btn-group {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 27px;
}

/* .btn-group>button {
  background-color: white;
  border: none;
  color: black;
  text-align: center;
} */

.select-category {
  display: flex;
  justify-content: left;
  align-items: center;
}

.btn-primary {
  opacity: 1;
  background-color: white;
  color: black;
  width: 120px;
  height: 50px;
  margin: 0px 20px;
  border: none;
  transition: opacity 0.2s ease-in;
}

.btn-primary:hover {
  opacity: 0.3;
}

.btn-dropdown {
  opacity: 1;
  background-color: white;
  color: black;
  width: 80px;
  height: 50px;
  margin: 0px 20px;
  border: none;
  transition: opacity 0.2s ease-in;
}

.btn-dropdown:hover {
  opacity: 0.3;
}

.dropdown-menu {
  min-width: 0;
  /* To adjust the width of the dropdown */
}
</style>