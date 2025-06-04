<template>
  <div>
    <h1>Dashboard</h1>
    <p>Welcome to your dashboard! Here you can view your spending predictions for the next month.</p>
    <p v-if="!predictions">Loading predictions...</p>
    <SpendingPredictionChart :predictions="predictions" />
  </div>
</template>

<script>
import axios from '../services/axios'
import SpendingPredictionChart from '../components/SpendingPredictionChart.vue'

export default {
  components: { SpendingPredictionChart },
  data() {
    return { predictions: null }
  },
  async created() {
    try {
      const response = await axios.get('predict/')
      this.predictions = response.data.predicted_spending
    } catch (error) {
      console.error('Error fetching predictions:', error)
    }
  }
}
</script>
