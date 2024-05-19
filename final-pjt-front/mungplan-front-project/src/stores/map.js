import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import Map from '@/views/map/MapView.vue'
import naver from 'vue-naver-maps'

export const useMapStore = defineStore('map', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state
  const places = ref([])
  let count = ref(0)
  // getters

  // actions

  const getPlace = function (word) {
    count.value += 1
    axios({
      method:'GET',
      url:`${API_URL}maps/${word}`
    })
    .then(response => {
      places.value = response.data
      console.log(places.value)
    })
    .catch(error => {
      console.log(error)
    })
  }

  // Map.use(naver, {
  //   clientID: import.meta.env.VUE_APP_CLIENT_ID,
  //   useGovAPI : false,
  //   subModules:'',
  //   })

  return { API_URL, getPlace, places, count }
}, { persist: true })