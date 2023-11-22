<template>
  <div>
    <h1>영화 리뷰</h1>

    <!-- 리뷰 list 컴포넌트 -->
    <MovieReviewItem />

    <!-- 리뷰 작성 폼 -->
    <div>
      <label for="review">리뷰 작성:</label>
      <textarea v-model.trim="newReview" id="review"></textarea>
      <button @click="createReview">등록</button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import MovieReviewItem from '@/components/movie/MovieReviewItem.vue'

const store = useCounterStore()
const route = useRoute()
const movieId = route.params.id
const newReview = ref('')  // 새로 작성할 리뷰를 담을 변수

onMounted(async () => {
    store.getMovie(movieId)
  })

const createReview = () => {
  // 새로운 리뷰 작성
  axios({
    method: 'post',
    url: `${store.API_URL}/movies/${movieId}/reviews/`,
    data: {
      content: newReview.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      // 리뷰 작성 후에는 입력 필드 초기화
      newReview.value = ''
      store.getMovie(movieId)
    })
    .catch((err) => {
      console.log('리뷰 생성 에러:', err)
    })
}

</script>

<style scoped>

</style>
