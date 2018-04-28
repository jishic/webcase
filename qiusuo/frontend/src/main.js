// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import axios from "axios";

import store from './store'
import vuescroll from 'vue-scroll'
import { EmojiPickerPlugin } from 'vue-emoji-picker'
Vue.use(EmojiPickerPlugin)
Vue.use(vuescroll, {throttle: 600})
Vue.config.productionTip = false
Vue.use(ElementUI)
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
Vue.prototype.$axios = axios
// require('./AgoraRTCSDK-2.1.1.js')
// require('./vendor/jquery.js')

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',

})
