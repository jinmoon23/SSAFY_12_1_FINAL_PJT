<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">주주님이 궁금해요!</h1>

    <!-- 3등분 레이아웃 -->
    <div class="row">
      <!-- MBTI 선택 -->
      <div class="col-md-4">
        <MbtiSelect />
      </div>

      <!-- 관심 분야 선택 -->
      <div class="col-md-4">
        <InterestSelect />
      </div>

      <!-- 투자 기간 선택 -->
      <div class="col-md-4">
        <PeriodSelect />
      </div>
    </div>

    <!-- 추천 테마 확인 버튼 -->
    <div class="text-center mt-4">
      <button class="btn btn-primary" @click="sendUserData">추천 테마 확인</button>
    </div>
  </div>
</template>

<script setup>
import MbtiSelect from '@/components/interests/MbtiSelect.vue'
import InterestSelect from '@/components/interests/InterestSelect.vue'
import PeriodSelect from '@/components/interests/PeriodSelect.vue'

import { useUserInterestStore } from '@/stores/userinterst'
const store = useUserInterestStore()

const sendUserData = function () {
  store.analyze()
}

</script>

<style scoped>
/* 추가적인 스타일이 필요하다면 여기에 작성 */
</style>