import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import Map from '@/views/map/MapView.vue'
import naver from 'vue-naver-maps'

export const useMapStore = defineStore('map', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state

  // getters

  // actions

  Map.use(naver, {
    clientID: import.meta.env.VUE_APP_CLIENT_ID,
    useGovAPI : false,
    subModules:'',
    })

  return { API_URL }
}, { persist: true })