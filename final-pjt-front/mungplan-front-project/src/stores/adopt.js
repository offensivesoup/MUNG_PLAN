import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAdoptStore = defineStore('adopt', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state
  const shelterDogs = ref([])

  // getters

  // actions
  const getShelterDogs = function () {
    axios({
      method: 'get',
      url: `${API_URL}/life/adopts/`
    })
      .then(response => {
        console.log(response)
        shelterDogs.value = response.data
      })
      .catch(error => console.log(error))
  }

  return { API_URL, shelterDogs, getShelterDogs }
}, { persist: true })