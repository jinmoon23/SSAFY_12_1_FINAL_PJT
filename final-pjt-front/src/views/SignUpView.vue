<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div class="mb-3">
        <label for="input_id" class="form-label">아이디</label>
        <input type="text" class="form-control" id="input_id" v-model.trim="username">
      </div>
      <div class="mb-3">
        <label for="input_password1" class="form-label">비밀번호</label>
        <input type="password" class="form-control" id="input_password1" v-model.trim="password1">
      </div>
      <div class="mb-3">
        <label for="input_password2" class="form-label">비밀번호 확인</label>
        <input type="password" class="form-control" id="input_password2" v-model.trim="password2">
      </div>
      <div>
        <label for="input_email" class="form-label">이메일</label>
        <input type="email" class="form-control" id="input_email" v-model.trim="email">
      </div>
      <div class="mb-3">
        <label for="input_nickname" class="form-label">닉네임</label>
        <input type="text" class="form-control" id="input_nickname" v-model.trim="nickname">
      </div>
      <button type="submit" class="btn btn-primary">가입하기</button>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { ref } from 'vue'

const store = useAuthStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const nickname = ref(null)

const signUp = function () {
  const payload =  {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    nickname: nickname.value
  }
  store.signUp(payload)
}

</script>

<style scoped>

</style>