import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAdoptStore = defineStore('adopt', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state
  const shelterDogs = ref([
    // id, img, state, kind, age??, gender, notice, center_address ...
  ])

  // getters

  // actions
  const getShelterDogs = function () {
    axios({
      method: 'get',
      // url: `${API_URL}/`
    })
      .then(res => {
        shelterDogs.value = res.data
      })
      .catch(err => console.log(err))
  }

  return { API_URL, shelterDogs, getShelterDogs }
}, { persist: true })
