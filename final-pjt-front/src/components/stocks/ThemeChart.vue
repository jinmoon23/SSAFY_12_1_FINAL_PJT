<template>
  <div>
    <apexchart
      v-if="stockStore.chartdata && stockStore.chartdata.length > 0"
      width="800"
      height="400"
      type="line"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script setup>
import { useStockStore } from '@/stores/stock'
import { computed } from 'vue'

const stockStore = useStockStore()

// computed를 사용하여 반응형 데이터 처리
const chartData = computed(() => {
  const price = []
  const date = []
  
  if (stockStore.chartdata && stockStore.chartdata.length > 0) {
    stockStore.chartdata.forEach((data) => {
      price.push(data.average_close)
      date.push(data.date)
    })
  }
  
  return { price, date }
})

const chartOptions = computed(() => ({
  chart: {
    type: 'line',
    toolbar: {
      show: false
    },
    zoom: {
      enabled: false
    }
  },
  grid: {
    borderColor: '#f1f1f1',
    strokeDashArray: 4,
  },
  stroke: {
    curve: 'smooth',
    width: 2,
    colors: ['#008FFB']
  },
  xaxis: {
    categories: chartData.value.date,
    labels: {
      rotate: -45,
      style: {
        fontSize: '12px'
      }
    }
  },
  yaxis: {
    labels: {
      formatter: (value) => value.toFixed(2)
    }
  },
  tooltip: {
    y: {
      formatter: (value) => value.toFixed(2)
    }
  }
}))

const series = computed(() => [{
  name: 'Stock Price',
  data: chartData.value.price
}])
</script>