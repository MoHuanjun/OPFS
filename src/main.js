import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import VueAxios from 'vue-axios';
import qs from 'qs'
import VueRouter from "vue-router";

axios.defaults.withCredentials = true
Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(VueAxios , axios)
Vue.use(VueRouter)

Vue.prototype.$axios = axios    //全局注册，使用方法为:this.$axios
Vue.prototype.qs = qs   //全局注册，使用方法为:this.qs

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
