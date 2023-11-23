<template>
  <div class="comment-section">
    <!-- 댓글 list 컴포넌트 -->
    <CommentList />
    
    <!-- 댓글 작성 폼 -->
    <div class="comment-form">
      <label for="comment">{{ store.currentUser.username }}님의 댓글을 남겨주세요.</label>
      <div class="comment-area">
        <textarea
          v-model.trim="newComment"
          id="comment"
          placeholder="댓글을 입력하세요...">
        </textarea>
        <button @click="createComment" class="submit-button">등록</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import CommentList from '@/components/community/CommentList.vue'

const store = useCounterStore()
const route = useRoute()
const newComment = ref('')  // 새로 작성할 댓글을 담을 변수

onMounted(() => {
  // 게시글 데이터 가져오기
  store.getArticle(route.params.id)
})

const createComment = () => {
  // 새로운 댓글 작성
  axios({
    method: 'post',
    url: `${store.API_URL}/community/articles/${route.params.id}/comments/`,
    data: {
      content: newComment.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      // 댓글 작성 후에는 입력 필드 초기화
      newComment.value = ''
      store.getArticle(route.params.id)
    })
    .catch((err) => {
      console.log('댓글 생성 에러:', err)
    })
}
</script>

<style scoped>
.comment-section {
  display: flex;
  flex-direction: column;
  gap: 20px; /* 댓글과 댓글 작성 폼 간의 간격 */
  width: 60%;
  min-width: 800px; /* 예시로 설정한 최소 너비 */
  max-width: 1200px; /* 예시로 설정한 최대 너비 */
  margin: auto;
}

.comment-form {
  display: flex;
  flex-direction: column;
  gap: 10px; /* 레이블과 textarea 간의 간격 */
  background-color: #f2f2f2; /* 연한 회색 배경색 */
  padding: 20px; /* 패딩 설정 */
  border-radius: 5px; /* 둥근 테두리 적용*/
}

.comment-area {
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
