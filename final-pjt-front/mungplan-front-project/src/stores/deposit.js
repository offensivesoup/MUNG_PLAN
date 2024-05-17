import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useDepositStore = defineStore('adopt', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state
  const deposits = ref([])

  // getters

  // actions
  const getDeposits = function () {
    axios({
      method: 'get',
      // url: `${API_URL}/`
    })
      .then(res => {
        deposits.value = res.data
      })
      .catch(err => console.log(err))
  }

  return { API_URL, deposits, getDeposits }
}, { persist: true })
