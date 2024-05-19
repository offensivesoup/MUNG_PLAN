import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useDepositStore = defineStore('deposit', () => {
  const API_URL = 'http://127.0.0.1:8000/'

  // state
  const deposits = ref([])
  const staticUrl = ref('')  // staticUrl 선언

  // getters

  // actions
  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}finance/deposits/`
    })
      .then(res => {
        deposits.value = res.data.deposits  // deposits 데이터 설정
        staticUrl.value = res.data.static_url.substring(1)  // staticUrl 데이터 설정
      })
      .catch(err => console.log(err))
  }

  return { API_URL, deposits, staticUrl, getDeposits }
}, { persist: true })
