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
                <RouterLink :to="{ name: 'DepositView' }" class="nav-link">Finance</RouterLink>
              </li>
            </ul>
          </div>

          <!-- 여기. 사이즈가 안 맞아.. 이상해.. 반응형도 더 넣어야할 듯 ㅜㅜ -->
          <div class="d-flex nav-item dropdown d-none d-lg-block">
            <button class="image-button" href="#" id="userDropDown" role="button" data-bs-toggle="dropdown"
              aria-expanded="false">
              <img src="/landing/userIcon.png" id="user-icon" class="user" alt="user icon" />
              {{ username }}
            </button>
            <ul class="dropdown-menu" aria-labelledby="userDropDown">
              <li v-if="store.state.isAuthenticated">
                <button @click="store.logOut" class="dropdown-item">Logout</button>
              </li>
              <li v-else>
                <RouterLink :to="{ name: 'LogInView' }" class="dropdown-item">Login</RouterLink>
              </li>
              <li v-if="store.state.isAuthenticated">
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

    <RouterView />
  </div>
</template>

<script setup>

import { useAccountStore } from './stores/account';
import { ref, computed } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { onMounted, onBeforeUnmount } from 'vue'

const store = useAccountStore()

const username = computed(() => {
  return store.state.isAuthenticated ? store.state.username : '로그인이 필요합니다'
})

// navbar 스크롤 이벤트 - 지금은 border-bottom 추가\
const navbar = ref(null)

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
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
  max-width: 1700px;
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
}


#user-icon {
  width: 20%;
  height: 70%;
  object-fit: contain;
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
  right: 100px;
}
</style>