import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createNaverMap } from "vue3-naver-maps";
import { createPinia } from 'pinia'
import './styles/global.css'
import App from './App.vue'
import router from './router'
import '@fortawesome/fontawesome-free/css/all.css'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.use(router)
app
  .use(createNaverMap, {
    clientId: import.meta.env.VITE_APP_CLIENT_ID,
    category: "ncp", // Optional
    subModules: [], // Optional, "panorama" | "geocoder" | "drawing" | "visualization"
  })

app.mount('#app')
