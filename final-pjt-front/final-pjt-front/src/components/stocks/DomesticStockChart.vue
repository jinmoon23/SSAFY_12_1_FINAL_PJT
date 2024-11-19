<template>
  <div>
    <h1>실시간 주가 차트</h1>
    <div class="card-body">
      <div class="tab-content p-0">
        <div class="chart tab-pane active">
          <Line 
            v-if="chartData"
            :data="chartData"
            :options="chartOptions"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, provide, onMounted, onUnmounted } from 'vue'


//////////////// 차트 그리는 코드

import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale
} from 'chart.js'


ChartJS.register(
  Title,
  Tooltip,
  Legend,
  ArcElement,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale
)

// 차트 데이터 관리
const timeLabels = ref([])
const priceData = ref([])

// 최대 데이터 포인트 수
const MAX_DATA_POINTS = 30

// 차트 데이터 계산
const chartData = computed(() => ({
  labels: timeLabels.value,
  datasets: [
    {
      label: '주가',
      borderColor: '#36A2EB',
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      data: priceData.value,
      tension: 0.4
    }
  ]
}))

// 차트 옵션
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: false,
      ticks: {
        callback: value => `${value}원`
      }
    }
  },
  plugins: {
    legend: {
      display: true
    },
    tooltip: {
      callbacks: {
        label: context => `${context.parsed.y}원`
      }
    }
  }
}

//////////////// 당일 시세 조회 코드

// axios 로 백에서 받아오기,,,

//////////////// 실시간 웹소켓 통신 데이터 받는 코드

const socket = ref(null)
let isRunning = true

const currentTime = ref(null)
const currentPrice = ref(null)

// 받은 데이터 처리..!!
const stockspurchaseDomestic = (data) => {
  const pValue = data.split('^');

  currentTime.value = pValue[1]
  currentPrice.value = parseInt(pValue[2])

  // 차트 데이터 업데이트
  updateChartData(time, price)

  return {
    current_time: pValue[1],
    current_price: pValue[2]
  };
};

// 차트 데이터 업데이트 함수
const updateChartData = (time, price) => {
  // 시간 레이블 추가
  timeLabels.value.push(time)
  priceData.value.push(price)

  // 최대 데이터 포인트 수를 유지
  if (timeLabels.value.length > MAX_DATA_POINTS) {
    timeLabels.value.shift()
    priceData.value.shift()
  }
}

const sendMessage = () => {
  if (socket.value && socket.value.readyState === WebSocket.OPEN) {
    socket.value.send(JSON.stringify({
      header: {
        approval_key: '9cf04d10-0346-4c6c-8275-eeb356afe439',
        custtype: "P",
        tr_type: "1",
        content_type: "utf-8"
      },
      body: {
        input: {
          tr_id: "H0STCNT0",
          tr_key: "005930"
        }
      }
    }))
  }
  console.log('메세지 전송 완료')
}

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms))

const receiveMessage = () => {
  return new Promise((resolve) => {
    socket.value.onmessage = (event) => {
      console.log('Raw data:', event.data)
      const processedData = stockspurchaseDomestic(event.data)
      console.log('Processed data:', processedData)
      resolve(processedData)
    }
  })
}

const dataFetchLoop = async () => {
  while (isRunning) {
    sendMessage()
    await receiveMessage()
    await sleep(3000) // 5초 대기
  }
}


onMounted(() => {
  socket.value = new WebSocket('ws://ops.koreainvestment.com:21000')

  // 실시간으로 받는 데이터 

  socket.value.onopen = () => {
    console.log('WebSocket 연결이 열렸습니다.')
    dataFetchLoop()
    // sendMessage() // 연결이 열린 후 메시지 전송
  }

  socket.value.onerror = (error) => {
    console.error('WebSocket 오류:', error)
  }

  socket.value.onclose = () => {
    console.log('WebSocket 연결이 닫혔습니다.')
    isRunning = false
  }
})

onUnmounted(() => {
  isRunning = false
  if (socket.value) {
    socket.value.close()
  }
})
</script>

<style scoped>
.chart {
  height: 400px;
}
</style>