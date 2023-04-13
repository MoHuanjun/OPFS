import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '@/components/Login.vue';
import Register from "@/components/Register.vue";
import Uploader from "@/components/Uploader.vue";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/uploader',
    name: 'Uploader',
    component: Uploader
  },
]

const router = new VueRouter({
  mode:"history",
  routes
})

export default router
