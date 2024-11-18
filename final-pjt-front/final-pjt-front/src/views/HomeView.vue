<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'LogInView'}">로그인</RouterLink>
      |
      <RouterLink :to="{name: 'SignUpView'}">회원가입</RouterLink>
    </nav>
    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>

<style scoped>

</style>