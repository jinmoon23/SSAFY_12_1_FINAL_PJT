<template>
  <div class="container mt-4">
    <div class="row">
      <!-- 국내 주식 칼럼 -->
      <div class="col-md-6">
        <div class="card shadow-sm">
          <div class="card-header bg-light">
            <h2 class="h4 mb-0 fw-bold">국내</h2>
          </div>
          <div class="card-body">
            <div class="stock-list">
              <div v-for="stock in koreanStocks" 
                  :key="stock.code" 
                  class="stock-item">
                <div class="d-flex align-items-center p-2 border-bottom" @click="moveStockItem(stock.code)">
                  <div class="stock-logo me-3">
                    <img :src="getStockLogo(stock.code)" 
                        :alt="stock.name"
                        class="rounded-circle"
                        width="40"
                        height="40">
                  </div>
                  <span class="stock-name">{{ stock.name }}</span>
                  <span class="ms-auto">{{ formatPrice(stock.price) }}원</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 미국 주식 칼럼 -->
      <div class="col-md-6">
        <div class="card shadow-sm">
          <div class="card-header bg-light">
            <h2 class="h4 mb-0 fw-bold">미국</h2>
          </div>
          <div class="card-body">
            <div class="stock-list">
              <div v-for="stock in usaStocks" 
                  :key="stock.code" 
                  class="stock-item">
                <div class="d-flex align-items-center p-2 border-bottom" @click="moveStockItem(stock.code)">
                  <div class="stock-logo me-3">
                    <img :src="getStockLogo(stock.code)" 
                        :alt="stock.name"
                        class="rounded-circle"
                        width="40"
                        height="40">
                  </div>
                  <span class="stock-name">{{ stock.name }}</span>
                  <span class="ms-auto">{{ formatPrice(stock.price) }}원</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useStockStore } from '@/stores/stock'
import { useStockItemStore } from '@/stores/stockitem'
import { computed, onMounted , ref} from 'vue'
import { useRouter } from 'vue-router'

const stockStore = useStockStore()
const stockItemStore = useStockItemStore()
const router = useRouter()
const stockLogos = ref({});

const checkUsa = (stock_code) => isNaN(stock_code)

// 국내/미국 주식 분리
const koreanStocks = computed(() => 
  stockStore.stocklist.filter(stock => !checkUsa(stock.code))
)

const usaStocks = computed(() => 
  stockStore.stocklist.filter(stock => checkUsa(stock.code))
  
)

const checkImageExists = (url) => {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(true);
    img.onerror = () => resolve(false);
    img.src = url;
  });
};

const getStockLogo = (code) => {
  if (isNaN(Number(code))) {
    const parqetLogoUrl = `https://assets.parqet.com/logos/symbol/${code}?format=png`;
    const isParqetLogoValid = checkImageExists(parqetLogoUrl);
    if (isParqetLogoValid) {
      return parqetLogoUrl;
    }
  }
  try {
    return new URL(`../../assets/logos/${code}.png`, import.meta.url).href;
  } catch {
    console.error(`로컬 이미지가 존재하지 않습니다: @/assets/logos/${code}.png`);
    return null;
  }
};

// 모든 주식의 로고 URL을 초기화
// const initializeStockLogos = () => {
//   for (const stock of koreanStocks.value) {
//     if (!stockLogos.value[stock.code]) {
//       stockLogos.value[stock.code] =  getStockLogo(stock.code);
//     }
//   }
//   for (const stock of usaStocks.value) {
//     if (!stockLogos.value[stock.code]) {
//       stockLogos.value[stock.code] =  getStockLogo(stock.code);
//     }
//   }
// };

const formatPrice = (price) => {
  return price.toLocaleString('ko-KR')
}

const getCurrentTime = () => {
  const now = new Date()
  const hours = String(now.getHours()).padStart(2, '0')
  const minutes = String(now.getMinutes()).padStart(2, '0')
  const seconds = String(now.getSeconds()).padStart(2, '0')
  return `${hours}${minutes}${seconds}`
}

const currentTime = getCurrentTime()

const moveStockItem = function (stockcode) {
  router.push({
    name: 'day',
    params: { stock_id: stockcode }
  })

}

</script>

<style scoped>
.stock-list {
  max-height: 70vh;
  overflow-y: auto;
}

.stock-item:hover {
  background-color: var(--primary-light_g);
}

.stock-name {
  font-size: 0.95rem;
}

/* 스크롤바 스타일링 */
.stock-list::-webkit-scrollbar {
  width: 6px;
}

.stock-list::-webkit-scrollbar-track {
  background: #f1f1f1;
}

.stock-list::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 3px;
}

.stock-list::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>