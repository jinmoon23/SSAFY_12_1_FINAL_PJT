import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAuthStore } from './auth'

export const useUserInterestStore = defineStore('stock', () => {
  const store = useAuthStore()

  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/stock//`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {

    },
  })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })

  return {}
},{persist: true}
)
