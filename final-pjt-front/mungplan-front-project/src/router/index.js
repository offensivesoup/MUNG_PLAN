import { createRouter, createWebHistory } from 'vue-router'
// life
import AdoptView from '@/views/life/adopt/AdoptView.vue'
import AdoptDetailView from '@/views/life/adopt/DetailView.vue'
import MapView from '@/views/life/map/MapView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'HomeView',
    //   component: HomeView
    // },
    {
      path: '/life/adopt',
      name: 'AdoptView',
      component: AdoptView
    },
    // {
    //   path: '/life/adopt/:num',
    //   name: 'AdoptDetailView',
    //   component: AdoptDetailView
    // },
    {
      path: '/life/map',
      name: 'MapView',
      component: MapView
    }
  ]
})

export default router
