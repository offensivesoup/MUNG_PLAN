<template>
  <article :class="['intro', { 'fade-out': visible }]">
    <img src="@/assets/adopt-intro.png" alt="">
  </article>

  <article :class="['content', { 'fade-in': visible }]">
    <div class="adopt adopt-header">
      <h1 style="font-size: 3.2rem; padding-top: 12px;">유기견 입양</h1>
    </div>
    <div class="adopt adopt-main">
      <!-- + : 필터 - 나이, 성별, 중성화, 지역, 품종? 너무 많은가 -->
    </div>
    <div class="adopt adopt-count-info">
      <img src="/adopt/brownDog1.png" alt="brown dog icon" style="width: 40px; height: 40px;">
      <h5 style="margin: 0; font-size: 18px;">{{ store.shelterDogs.length }}마리의 아이들이 가족을 기다리고 있어요.</h5>
    </div>

    <article class="select-category">

      <div>
        <p>
          <button class="filter-btn" type="button" data-bs-toggle="collapse" data-bs-target="#collapseWidthExample"
            aria-expanded="false" aria-controls="collapseWidthExample">
            필터
          </button>
        </p>
      </div>

      <div style="min-height: 120px;">
        <div class="collapse collapse-horizontal" id="collapseWidthExample">
          <div class="btn-group">

            <div class="button1">
              <button type="button" class="filter-btn dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                상태
              </button>
              <ul class="dropdown-menu">
                <li><button class="btn-dropdown" @click="store.filteringDogs('stateEnd')">보호 종료</button></li>
                <li><button class="btn-dropdown" @click="store.filteringDogs('state')">보호 중</button></li>
              </ul>
            </div>

            <div class="button2">
              <button type="button" class="filter-btn dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                성별
              </button>
              <ul class="dropdown-menu">
                <li><button class="btn-dropdown" @click="store.filteringDogs('femail')">여아</button></li>
                <li><button class="btn-dropdown" @click="store.filteringDogs('mail')">남아</button></li>
              </ul>
            </div>

            <div class="button3">
              <button type="button" class="filter-btn dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
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
    <AdoptList />
  </article>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAdoptStore } from '@/stores/adopt'
import AdoptList from '@/components/adopt/AdoptList.vue'

const visible = ref(false)
const store = useAdoptStore()

onMounted(() => {
  store.getShelterDogs()
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
  z-index: -1;
}

.content {
  opacity: 0;
}

.fade-in {
  opacity: 1;
  transition: opacity 2s ease-in-out;
}

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
  /* margin-top: 27px; */
  margin-bottom: 16px;
  gap: 20px;
}


.select-category {
  display: flex;
  justify-content: left;
  align-items: center;
  margin-left: 250px;
}

.btn-dropdown {
  opacity: 1;
  background-color: #FFBF9B;
  color: black;
  width: 70px;
  height: 50px;
  margin: 0px 20px;
  border: none;
  transition: color 0.2s ease-in;
}

.btn-dropdown:hover {
  color: white;
}

.dropdown-menu {
  background-color: #FFBF9B;
  min-width: 0;
  width: 140px;
  text-align: center;
  /* To adjust the width of the dropdown */
}

.filter-btn {
  position: relative;
  border: none;
  background-color: transparent;
  color: black;
  text-transform: uppercase;
  width: 140px;
  height: 60px;
  margin: 50px 0px;
  font-size: 25px;
  opacity: 1;
  transition: all 0.5s ease-in-out;
  overflow: hidden;
  margin-right: 40px;
  font-size: 25px;
  border-radius: 10%;
}

.filter-btn:focus {
  outline: none;
}

.filter-btn::before {
  content: "";
  height: 100%;
  width: 100%;
  position: absolute;
  background-color: rgb(255, 191, 155);
  /* color:white; */
  top: 100%;
  left: 0;
  transition: all 0.4s;
  z-index: -1;
}

.filter-btn:hover::before {
  transform: translateY(-100%);
}

.filter-btn:hover {
  color: #ffffff;
}
</style>