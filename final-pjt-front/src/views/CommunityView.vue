<template>
  <div class="container mt-5">
    <h1>커뮤니티 웰컴 ~~!</h1>
    <div v-for="article in store.articles">
      <p>{{ article }}</p>
    </div>
  </div>
</template>

<script setup>
import { useUserInterestStore } from '@/stores/userinterest'

const store = useUserInterestStore


getStockInfo
</script>

<style scoped>

</style>