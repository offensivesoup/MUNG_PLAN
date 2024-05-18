// 이건 파일 여러개 못 만드나? 좀 복잡스
// path에 community, life 이런 거 꼭 넣어야 할까? 뺄까? 넘 길어져서

import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
// life
import AdoptView from '@/views/life/adopt/AdoptView.vue'
import AdoptDetailView from '@/views/life/adopt/DetailView.vue'
import MapView from '@/views/life/map/MapView.vue'

// community
import ArticleView from '@/views/community/ArticleView.vue'
import ArticleDetailView from '@/views/community/DetailView.vue'
import CreateView from '@/views/community/CreateView.vue'

// finance
import DepositView from '@/views/finance/DepositView.vue'
import DepositDetailView from '@/views/finance/DepositView.vue'
import DepositRecommendView from '@/views/finance/DepositRecommendView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },

    // for adopt
    {
      path: '/life/adopts/',
      name: 'AdoptView',
      component: AdoptView
    },
    {
      path: '/life/adopt/:id',
      name: 'AdoptDetailView',
      component: AdoptDetailView
    },
    {
      path: '/life/map',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/community/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    // {
    //   path: '/community/articles/share',
    //   name: 'ArticleShareView',
    //   component: ArticleShareView
    // },
    // {
    //   path: '/community/articles/used',
    //   name: 'ArticleUsedView',
    //   component: ArticleUsedView
    // },
    // {
    //   path: '/community/articles/town',
    //   name: 'ArticleTownView',
    //   component: ArticleTownView
    // },

    // for community
    {
      path: '/community/article/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/community/article/create',
      name: 'CreateView',
      component: CreateView
    },

    // for finance
    {
      path: '/finance/deposits',
      name: 'DepositView',
      component: DepositView
    },
    {
      path: '/finance/deposit/:id',
      name: 'DepositDetailView',
      component: DepositDetailView
    },
    {
      path: '/finance/deposit/recommend',
      name: 'DepositRecommendView',
      component: DepositRecommendView
    },
  ]
})

export default router
