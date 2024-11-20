<template>
  <div class="container mt-5">
    <h1>테마 1개와 종목 몇개 나열 되는 페이지</h1>
    <p>{{ theme_name }}</p>
    <div>
      <!-- 테마 그래프 작성 -->
      <h2>테마 차트 그래프</h2>
      <ThemeChart/>
    </div>
    <div>
      <!-- 각 테마의 주식 종목 나열 -->
      <ThemeStockList/>
    </div>
  </div>
</template>

<script setup>
import { useStockStore } from '@/stores/stock'
import { useRoute } from 'vue-router'
import ThemeChart from '@/components/stocks/ThemeChart.vue'
import ThemeStockList from '@/components/stocks/ThemeStockList.vue'
import { onMounted } from 'vue';

// axios post 요청 변수

const route = useRoute()
const store = useStockStore()
const theme_name = route.params.id
const currentDate = new Date()

onMounted(() => {
  store.todaydate = `${currentDate.getFullYear()}${currentDate.getMonth()+1}${currentDate.getDate()}`
  store.getStockChart(theme_name)
})


</script>

<style scoped>

</style>