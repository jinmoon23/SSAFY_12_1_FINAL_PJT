<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'HomeView'}">Home</RouterLink>
      |
      <RouterLink :to="{name: 'LogInView'}">로그인</RouterLink>
      |
      <RouterLink :to="{name: 'SignUpView'}">회원가입</RouterLink>
      |
      <button @click="logOut">로그아웃</button>
    </nav>
    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from './stores/auth'

const store = useAuthStore()

const logOut = function () {
  store.logOut()
}

</script>

<style scoped>

</style>