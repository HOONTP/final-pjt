import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const profileData = ref()
  const movies = ref()
  
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const signUp = function (payload) {
    const { nickname, username, password, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/user/`,
      data: {
        nickname, username, password, password2
      }
    })
      .then((res) => {
        console.log(res)
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

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
        console.log(res)
        token.value = res.data.token
        router.push({ name: 'CommunityView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'delete',
      url: `${API_URL}/accounts/log/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const profileDetail = function (user_pk) {
    axios({
      method: 'GET',
      url: `${API_URL}/accounts/${user_pk}/person/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        profileData.value = res
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/movies/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        console.log(res)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return { API_URL, signUp, logIn, token, isLogin, logOut, profileDetail, profileData, 
    getArticles, articles, 
    getMovies, movies,
  }
}, { persist: true })
