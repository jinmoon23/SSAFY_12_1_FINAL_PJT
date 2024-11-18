<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'HomeView'}">Home</RouterLink>
      |
      <RouterLink v-if="!isLoggedIn" :to="{name: 'LogInView'}">로그인</RouterLink>
      |
      <RouterLink v-if="!isLoggedIn" :to="{name: 'SignUpView'}">회원가입</RouterLink>
      |
      <button v-if="isLoggedIn" @click="logOut">로그아웃</button>
    </nav>
    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from './stores/auth'
import { computed } from 'vue'

const store = useAuthStore()
const isLoggedIn = computed (() => store.isAuthenticated)

const logOut = function () {
  store.logOut()
}

</script>

<style scoped>

</style>