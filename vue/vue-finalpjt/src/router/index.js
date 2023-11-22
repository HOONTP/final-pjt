import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

// Acounts
import LogInView from '@/views/accounts/LogInView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'

// Community
import CommunityFreeView from '@/views/community/CommunityFreeView.vue'
import CommunityHotView from '@/views/community/CommunityHotView.vue'
import CommunityReviewView from '@/views/community/CommunityReviewView.vue'
import CommunityTotalView from '@/views/community/CommunityTotalView.vue'
import ArticleCreateView from '@/views/community/ArticleCreateView.vue'
import ArticleDetailView from '@/views/community/ArticleDetailView.vue'
import ArticleEditView from '@/views/community/ArticleEditView.vue'

// Movie
import MovieView from '@/views/movie/MovieView.vue'
import MovieDetailView from '@/views/movie/MovieDetailView.vue'

// Profile
import ProfileView from '@/views/profile/ProfileView.vue'
import ProfileArticleView from '@/views/profile/ProfileArticleView.vue'
import ProfileCommentView from '@/views/profile/ProfileCommentView.vue'
import ProfileLikeView from '@/views/profile/ProfileLikeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Accounts
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },

    // Community
    {
      path: '/community/free',
      name: 'CommunityFreeView',
      component: CommunityFreeView
    },
    {
      path: '/community/hot',
      name: 'CommunityHotView',
      component: CommunityHotView
    },
    {
      path: '/community/review',
      name: 'CommunityReviewView',
      component: CommunityReviewView
    },
    {
      path: '/community/total',
      name: 'CommunityTotalView',
      component: CommunityTotalView
    },
    {
      path: '/articles/create',
      name: 'ArticleCreateView',
      component: ArticleCreateView,
      props: route => ({ board1: route.params.board1 }) // 이 부분 추가
    },
    {
      path: '/articles/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/articles/:id/edit',
      name: 'ArticleEditView',
      component: ArticleEditView
    },

    // Movie
    {
      path: '/movie',
      name: 'MovieView',
      component: MovieView
    },
    {
      path: '/movie/:id',
      name: 'MovieDetailView',
      component: MovieDetailView
    },

    // Profile
    {
      path: '/profile/:nickName',
      name: 'ProfileView',
      component: ProfileView,
      props: true,
    },
    {
      path: '/profile/:username/article',
      name: 'ProfileArticleView',
      component: ProfileArticleView
    },
    {
      path: '/profile/:username/comment',
      name: 'ProfileCommentView',
      component: ProfileCommentView
    },
    {
      path: '/profile/:username/like',
      name: 'ProfileLikeView',
      component: ProfileLikeView
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'ArticleView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }
})

export default router
