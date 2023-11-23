<template>
  <div>
    <!-- 리뷰 list 컴포넌트 -->
    <MovieReviewItem />

    <!-- 리뷰 작성 폼 -->
    <div class="review-form">
      <label for="review">{{ store.currentUser.username }}님의 리뷰를 남겨주세요.</label>
      <div class="review-area">
        <textarea
          v-model.trim="newReview"
          id="review"
          placeholder="리뷰를 입력하세요..."
          @keyup.enter="createReview">          
        </textarea>
        <button @click="createReview" class="submit-button">등록</button>
      </div>
    </div>
  </div>
  <!-- 댓글 작성 폼 -->

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
.review-section {
  display: flex;
  flex-direction: column;
  gap: 20px; /* 댓글과 댓글 작성 폼 간의 간격 */
  min-width: 800px; /* 예시로 설정한 최소 너비 */
  max-width: 800px; /* 예시로 설정한 최대 너비 */
  margin: auto;
}

.review-form {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px; /* 레이블과 textarea 간의 간격 */
  background-color: #f2f2f2; /* 연한 회색 배경색 */
  padding: 20px; /* 패딩 설정 */
  border-radius: 5px; /* 둥근 테두리 적용*/
  margin-bottom: 50px;
}

.review-area {
  display: flex;
  gap: 20px; /* textarea와 button 간의 간격 */
}

label {
  align-self: flex-start; /* 왼쪽 정렬 */
}

textarea {
  width: 100%; /* 가로로 화면을 채우도록 설정 */
}

button {
  width: 80px;
  height: 60px;
}

.submit-button {
  background-color: #4CAF50;
  color: white;
  font-size: 16px;
  border-radius: 5px; 
  transition: background-color 0.3s;
  border: none;
}

.submit-button:hover {
  background-color: #45a049;
}
</style>
