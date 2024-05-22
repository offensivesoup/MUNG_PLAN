import { ref, computed, reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000/'
  const token = ref(null)

  const state = reactive({
    id: null,
    username: null,
    nickname: null,
    // profileImg: null,
    dogs: [],
    articles: [],
    isAuthenticated: false
  })

  const router = useRouter()

  const signUp = async (payload) => {
    const { username, password1, password2, nickname, phoneNumber, address, birthDate, firstName, lastName } = payload;

    try {
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password1', password1);
      formData.append('password2', password2);
      formData.append('nickname', nickname);
      formData.append('phone_number', phoneNumber);
      formData.append('address', address);
      formData.append('birth_date', birthDate);
      formData.append('first_name', firstName);
      formData.append('last_name', lastName);

      const response = await axios({
        method: 'post',
        url: `${API_URL}auth/registration/`,
        data: formData,
      });

      console.log('회원가입 성공!', response.data);
      const password = password1;
      logIn({ username, password });

    } catch (error) {
      console.error('회원가입 실패:', error.response ? error.response.data : error.message);
      console.log(payload);
    }
  };

  const logIn = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload

    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}auth/login/`,
      data: { username, password }
    })
      .then((response) => {
        // console.log(response)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
        state.isAuthenticated = true
        // state.username = username
        // console.log(state)

        // 4. 토큰을 사용하여 사용자 정보를 가져옴
        axios({
          method: 'get',
          url: `${API_URL}accounts/userinfo/`,
          headers: {
            'Authorization': `Token ${token.value}`
          }
        })
          .then((response) => {
            console.log(response)
            state.id = response.data.id
            state.username = response.data.username
            state.nickname = response.data.nickname
            state.profileImg = response.data.profile_img
            state.dogs = response.data.dogs
            state.articles = response.data.articles

            // 사용자 정보가 state 객체에 성공적으로 저장된 후에 홈 뷰로 이동
            router.push({ name: 'HomeView' })
          })
          .catch((error) => {
            console.error('사용자 정보 가져오기 실패:', error.response ? error.response.data : error.message);
          })
      })
  }

  const logOut = () => {
    state.id = null
    state.username = null
    state.nickname = null
    state.profileImg = null
    state.isAuthenticated = false
    token.value = null

    // Clear browser storage
    localStorage.clear()
    sessionStorage.clear()

    // Clear axios cache
    axios.defaults.headers = {}
    
    axios({
      method: 'POST',
      url: `${API_URL}auth/logout/`
    })
      .then(response => {
        console.log('로그아웃 성공')
        router.push({ name: 'HomeView' })
      })
      .catch(error => {
        console.log(error)
      })
  }

  const userDetail = (username) => {
    return new Promise((resolve, reject) => {
      axios({
        method: 'GET',
        url: `${API_URL}accounts/detail/${username}/`
      })
        .then(response => {
          // console.log(response.data)
          resolve(response.data)
        })
        .catch(error => {
          reject(error)
        })
    })
  }

  return { API_URL, signUp, logIn, logOut, token, state, userDetail }
}, { persist: true })
