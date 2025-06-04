<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
    <p v-if="error" class="error">Login failed: {{ error }}</p>
  </div>
</template>

<script>
import { login } from '../services/auth'

export default {
  data() {
    return {
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async handleLogin() {
      try {
        await login(this.email, this.password)
        this.$router.push('/')
      } catch (err) {
        this.error = 'Invalid email or password.'
      }
    }
  }
}
</script>

<style scoped>
input {
  display: block;
  margin: 10px 0;
  padding: 8px;
  width: 200px;
}
button {
  padding: 8px 16px;
  background-color: #42b883;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #367c6b;
}
.error {
  color: red;
  margin-top: 10px;
}
</style>
