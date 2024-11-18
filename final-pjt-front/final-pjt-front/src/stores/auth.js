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
        router.push({ name: 'HomeView'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(() => {
        // 로그아웃 성공 처리
        token.value = null
        // 로컬 스토리지나 쿠키에 저장된 토큰 제거
        localStorage.removeItem('token')
        // 홈 페이지나 로그인 페이지로 리다이렉트
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { signUp, logIn, logOut, API_URL, token }
},{persist: true}
)
