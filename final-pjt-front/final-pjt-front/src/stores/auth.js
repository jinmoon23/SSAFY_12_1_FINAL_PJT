import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('auth', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  
  const signUp = function (payload) {
    const {username, password1, password2, email, nickname } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, email, nickname
      }
    })
      .then((res) => {
        console.log(res)
        console.log('회원가입 성공')

        // 회원가입 성공 후 자동 로그인
        const password = password1
        logIn({username, password})
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  const logIn = function (payload) {
    const {username, password} = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        // 로그인 성공하면 다음 페이지로 이동 가능하게,,!
        // router.push({ name: 'View 이름'})
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { signUp, logIn, API_URL, token }
})
