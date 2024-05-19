import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMarketStore = defineStore('market', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state
  const products = ref([])

  // getters

  // actions
  const getProducts = function () {
    axios({
      method: 'get',
      url: `${API_URL}markets/`
    })
      .then(response => {
        products.value = response.data
      })
      .catch(error => console.log(error))
  }

  return { API_URL, products, getProducts }
}, { persist: true })