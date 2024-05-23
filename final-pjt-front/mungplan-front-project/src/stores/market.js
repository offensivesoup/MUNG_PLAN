import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMarketStore = defineStore('market', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state
  const products = ref([])
  const searchText = ref(null)
  // getters
  const searchProducts = computed(() => {
    if (searchText.value) {
      console.log('입력')
      return products.filter((product) => {
        return product.item_name.includes(searchText.value)
      })
    }
    else { return products.value }
  })

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
  // markets/product/<str:category_name>/
  const productFiltering = function (categoryName) {
    axios({
      method: 'get',
      url: `${API_URL}markets/product/${categoryName}/`,
    })
      .then(response => {
        products.value = response.data
        console.log(products)
      })
      .catch(error => {
        console.log(error)
        getProducts()
      })
  }

  return { API_URL, products, getProducts, productFiltering, searchProducts }
}, { persist: true })