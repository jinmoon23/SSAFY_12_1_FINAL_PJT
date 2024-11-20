<template>
  <div class="container mt-5">
    <h1>테마 1개와 종목 몇개 나열 되는 페이지</h1>
    <p>{{ theme_name }}</p>
    <div>
      <h2>테마 차트 그래프</h2>
    </div>
    <div>
      <h2>개별 주식 나열, 여기도 국내, 국외 페이지로 나눠서 종목 나열하기</h2>
    </div>
  </div>
</template>

<script setup>
import { useStockStore } from '@/stores/stock'
import { useRoute } from 'vue-router'
const route = useRoute()
const store = useStockStore()
const theme_name = route.params.id
const currentDate = new Date()

store.getStockChart(theme_name)
store.todaydate = `${currentDate.getFullYear()}${currentDate.getMonth()+1}${currentDate.getDate()}`


</script>

<style scoped>

</style>