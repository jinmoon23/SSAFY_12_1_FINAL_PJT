<template>
  <div class="container mt-5">
    <h1>당신의 추천 테마는 아래와 같습니다!</h1>
    <div v-for="theme in themes">
      <div class="bg-light text-dark">
        <h3 :to="{name: 'ThemeItemView'}">{{ theme.theme_name }}</h3>
        <p>{{ theme.description }}</p>
        <div v-for="stock in theme.stocks">
          <div v-if="checkUsa(stock.code)">
            <p>국내</p>
            <p>{{ stock }}</p>
          </div>
          <div v-else>
            <p>국외</p>
            <p>{{ stock }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserInterestStore } from "@/stores/userinterest"
import { ref } from "vue"

const store = useUserInterestStore()
const themes = store.recommendthemes

const checkUsa = function (stock_code) {
  // false 면 국내(숫자), true 면 국외(문자)
  return isNaN(stock_code)
}

// 테마 클릭하면 그 테마 페이지로 이동할 수 있게 하기


</script>

<style scoped>
</style>