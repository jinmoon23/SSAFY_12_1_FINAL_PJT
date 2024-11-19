import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAuthStore } from './auth'

export const useStockStore = defineStore('stock', () => {
  const store = useAuthStore()

  // 장고에서 받아오는 한국투자증권 토큰
  const requestToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6IjkyMzU0N2ZkLWU2OGUtNGM1Mi05ZDBkLWVlYjBmMGNkMzcyMiIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTczMjA2NjE0MCwiaWF0IjoxNzMxOTc5NzQwLCJqdGkiOiJQU09NTUdqNTdvcHY0c2FEaUJlbFNwOXVzYXI5THRYZnVrbzIifQ.a3bZcX4wBLPwm6mcMAjGzDU7wFTqwJcf7ADAv3cVyIkDSuZNFYRfrM3DyjSpNwRQuU9aJENN5JzE46v8BvunqA'

  const getStockChart = function () {
    axios({
      // 백에서 받아오기
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return {getStockChart}
},{persist: true}
)
