import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import RegisteView from '../views/RegisteView.vue'


const routes = [
  { path: '/dashboard', name:'Dashboard', component: Dashboard },
  { path: '/login', name:'Login', component: Login },
  {path: '/register', name: 'Register', component: RegisteView },
  {path: '/', redirect: '/Login' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
