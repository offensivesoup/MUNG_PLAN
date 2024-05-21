<template>
  <div>
    <!-- 첫번째 줄 -->
    <div class="row row-first text-white">
      <div class="row-first-image col-md-6">
        <img :src="`${store.API_URL}${profile}`" alt="프로필이미지">
      </div>
      <div class="row-first-info col-md-6">
        <h1 style="font-size: 3em; letter-spacing: 0.2em;">Welcome to '{{ nickName }}'</h1>
        <span>
          <p style="display: inline;">Followers: {{ followersCount }}</p>
          &nbsp; / &nbsp;
          <p style="display: inline-block;">Following: {{ followingsCount }}</p>
        </span>
        <button class="btn follow-btn btn-primary">Follow</button>
      </div>
    </div>

    <!-- 두번째 줄 -->
    <div class="row row-second">
      <div class="row-second-info col-md-6">
        <h3 style="margin-left: 5px;">USER INFO</h3>
        <div class="info-details">
          <div>
            <h5> <img src="/profile/star.png" alt="star emoji"> &nbsp; NAME: {{ nickName }}</h5>
            <h5> <img src="/profile/happy.png" alt="happy emoji">  &nbsp; BIRTHDATE: {{ birthDate }}</h5>
            <h5> <img src="/profile/location.png" alt="location emoji">  &nbsp; ADDRESS: {{ address }}</h5>
          </div>
        </div>
      </div>
      <div class="row-second-dogs col-md-6 overflow-auto">
        <h3 style="margin-left:25px;">DOG INFO</h3>
        <div v-if="dogs.length > 0" class="dogs-details" >
          <div class="row-second-image col-md-6">
            <img :src="`${store.API_URL.slice(0,-1)}${dog_img}`" alt="강아지 프로필 이미지">
          </div>
          <div class="row-second-info col-md-6">
            <h5> NAME: {{ dogs[0].name }}</h5>
            <h5> BREED: {{ dogs[0].breed }}</h5>
            <h5> AGE: {{ dogs[0].age }}</h5>
            <h5> GENDER: {{ dogs[0].gender }}</h5>
          </div>
        </div>
        <!-- 여기 별로.. 좀 바꿔야 할 듯 -->
        <div v-else class="dogs-details row-second-no-dog">
          <div class="adopt-page">
            <img src="/profile/adopt_page.png" alt="adopt page" style="width: 90%;">
          </div>
          <RouterLink :to="{ name: 'AdoptView' }" class="btn adopt-btn btn-primary">지금 만나러 가기!</RouterLink>
        </div>
      </div>
    </div>

    <!-- 세번째 줄 -->
    <div class="row row-third">
      <div class="row-third-article col-md-6">
        <h3 style="margin-left: 5px;">USER'S COMMUNITY</h3>
        <div class="article-table">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Title</th>
                <th scope="col">Category</th>
                <th scope="col">Post date</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(article, index) in articles.slice(0, 3)" :key="article.id">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ article.title }}</td>
                <td>{{ article.category }}</td>
                <td>{{ new Date(article.created_at).toLocaleDateString() }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/account'
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { watch } from 'vue'

const $route = useRoute()
const store = useAccountStore()

const loading = ref(false)
const username = ref('')
const birthDate = ref('')
const nickName = ref('')
const phone_number = ref('')
const address = ref('')
const profile = ref('')

const followersCount = ref(0)
const followingsCount = ref(0)

const dogs = ref([])
const articles = ref([])
const likeDeposits = ref([])

onMounted(async () => {
  await fetchUserDetail()
})

watch(() => $route.params.username, async () => {
  await fetchUserDetail()
})

async function fetchUserDetail() {
  try {
    loading.value = true
    const userData = await store.userDetail($route.params.username)
    console.log(userData)
    username.value = userData.username
    birthDate.value = userData.birth_date
    nickName.value = userData.nickname
    phone_number.value = userData.phone_number
    address.value = userData.address
    profile.value = userData.profile_img.substring(1)

    followersCount.value = userData.followers_count
    followingsCount.value = userData.following_count

    dogs.value = userData.dogs
    articles.value = userData.articles
    likeDeposits.value = userData.like_deposits
  } catch (error) {
    console.log(error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.row {
  margin-bottom: 50px; /* row 클래스 간의 간격을 20px로 설정합니다. */
}
.row-first {
  display: flex;
  align-items: center;
  background-color: #4d4d4dfd;
  border-radius: 20px;
  height: 250px;
}
.row-first-info, .row-first-image {
  flex: 1; /* flex 속성을 사용하여 요소의 크기를 조절합니다. */
  margin: 0 10px; /* margin을 조절하여 요소의 위치를 조절합니다. */
  display: flex; /* flexbox 모델을 사용합니다. */
}
.row-first-info {
  flex: 6; /* row-first-first 요소가 row-first의 70%를 차지하도록 합니다. */
  flex-direction: column;
  justify-content: left;
}

.row-first-image {
  flex: 5; /* row-first-imagea 요소가 row-first의 30%를 차지하도록 합니다. */
  display: flex; /* flexbox 모델을 사용합니다. */
  justify-content: center; /* 가로 방향으로 중앙에 위치하도록 합니다. */
  align-items: center; /* 세로 방향으로 중앙에 위치하도록 합니다. */

}
.row-first-image img {
  width: auto; /* 이미지의 가로 크기를 조절합니다. */
  height: 200px; /* 이미지의 세로 크기를 원본 비율에 맞게 조절합니다. */
}
.follow-btn {
  width: 100px;
  height: 40px;
}

.row-second {
  display: flex;
  align-items: center;
  height: 350px;
  margin-bottom: 80px;
}
.info-details, .dogs-details {
  display: flex;
  align-items: center;
  background-color: #F7CCAC;
  border-radius: 20px;
  height: 350px;
  flex: 1; /* info-details와 row-second-dogs 요소가 row-second의 너비를 균등하게 차지하도록 합니다. */
}

.info-details {
  margin-right: 20px; /* 오른쪽에 20px의 공백을 추가합니다. */
  flex-direction: column;
  justify-content: center; /* 가로 방향으로 중앙에 위치하도록 합니다. */
}

h5 > img {
  width: 50px;
  height: auto;
  margin: 10px;
}
.dogs-details {
  margin-left: 20px;
  flex: 1; /* flex 속성을 사용하여 요소의 크기를 조절합니다. */
  margin: 0 10px; /* margin을 조절하여 요소의 위치를 조절합니다. */
  display: flex; /* flexbox 모델을 사용합니다. */
}
.row-second-info {
  flex: 5; /* row-first-first 요소가 row-first의 70%를 차지하도록 합니다. */
  flex-direction: column;
  justify-content: left;
}

.row-second-image {
  flex: 5; /* row-first-imagea 요소가 row-first의 30%를 차지하도록 합니다. */
  display: flex; /* flexbox 모델을 사용합니다. */
  justify-content: center; /* 가로 방향으로 중앙에 위치하도록 합니다. */
  align-items: center; /* 세로 방향으로 중앙에 위치하도록 합니다. */

}
.row-second-info > h5 {
  margin: 20px;
}
.row-second-image img {
  width: auto; /* 이미지의 가로 크기를 조절합니다. */
  height: 200px; /* 이미지의 세로 크기를 원본 비율에 맞게 조절합니다. */
}
.row-second-no-dog{
  display: flex;
  flex-direction: column;
}
.adopt-page {
  display: flex; /* 이 부분을 추가하세요. */
  justify-content: center; /* 가로 방향으로 중앙에 위치하도록 합니다. */
  align-items: center; /* 세로 방향으로 중앙에 위치하도록 합니다. */
  margin-top: 20px;
  margin-bottom: 10px;
}
.adopt-btn {
  width: 140px;
  height: 40px;
}

.row-third {
  display: flex;
  align-items: center;
  height: 350px;
  margin-bottom: 80px;
}
.article-table{
  margin-right: 20px; /* 오른쪽에 20px의 공백을 추가합니다. */
}
.article-table, .dogs-details {
  display: flex;
  justify-content: center; /* 가로 방향으로 중앙에 위치하도록 합니다. */
  align-items: center;
  background-color: #F7CCAC;
  border-radius: 20px;
  height: 350px;
  flex: 1; /* info-details와 row-third-dogs 요소가 row-third의 너비를 균등하게 차지하도록 합니다. */
}
.table{
  width: 80%;
  --bs-table-bg: #F7CCAC;
  --bs-table-border-color: black;
}

</style>
