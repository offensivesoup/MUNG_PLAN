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
      url: `${API_URL}adopts/`
    })
      .then(response => {
        console.log(response)
        console.log(response.data)
        shelterDogs.value = response.data
      })
      .catch(error => console.log(error))
  }

  const filteringDogs = function (category) {
    shelterDogs.value = []
    axios({
      method: 'GET',
      url: `${API_URL}adopt/filter/${category}/`
    })
      .then(response => {
        console.log(response.data)
        shelterDogs.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
  return { API_URL, shelterDogs, getShelterDogs, filteringDogs }
}, { persist: true })