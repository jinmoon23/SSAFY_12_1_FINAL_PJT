<template>
  <div>
    <h3>관심 있는 카테고리를 최소 3개 선택하세요!</h3>
    <div class="row">
      <!-- 카테고리 리스트 -->
      <div class="col-6 col-md-4 mb-3" v-for="category in categories" :key="category.value">
        <button
          class="btn btn-outline-primary category-btn w-100"
          :class="{ active: selectedCategories.includes(category) }"
          @click="toggleCategory(category)"
        >
          {{ category.label }}
        </button>
      </div>
    </div>

    <!-- 선택된 카테고리 표시 및 제한 -->
    <div class="mt-4">
      <p v-if="selectedCategories.length < 3" class="text-danger">최소 3개의 카테고리를 선택해야 합니다.</p>
    </div>

    <!-- 다음 단계로 진행 버튼 (최소 3개 선택 시 활성화) -->
    <!-- <button
      class="btn btn-success mt-3"
      :disabled="selectedCategories.length < 3"
      @click="proceed"
    >
      다음 단계로 진행
    </button> -->
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useUserInterestStore } from '@/stores/userinterest'

// 카테고리 리스트 정의
const categories = ref([
  { label: '쇼핑/유통', value: 'shopping', mapping: ['리테일/유통', '언택트 경제', '플랫폼 대표주자'] },
  { label: '패션/뷰티', value: 'fashion', mapping: ['어디 옷이야?', '뷰티의 세계', '럭셔리'] },
  { label: '식음료', value: 'food', mapping: ['갈증 해소', '프랜차이즈'] },
  { label: '반려동물', value: 'pet', mapping: ['반려동물'] },
  { label: '건설', value: 'construct', mapping: ['건물주의 꿈'] },
  { label: '게임', value: 'game', mapping: ['게임월드', '메타버스구현'] },
  { label: '미디어/컨텐츠', value: 'media', mapping: ['컨텐츠 강자', '스트리밍의 시대'] },
  { label: '여행', value: 'travel', mapping: ['이번 휴가는 어디?'] },
  { label: 'IT', value: 'it', mapping: ['인공지능(AI)', '스트리밍의 시대', '플랫폼 대표주자'] },
  { label: '전기차', value: 'ev', mapping: ['리튬 & 배터리', '자율주행차'] },
  { label: '반도체', value: 'semiconductor', mapping: ['반도체', '소재/원자재'] },
  { label: '우주항공 & 방위산업', value: 'aerospace', mapping: ['항공우주 & 방위산업'] },
  { label: '메타버스', value: 'metaverse', mapping: ['메타버스구현'] },
  { label: '가상현실', value: 'vr', mapping: ['가상현실(VR)'] },
  { label: '증권', value: 'bankingSecurities', mapping: ['핀테크', '플랫폼 대표주자', '언택트 경제'] },
  { label: '블록체인', value: 'blockchain', mapping: ['블록체인'] },
  { label: '부동산', value: 'realestateReits', mapping:['건물주의 꿈']},
  { label: '신재생에너지' ,value:'renewableEnergy' ,mapping:['클린 에너지','자원/에너지' ]},
  { label: '2차전지' ,value:'battery' ,mapping:['리튬 & 배터리']}
])

// 사용자가 선택한 카테고리를 저장하는 배열
const selectedCategories = ref([])

// 백엔드로 보낼 최종 관심사 데이터 (중복 제거된 매핑 값)
const userInterestMappings = ref([])

// 카테고리 선택 및 해제 함수
const toggleCategory = (category) => {
  if (selectedCategories.value.includes(category)) {
    // 이미 선택된 경우 해제
    selectedCategories.value = selectedCategories.value.filter(c => c !== category)
    // 해당 카테고리의 매핑 값도 제거
    userInterestMappings.value = userInterestMappings.value.filter(mapping => !category.mapping.includes(mapping))
  } else {
    // 선택되지 않은 경우 추가
    selectedCategories.value.push(category)
    // 해당 카테고리의 매핑 값을 추가 (중복 제거)
    userInterestMappings.value = [...new Set([...userInterestMappings.value, ...category.mapping])]
  }
}

const store = useUserInterestStore()

// watch를 통해 userInterestMappings가 변경될 때마다 store.userinterest 업데이트
watch(userInterestMappings, (newMappings) => {
  store.userinterest = newMappings // 스토어에 최종 관심사 매핑 값 저장
}, { immediate:true })

</script>

<style scoped>
.category-btn {
  border-radius:50px; /* 둥근 버튼 스타일 */
}

.category-btn.active{
background-color:#007bff;
color:white;
}

.btn-success[disabled]{
  opacity: 0.5;
}
</style>