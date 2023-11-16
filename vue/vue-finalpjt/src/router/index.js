import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

// Acounts
import LogInView from '@/views/accounts/LogInView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'

// Community
import ArticleView from '@/views/community/ArticleView.vue'
import ArticleCreateView from '@/views/community/ArticleCreateView.vue'
import ArticleDetailView from '@/views/community/ArticleDetailView.vue'
// import ArticleEditView from '@/views/community/ArticleEditView.vue'

// Movie
import MovieHomeView from '@/views/movies/MovieHomeView.vue'
import MovieDetailView from '@/views/movies/MovieDetailView.vue'

// Profile
import ProfileArticleView from '@/views/profile/ProfileArticleView.vue'
import ProfileBookmarkView from '@/views/profile/ProfileBookmarkView.vue'
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
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: ArticleCreateView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: ArticleDetailView
    },
    // {
    //   path: '/articles/:id/edit',
    //   name: 'EditView',
    //   component: ArticleEditView
    // },

    // Movie
    {
      path: '/movie',
      name: 'MovieHomeView',
      component: MovieHomeView
    },
    {
      path: '/movie/:movieId',
      name: 'MovieDetailView',
      component: MovieDetailView
    },

    // Profile
    {
      path: '/profile/:username',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/profile/:username/article',
      name: 'ProfileArticleView',
      component: ProfileArticleView
    },
    {
      path: '/profile/:username/bookmark',
      name: 'ProfileBookmarkView',
      component: ProfileBookmarkView
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
