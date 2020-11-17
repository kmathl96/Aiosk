import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import axios from 'axios'
import '@/fontAwesomeIcon.js';
import vuetify from './plugins/vuetify';
import store from './vuex/store';

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
const SERVER_URL = "https://www.aiosk.co.kr:3000/"
// const SERVER_URL = "http://localhost:3000/"
Vue.prototype.$SERVER_URL = SERVER_URL;
new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App)
}).$mount("#app");
