<template>
  <h1>MBTI를 선택해주세요!</h1>
  <div>
    <div class="btn-group mb-3" role="group" aria-label="EI Group">
      <input type="radio" class="btn-check" id="E" autocomplete="off" v-model="selectedEI" value="E">
      <label class="btn btn-outline-primary" :class="{ active: selectedEI === 'E' }" for="E">외향형(E)</label>
      <input type="radio" class="btn-check" id="I" autocomplete="off" v-model="selectedEI" value="I">
      <label class="btn btn-outline-primary" :class="{ active: selectedEI === 'I' }" for="I">내향형(I)</label>
    </div>
    <div class="btn-group mb-3" role="group" aria-label="SN Group">
      <input type="radio" class="btn-check" id="S" autocomplete="off" v-model="selectedSN" value="S">
      <label class="btn btn-outline-primary" :class="{ active: selectedSN === 'S' }" for="S">감각형(S)</label>
      <input type="radio" class="btn-check" id="N" autocomplete="off" v-model="selectedSN" value="N">
      <label class="btn btn-outline-primary" :class="{ active: selectedSN === 'N' }" for="N">직관형(N)</label>
    </div>
    <div class="btn-group mb-3" role="group" aria-label="TF Group">
      <input type="radio" class="btn-check" id="T" autocomplete="off" v-model="selectedTF" value="T">
      <label class="btn btn-outline-primary" :class="{ active: selectedTF === 'T' }" for="T">판단형(T)</label>
      <input type="radio" class="btn-check" id="F" autocomplete="off" v-model="selectedTF" value="F">
      <label class="btn btn-outline-primary" :class="{ active: selectedTF === 'F' }" for="F">공감형(F)</label>
    </div>
    <div class="btn-group mb-3" role="group" aria-label="JP Group">
      <input type="radio" class="btn-check" id="J" autocomplete="off" v-model="selectedJP" value="J">
      <label class="btn btn-outline-primary" :class="{ active: selectedJP === 'J' }" for="J">계획형(J)</label>
      <input type="radio" class="btn-check" id="P" autocomplete="off" v-model="selectedJP" value="P">
      <label class="btn btn-outline-primary" :class="{ active: selectedJP === 'P' }" for="P">즉흥형(P)</label>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useUserInterestStore } from '@/stores/userinterest'

const selectedEI = ref(null)
const selectedSN = ref(null)
const selectedTF = ref(null)
const selectedJP = ref(null)

const store = useUserInterestStore()

// watch로 mbti 선택할 때 마다 값 바뀌게 설정
watch([selectedEI, selectedSN, selectedTF, selectedJP], ([newEI, newSN, newTF, newJP]) => 
  {if (newEI && newSN && newTF && newJP) {store.usermbti = `${newEI}${newSN}${newTF}${newJP}`;}}, 
  { immediate: true })

</script>

<style scoped>

</style>