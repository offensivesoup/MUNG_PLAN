<template>
  <div class="container">
    <header>
      <nav ref="navbar" class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
        <div class="container-fluid">
          <RouterLink :to="{ name: 'HomeView' }" class="navbar-brand">
            <img src="/landing/logo.png" alt="logo" class="logo" />
          </RouterLink>

          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav en me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <RouterLink :to="{ name: 'AdoptView' }" class="nav-link">Adopt</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'MapView' }" class="nav-link">Map</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'ArticleView' }" class="nav-link">Community</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'MarketView' }" class="nav-link">Market</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'FinanceSelectView' }" class="nav-link">Finance</RouterLink>
              </li>
            </ul>
          </div>

          <div class="d-flex nav-item dropdown d-none d-lg-block">
            <button class="image-button" href="#" id="userDropDown" role="button" data-bs-toggle="dropdown"
              aria-expanded="false">
              <img v-if="store.state && store.state.profileImg && store.state.profileImg !== ''"
                :src="`${store.API_URL}${store.state.profileImg}`" id="user-icon" class="user" alt="user icon" />
              <img v-else src="/landing/userIcon.png" id="user-icon" class="user" alt="user icon" />
              <span v-if="store.state && store.state.nickname" style="margin-left:8px;">{{ store.state.nickname }}</span>
              <span v-else style="margin-left:8px;">안녕하세요!</span>
            </button>
            <ul class="dropdown-menu" aria-labelledby="userDropDown">
              <li v-if="store.state.isAuthenticated">
                <button @click="store.logOut" class="dropdown-item">Logout</button>
              </li>
              <li v-else>
                <RouterLink :to="{ name: 'LogInView' }" class="dropdown-item">Login</RouterLink>
              </li>
              <li v-if="store.state.isAuthenticated && store.state.username">
                <RouterLink :to="{ name: 'ProfileView', params: { 'username': store.state.username } }"
                  class="dropdown-item">Profile</RouterLink>
              </li>
              <li v-else>
                <RouterLink :to="{ name: 'SignUpView' }" class="dropdown-item">Signup</RouterLink>
              </li>
            </ul>
          </div>

        </div>
      </nav>
    </header>
    <main>
      <RouterView />
    </main>
  </div>
  <footer :class="[{ 'fade-in': canSee }]">
    <div class="inner">
      <div class="footer-message">모두의 아름다운 선택을 위해서</div>
      <div class="footer-message">SSAFY 11기 관통 프로젝트</div>
      <div class="footer-contact">
        김동환 : 깃허브 주소
        이승지 : 깃허브 주소
      </div>
      <div class="footer-copyright">Copyright 2020 All ⓒ rights reserved</div>
      <div class="footer-links">
        <RouterLink :to="{ name: 'AdoptView' }" class="footer-link">Adopt</RouterLink>
        <RouterLink :to="{ name: 'MapView' }" class="footer-link">Map</RouterLink>
        <RouterLink :to="{ name: 'ArticleView' }" class="footer-link">Community</RouterLink>
        <RouterLink :to="{ name: 'MarketView' }" class="footer-link">Market</RouterLink>
        <RouterLink :to="{ name: 'DepositView' }" class="footer-link">Finance</RouterLink>
      </div>
    </div>
  </footer>
</template>

<script setup>

import { useAccountStore } from './stores/account';
import { ref, computed } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { onMounted, onBeforeUnmount } from 'vue'
import HomeView from '@/views/HomeView.vue';
const canSee = ref(false)
const store = useAccountStore()

const username = computed(() => {
  return store.state.isAuthenticated ? store.state.username : '로그인이 필요합니다'
})

// navbar 스크롤 이벤트 - 지금은 border-bottom 추가\
const navbar = ref(null)

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  setTimeout(() => {
    canSee.value = true
  }, 1500)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
})

const handleScroll = () => {
  if (navbar.value) {
    if (window.scrollY > 0) {
      navbar.value.classList.add('border-bottom')
    } else {
      navbar.value.classList.remove('border-bottom')
    }
  }
}

</script>

<style scoped>
.navbar {
  padding: 0 15px;
  max-width: 1800px;
  margin: 0 auto;
}

.navbar.border-bottom {
  border-bottom: 1px solid #ccc;
}

.bg-light {
  background-color: #FFF4E0 !important;
}

.logo {
  height: 100%;
  width: 150px;
}

.nav-item {
  font-size: 1.1rem;
  padding-top: 25px;
}

.nav-item a:hover {
  text-shadow: true;
  color: #000;
  /* 더 진한 색상으로 변경 */
}


#user-icon {
  width: 20%;
  height: 70%;
  object-fit: contain;
}

.navbar-nav {
  padding-left: 70px;
}

.navbar-nav>li {
  padding-left: 30px;
  padding-right: 30px;
}

.navbar-collapse {
  flex-grow: 0;
}

.image-button {
  box-sizing: content-box;
  padding: 0px;
  margin: 0px;
  border: none;
  background-color: transparent;
  outline: none;
  /* 이렇게 하면 버튼사이즈랑 안에 컨텐츠 내용이랑 딱 맞긴 하는데 글자수 제한을 둬야할 듯 아오 */
  width: 200px;
  height: auto;
}

.dropdown-menu {
  position: absolute;
  background-color: white;
  left: 20px;
}

/* footer 관련 */

footer {
  position: relative;
  text-align: center;
  border-top: #bababa 1px solid;
  transform: translateY(-100%);
  background-color: #FFF4E0;
  padding: 1rem 0;
  opacity: 0;
  transition: opacity 2s ease-in-out;
  /* z-index: -1; */
}

.fade-in {
  opacity: 1;
}

.footer-message {
  font-weight: bold;
  font-size: 0.9rem;
  color: #545e6f;
  margin-bottom: 0.3rem;
  margin: 0 0 0 0.6rem;
}

.footer-contact {
  font-size: 0.9rem;
  color: #545e6f;
  margin: 0.6rem;
}

.footer-copyright {
  font-size: 0.9rem;
  color: #545e6f;
  margin: 0.6rem;
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: 10px;
  /* 링크들 사이의 간격을 설정 */
}

.footer-link {
  text-decoration: none;
  color: #000;
  /* 기본 링크 색상 */
  padding: 5px 10px;
  /* 링크에 여백을 추가 */
}</style>