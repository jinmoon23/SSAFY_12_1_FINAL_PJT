<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div class="mb-3">
        <label for="input_id" class="form-label">아이디</label>
        <input type="text" class="form-control" id="input_id" v-model.trim="username">
      </div>
      <div class="mb-3">
        <label for="input_password" class="form-label">비밀번호</label>
        <input type="password" class="form-control" id="input_password" v-model.trim="password">
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { ref } from 'vue'

const store = useAuthStore()
const username = ref(null)
const password = ref(null)

const logIn = function() {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>

</style>