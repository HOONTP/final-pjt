import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  // Accounts
  const token = ref(null)
  const currentUser = ref(0)
  const isLogin = computed(() => {
    // 로그인 여부 확인
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // Community
  const articles = ref([])
  const article = ref([])
  const LikedArticles = ref([])
  const hotArticles = ref([])
  
  // Movie
  const movies = ref([])
  const movie = ref([])
  const recommendmovies = ref([])
  const LikedMovies = ref([])
  const movieReviews = ref([])

  // Profile
  const profile = ref([])
  
  // Search
  const now_gps = ref()

  // 회원가입
  const signUp = function (payload) {
    const { nickname, username, password, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/user/`,
      data: {
        nickname, username, password, password2
      }
    })
      .then(() => {
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/log/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.token
        currentUser.value = res.data
        router.push({ name: 'MovieView' })
        getProfile(currentUser.value.user_id)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 로그아웃
  const logOut = function () {
    axios({
      method: 'delete',
      url: `${API_URL}/accounts/log/`,
    })
      .then(() => {
        token.value = null
        currentUser.value = 0
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 게시판 종류 별/작성자 별 게시글 목록 조회
  const getArticles = function (community_pk=0, user_pk=0) {
    axios({
      method: 'get',
      url: `${API_URL}/community/${community_pk}/articles/${user_pk}/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
    })
      .then((res) =>{
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 특정 게시글 조회
  const getArticle = function (article_pk) {
    axios({
      method: 'get',
      url: `${API_URL}/community/articles/${article_pk}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        article.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  // 좋아요 한 게시글 목록 조회
  const getLikedArticles = function (user_pk) {
    axios({
      method: 'get',
      url: `${API_URL}/community/${community_pk}/articles/${user_pk}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        LikedArticles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 인기글 조회
  const getHotArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community/hot/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        hotArticles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 영화 목록 조회
  const getMovies = function (page) {
    axios({
      method: 'get',
      url: `${API_URL}/movies/`,
      headers: {
        Authorization: `Token ${token.value}`,
        'page': page,
      }
    })
      .then((res) =>{
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  // 추천 영화 조회
  const getRecommendMovie = async function () {
    console.log(currentUser.value)
    await axios({
      method: 'get',
      url: `${API_URL}/movies/recommend/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
  })
    .then((res) => {
      // recommendmovies.value = null
      recommendmovies.value = res.data
      console.log(res.data)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  // 영화 좋아요 목록 감시 => 추천 영화 업데이트
  watch(LikedMovies, (newValue, oldValue) => {
    getRecommendMovie()
    console.log(newValue, 'new')
    console.log(oldValue, 'old')
  })

  // 영화 좋아요 및 취소
  const likeMovie = function (movie_pk) {
    axios({
      method: 'post',
      url: `${API_URL}/movies/${movie_pk}/likes/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
  })
    .then((res) => {
      LikedMovies.value = res.data
      getMovie(movie_pk)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  // 단일 영화 조회
  const getMovie = function (id) {
    axios({
      method: 'get',
      url: `${API_URL}/movies/${id}`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        movie.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 영화 리뷰 조회
  const getMovieReview = function (movieId) {
    axios({
      method: 'get',
      url: `${API_URL}/reviews/`,
      headers: {
        Authorization: `Token ${token.value}`,
        // movie: movieId
      }
    })
      .then((res) =>{
        movieReviews.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 검색 기능
  const searchMovie = function (keyword) {
    if (keyword === '') {
      alert('목숨이 아깝다면 값을 입력하세요.')
      return
    }
    axios({
      method: 'get',
      url: `${API_URL}/movies/search/?keyword=${keyword}`,
      headers: {
        Authorization: `Token ${token.value}`,
        'content-type': 'application/json;charset=UTF-8',
      }
    })
      .then((res) => {
        movies.value = res.data
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
        console.log(movies)
        alert('검색 결과가 없습니다.')
      })
  }
  const searchArticle = function (keyword) {
    if (keyword === '') {
      alert('목숨이 아깝다면 값을 입력하세요.')
      return
    }
    axios({
      method: 'get',
      url: `${API_URL}/community/search/${articles.value[0].board}/?keyword=${keyword}`,
      headers: {
        Authorization: `Token ${token.value}`,
        'content-type': 'application/json;charset=UTF-8',
      }
    })
      .then((res) => {
        articles.value = res.data
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
        console.log(articles)
        alert('검색 결과가 없습니다.')
      })
  }
  // 특정 프로필 조회
  const getProfile = function (user_pk) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/${user_pk}/person/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        profile.value = res
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return {
    // Default
    API_URL,

    // Accounts
    signUp, logIn, logOut,
    token, currentUser, isLogin,

    // Community
    getArticles, getArticle, getLikedArticles, getHotArticles,
    articles, article, LikedArticles, hotArticles,

    // Movie
    getMovies, getMovie, getRecommendMovie, likeMovie, getMovieReview,
    movies, movie, recommendmovies, LikedMovies, movieReviews,

    // Profile
    getProfile, 
    profile,

    // Search
    searchMovie, searchArticle,
  }
}, { persist: true })
