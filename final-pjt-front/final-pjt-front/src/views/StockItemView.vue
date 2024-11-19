<template>
  <div>
    <h1>종목 차트 실시간으로 그리는 페이지</h1>
  </div>
    <!-- 입력 코드가 국내면 -->
    <!-- <DomesticStockChart/> -->
    <!-- 입력 코드가 해외면 -->
    <UsaStockChart/>
</template>

<script setup>
import DomesticStockChart from '@/components/stocks/DomesticStockChart.vue'
import UsaStockChart from '@/components/stocks/UsaStockChart.vue'


</script>

<style scoped>

</style>