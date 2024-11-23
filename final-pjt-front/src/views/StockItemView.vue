<template>
  <div class="container-fluid px-4 mt-5">
    <h1 class="mb-4">{{ stockItemStore.stockInfo.articles_data?.stock_name }}</h1>
    
    <!-- 차트와 종목정보 섹션 -->
    <div class="row gx-4 mb-4">
      <!-- 차트 섹션 (왼쪽) -->
      <div class="col-lg-8">
        <!-- 네비게이션 Pills -->
        <ul class="nav nav-pills mb-4">
          <li class="nav-item">
            <RouterLink 
              :to="{ name: 'day', params: { stock_id: stockcode }}" 
              class="nav-link" 
              :class="{ active: $route.name === 'day' || !$route.name }"
              @click="moveDayChart(stockcode)"
            >일</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink 
              :to="{ name: 'week', params: { stock_id: stockcode }}" 
              class="nav-link"
              :class="{ active: route.name === 'week' }"
              @click="movePeriodChart('W')"
            >주</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink 
              :to="{ name: 'month', params: { stock_id: stockcode }}" 
              class="nav-link"
              :class="{ active: route.name === 'month' }"
              @click="movePeriodChart('1M')"
            >월</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink 
              :to="{ name: 'sixmonth', params: { stock_id: stockcode }}" 
              class="nav-link"
              :class="{ active: route.name === 'sixmonth' }"
              @click="movePeriodChart('6M')"
            >6개월</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink 
              :to="{ name: 'year', params: { stock_id: stockcode }}" 
              class="nav-link"
              :class="{ active: route.name === 'year' }"
              @click="movePeriodChart('1Y')"
            >년</RouterLink>
          </li>
        </ul>
        
        <!-- 차트 영역 -->
        <div class="chart-container">
          <RouterView></RouterView>
        </div>
      </div>

      <!-- 종목 정보 섹션 (오른쪽) -->
      <div class="col-lg-4">
        <div class="stock-info-container">
          <div v-if="isNaN(stockcode)">
            <UsaStockInfo/>
          </div>
          <div v-else>
            <DomesticStockInfo/>
          </div>
        </div>
      </div>
    </div>


  <!-- 커뮤니티 섹션 -->
  <div class="row mt-4">
    <div class="col-12">
      <div class="community-container">
        <div class="d-flex justify-content-between align-items-center mb-4">
          <h3 class="community-title" @click="moveCommunity">커뮤니티</h3>
          <button class="btn btn-primary rounded-pill px-4" @click="writeArticle">
            <i class="bi bi-pencil-fill me-2"></i>글 작성하기
          </button>
        </div>
        
        <!-- 최신 5개 게시글 -->
        <div class="articles-list">
          <div v-for="article in latestArticles" 
              :key="article.id" 
              class="article-card">
            <!-- 작성자 정보 -->
            <div class="article-user-info">
              <div class="user-avatar">
                <img src="" alt="user avatar" class="rounded-circle">
              </div>
              <div class="user-details">
                <span class="user-name">{{ article.author_nickname || '익명' }}</span>
                <span class="post-time">{{ formatTime(article.created_at) }}</span>
              </div>
              <div class="more-options">
                <i class="bi bi-three-dots-vertical"></i>
              </div>
            </div>
            
            <!-- 게시글 내용 -->
            <div class="article-content">
              <h5 class="mb-2">{{ article.title }}</h5>
              <p class="article-text">{{ article.content }}</p>
              <div class="theme-tag">
                <span class="badge rounded-pill bg-light text-dark">
                  {{ article.theme_name }}
                </span>
              </div>
            </div>
            
            <!-- 좋아요/댓글 버튼 -->
            <div class="article-actions">
              <button class="btn btn-link">
                <i class="bi bi-heart"></i>
                <span>좋아요</span>
              </button>
              <button class="btn btn-link">
                <i class="bi bi-chat"></i>
                <span>댓글</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script setup>
import DomesticStockInfo from '@/components/stocks/DomesticStockInfo.vue'
import UsaStockInfo from '@/components/stocks/UsaStockInfo.vue'
import { useStockItemStore } from '@/stores/stockitem'
import { computed, onMounted, ref, watch } from 'vue'
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'

const stockItemStore = useStockItemStore()
const route = useRoute()
const router = useRouter()
const stockcode = route.params.stock_id

// 입력 코드 국내/해외 인지 구분하기!
const checkDomestic = (stockcode) => isNaN(stockcode)

const getCurrentTime = () => {
  const now = new Date()
  const hours = String(now.getHours()).padStart(2, '0')
  const minutes = String(now.getMinutes()).padStart(2, '0')
  const seconds = String(now.getSeconds()).padStart(2, '0')
  return `${hours}${minutes}${seconds}`
}

// 라우트링크 클릭할때는 주, 월, 년 각각 데이터 받아오기
const movePeriodChart = function (period) {
  // 주, 월, 년 함수
  stockItemStore.getPeriodInfo(stockcode, period)
  console.log(stockItemStore.periodChart)
}

const currentTime = getCurrentTime()

const moveDayChart = function (stockcode){
  stockItemStore.getDayInfo(stockcode, currentTime)
}

// 페이지 처음 들어왔을때
onMounted(() => {
  // 종목 정보 먼저 가져오기
stockItemStore.getStockInfo(stockcode, currentTime)
  // 일 차트 그리기
stockItemStore.getDayInfo(stockcode, currentTime)
})

const moveCommunity = function () {
  router.push({ name: 'CommunityView'})
}

const writeArticle = () => {
  // 글 작성 페이지로 이동하는 로직 구현
  router.push({
    name: 'CreateArticleView',
    params: { stock_id: stockcode }
  })
}

////커뮤니티 관련
// 최신 5개 게시글만 표시
const latestArticles = computed(() => {
  return stockItemStore.stockInfo.articles_data?.articles.slice(0, 5) || []
})

const formatTime = (timestamp) => {
  // 한국 시간으로 변환
  const date = new Date(timestamp)
  const now = new Date()

  // 한국 시간으로 조정 (UTC+9)
  const kstDate = new Date(date.getTime() + (9 * 60 * 60 * 1000))
  const diff = now - kstDate

  // 1시간 이내
  if (diff < 3600000) {
    const minutes = Math.floor(diff / 60000)
    return `${minutes}분 전`
  }
  // 24시간 이내
  if (diff < 86400000) {
    const hours = Math.floor(diff / 3600000)
    return `${hours}시간 전`
  }
  // 그 외
  return `${kstDate.getMonth() + 1}월 ${kstDate.getDate()}일`
}

</script>

<style scoped>
.container-fluid {
  max-width: 1600px;
  margin: 0 auto;
}

.chart-container {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  height: calc(100vh - 250px);
}

.stock-info-container {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  height: calc(100vh - 250px);
  overflow-y: auto;
}

.nav-pills .nav-link {
  margin-right: 0.5rem;
  border-radius: 20px;
  padding: 0.5rem 1.5rem;
}

.nav-pills .nav-link.active {
  background-color: #0d6efd;
}

h1 {
  font-size: 1.8rem;
  color: #333;
  margin-left: 0.5rem;
}

.btn-primary {
  background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
  border: none;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

.community-container {
  max-width: 600px;
  margin: 0 auto;
}

.article-card {
  background: white;
  border-radius: 15px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.article-user-info {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.user-avatar img {
  width: 40px;
  height: 40px;
  object-fit: cover;
}

.user-details {
  margin-left: 0.8rem;
  flex-grow: 1;
}

.user-name {
  display: block;
  font-weight: 600;
  font-size: 0.95rem;
}

.post-time {
  font-size: 0.8rem;
  color: #666;
}

.more-options {
  color: #666;
  cursor: pointer;
}

.article-content {
  margin-bottom: 1rem;
}

.article-text {
  color: #444;
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
}

.theme-tag {
  margin-bottom: 0.5rem;
}

.article-actions {
  display: flex;
  gap: 1rem;
  border-top: 1px solid #eee;
  padding-top: 1rem;
}

.article-actions .btn-link {
  color: #666;
  text-decoration: none;
}

.article-actions .btn-link i {
  margin-right: 0.4rem;
}
</style>