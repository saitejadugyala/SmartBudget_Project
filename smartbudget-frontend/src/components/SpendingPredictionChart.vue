<template>
  <div>
    <Bar v-if="chartData" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title, Tooltip, Legend,
  BarElement, CategoryScale, LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'SpendingPredictionChart',
  components: { Bar },
  props: ['predictions'],
  computed: {
    chartData() {
      if (!this.predictions) return null
      return {
        labels: Object.keys(this.predictions),
        datasets: [
          {
            label: 'Predicted Spending (Next Month)',
            data: Object.values(this.predictions),
            backgroundColor: '#42a5f5',
          }
        ]
      }
    },
    chartOptions() {
      return {
        responsive: true,
        plugins: {
          legend: { position: 'top' },
          title: { display: true, text: 'Spending Forecast by Category' }
        }
      }
    }
  }
}
</script>
