<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <RouterLink :to="{ name: 'HomeView' }" class="navbar-brand">
          <img src="/landing/logo.png" alt="logo" class="logo" />
        </RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink :to="{ name: 'AdoptView' }" class="nav-link">Life</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'ArticleView' }" class="nav-link">Community</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'DepositView' }" class="nav-link">Finance</RouterLink>
            </li>
          </ul>
        </div>
        <div class="d-flex nav-item dropdown">
          <button class="nav-item image-button" href="#" id="userDropDown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="/landing/userIcon.png" id="user-icon" alt="user icon" />
            Hello, 김승지렁이와두루미!
          </button>
          <ul class="dropdown-menu" aria-labelledby="userDropDown">
            <li><a class="dropdown-item" href="#">Login</a></li>
            <li><a class="dropdown-item" href="#">Signup</a></li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.navbar-brand{
  margin: 0 10% 0 5%;
}
.logo {
  height: 60px; /* 로고 이미지의 높이를 조정합니다. */
  width: auto; /* 너비는 자동으로 설정하여 비율을 유지합니다. */
}
#user-icon{
  width: 20%;
  height: 95%;
  object-fit: contain;
}
.navbar-collapse{
  flex-grow : 0;
}
/* 버튼에 잡히는 크기가 좀 큰데 어떻게 줄이는지 모르겠음 .ㅜ ㅜ ㅜ ㅜ 이미지&텍스트와 딱 맞추고 싶어요 */
.image-button {
  padding: 0px;
  margin: 0px;
  border: none;
  background-color: transparent;
  outline: none;
}
.dropdown-menu {
  position:absolute;
  background-color: white;
  right:0px;
}
</style>