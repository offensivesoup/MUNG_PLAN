import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const API_URL = 'http://127.0.0.1:8000'

  // state
  const articles = ref([])
  
  // getters

  // actions
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
  return { API_URL, articles, getArticles }
}, { persist: true })
