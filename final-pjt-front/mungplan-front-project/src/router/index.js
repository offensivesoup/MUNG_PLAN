// 이건 파일 여러개 못 만드나? 좀 복잡스
// path에 community, life 이런 거 꼭 넣어야 할까? 뺄까? 넘 길어져서

import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
// adopt
import AdoptView from '@/views/adopt/AdoptView.vue'
import AdoptDetailView from '@/views/adopt/DetailView.vue'

// map
import MapView from '@/views/map/MapView.vue'

// community
import ArticleView from '@/views/community/ArticleView.vue'
import ArticleDetailView from '@/views/community/DetailView.vue'
import ArticleCreateView from '@/views/community/CreateView.vue'

// market
import MarketView from '@/views/market/MarketView.vue'

// finance
import DepositView from '@/views/finance/DepositView.vue'
import DepositDetailView from '@/views/finance/DetailView.vue'
import RecommendDepositView from '@/views/finance/RecommendDepositView.vue'

// account
import SignUpView from '@/views/account/SignUpView.vue'
import LogInView from '@/views/account/LogInView.vue'
import ProfileView from '@/views/account/ProfileView.vue'

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
      path: '/adopts/',
      name: 'AdoptView',
      component: AdoptView
    },
    {
      path: '/adopt/:id',
      name: 'AdoptDetailView',
      component: AdoptDetailView
    },
    {
      path: '/map',
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
      name: 'ArticleCreateView',
      component: ArticleCreateView
    },

    // for market
    {
      path: '/market',
      name: 'MarketView',
      component: MarketView
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
      path: '/finance/recommend-deposit',
      name: 'RecommendDepositView',
      component: RecommendDepositView
    },

    // for map
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },

    // for account
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/profile/:username',
      name: 'ProfileView',
      component: ProfileView
    }
  ]
})

import { useAccountStore } from '@/stores/account'

router.beforeEach((to, from) => {
  const store = useAccountStore()
  // 인증되지 않은 사용자는 create에 접근 할 수 없음
  if (to.name === 'ArticleCreateView' && store.state.isAuthenticated === false) {
    window.alert('로그인이 필요해요!!')
    return { name: 'LogInView' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.state.isAuthenticated === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }
})

export default router
