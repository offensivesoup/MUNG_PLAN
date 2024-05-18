import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state
  let articles = ref([])

  // getters

  // actions
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}community/articles/`
    })
      .then(response => {
        articles.value = response.data
        console.log(articles)
      })
      .catch(error => {
        console.log(error)
      })
  }

  const articleFiltering = function (categoryName) {
    axios({
      method: 'get',
      url: `${API_URL}community/articles/${categoryName}`
    })
      .then(response => {
        articles.value = response.data
        console.log(articles)
      })
      .catch(error => {
        console.log(error)
        getArticles()
      })
  }
  return { API_URL, articles, getArticles, articleFiltering }
}, { persist: true })
