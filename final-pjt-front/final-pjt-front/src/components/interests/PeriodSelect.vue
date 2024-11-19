<template>
  <div class="container mt-5">
    <h3>투자 기간을 선택하세요</h3>
    <div class="slider-container">
      <!-- 슬라이더 -->
      <input 
        type="range" 
        class="form-range" 
        min="1" 
        max="12" 
        step="1" 
        v-model="investmentDuration" 
        @input="updateDurationLabel"
      />
      <!-- 선택된 투자 기간 표시 -->
      <p>선택된 투자 기간: {{ durationLabel }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useUserInterestStore } from '@/stores/userinterst'

// 슬라이더 값 (1~12개월)
const investmentDuration = ref(1)

// 투자 기간 라벨 업데이트 함수
const durationLabel = ref('1달')

// 백엔드로 보낼 ENUM 값
const period = ref(null)
const store = useUserInterestStore()

const updateDurationLabel = () => {
  if (investmentDuration.value >= 12) {
    period.value = '장기'
    durationLabel.value = '1년 이상'
  } else {
    durationLabel.value = `${investmentDuration.value}달`
    if (investmentDuration.value <= 3) {
      period.value = '단기'
    } else {
      period.value = '중기'
    }
  }
}

watch(period, (newPeriod) => {
  store.userperiod = newPeriod // 스토어에 최종 관심사 매핑 값 저장
}, { immediate:true })

</script>

<style scoped>
/* 슬라이더 스타일 */
.slider-container {
  margin-top: 20px;
}

.form-range {
  width: 100%;
}
</style>