import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAuthStore } from './auth'

export const useUserInterestStore = defineStore('interest', () => {
  const store = useAuthStore()
  
  const usermbti = ref(null)
  const userinterest = ref([])
  const userperiod = ref(null)

  const analyze = function () {

    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/stock/analyze/`,
      headers: {
        Authorization: `Token ${store.token}`
      },
      data: {
        mbti: usermbti,
        interest: userinterest,
        period: userperiod,
      },
    })
      .then((res) => {
        console.log(res)
        console.log('분석 요청 전송 완료')
  
        // 응답 데이터 처리
        // 추천 테마 6개 리스트 반환

      })
      .catch((err) => {
        console.log(err)
      })
  }

  return {analyze, usermbti, userinterest, userperiod}
},{persist: true}
)
