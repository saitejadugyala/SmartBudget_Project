<template>
  <div class="register">
    <h2 class="text-xl font-semibold mb-4">Register</h2>
    <form @submit.prevent="registerUser" class="grid gap-4">
      <input v-model="form.username" type="text" placeholder="Username" required />
      <input v-model="form.email" type="email" placeholder="Email" required />
      <input v-model="form.mobile_number" type="text" placeholder="Mobile Number" required />
      
      <select v-model="form.gender" required>
        <option disabled value="">Select Gender</option>
        <option>Male</option>
        <option>Female</option>
        <option>Other</option>
      </select>
      
      <input v-model="form.password" type="password" placeholder="Password" required />
      <button type="submit" class="bg-blue-600 text-white py-2 rounded hover:bg-blue-700">Register</button>
    </form>

    <p class="mt-4 text-red-500" v-if="error">{{ error }}</p>
    <p class="mt-4 text-green-600" v-if="success">{{ success }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        username: '',
        email: '',
        mobile_number: '',
        gender: '',
        password: ''
      },
      error: '',
      success: ''
    }
  },
  methods: {
    async registerUser() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/register/', this.form)
        this.success = 'Registration successful! Please log in.'
        this.error = ''
        this.form = { username: '', email: '', mobile_number: '', gender: '', password: '' }
      } catch (err) {
        this.error = err.response?.data?.detail || 'Registration failed. Try again.'
        this.success = ''
      }
    }
  }
}
</script>

<style scoped>
input, select {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
}
button {
  padding: 10px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
.error {
  color: red;
}
.success {
  color: green;
}

</style>
