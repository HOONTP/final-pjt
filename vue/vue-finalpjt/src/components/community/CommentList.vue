<template>
  <div>
    <div v-if="store.article && store.article.comments && store.article.comments.length > 0">
      <ul>
        <hr class="comment-divider">
        <div v-for="comment in store.article.comments" :key="comment.id" class="comment-container">
          <div class="comment-info">
            <h4>{{ comment.user_nickname }}</h4>
            <p class="comment-time">({{ formatCommentTime(comment.created_at) }})</p>
          </div>

          <p class="comment-content">{{ comment.content }}</p>

          <div class="buttons">
            <!-- 답글 버튼 -->
            <p class="button" @click="toggleReplyForm(comment.id)"><strong>답글쓰기</strong></p>

            <!-- 답글 작성 폼 -->
            <div v-if="activeReplyForm === comment.id" class="reply-form">
              <div class="reply-area">
                <textarea
                  v-model.trim="newReply"
                  id="reply"
                  placeholder="답글을 입력하세요..."
                  class="reply-textarea"
                  @keydown.enter.prevent="createReply(comment.id)">
                </textarea>
                <button @click="createReply(comment.id)" class="submit-button">등록</button>
              </div>
            </div>

            <!-- 내가 작성한 댓글만 수정/삭제 버튼 존재 -->
            <div v-if="store.currentUser.user_id === comment.user" class="my-buttons">
              <!-- 댓글 수정 버튼 -->
              <p class="button" @click="editCommentReply(comment.id)">수정하기</p>|
              <!-- 댓글 삭제 버튼 -->
              <p class="button" @click="deleteCommentReply(comment.id)">삭제하기</p>
            </div>
          </div>
          
          <!-- 댓글 좋아요 버튼 -->
          <button
            :class="{ 'like-button': true, 'liked': isLiked(comment.like_users, store.currentUser.user_id) }"
            @click="toggleLike(comment.user, comment.id)">
            👍
            {{ comment.like_users ? comment.like_users.length : 0 }}
          </button>
         
          <hr class="comment-divider">
          
          <!----------------------------- 답글 목록 시작 ----------------------------->
          <ul class="reply-list">
            <div v-for="reply in comment.replies" :key="reply.id">
              <div class="comment-container">
                <div class="comment-info">
                  <h4>{{ reply.user_nickname }}</h4>
                  <p class="comment-time">({{ formatCommentTime(reply.created_at) }})</p>
                </div>

                <p class="comment-content">{{ reply.content }}</p>

                <!-- 내가 작성한 답글만 수정/삭제 버튼 존재 -->
                <div v-if="store.currentUser.user_id === reply.user" class="my-buttons">
                  <!-- 답글 수정 버튼 -->
                  <p class="button" @click="editCommentReply(comment.id, reply.id)">수정하기</p>|
                  <!-- 답글 삭제 버튼 -->
                  <p class="button" @click="deleteCommentReply(comment.id, reply.id)">삭제하기</p>
                </div>

                <!-- 답글 좋아요 버튼 -->
                <button
                  :class="{ 'like-button': true, 'liked': isLiked(reply.like_users, store.currentUser.user_id) }"
                  @click="toggleLike(reply.user, comment.id, reply.id)">
                  👍
                  {{ reply.like_users ? reply.like_users.length : 0 }}
                </button>
              </div>
              <hr class="comment-divider">
            </div>
          </ul>
          <!----------------------------- 답글 목록 끝 ----------------------------->

        </div>
      </ul>
    </div>
    <div v-else>
      <hr class="comment-divider">
      <p>댓글이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const activeReplyForm = ref(null)  // 열린 답글 폼의 comment.id를 저장
const newReply = ref('')           // 댓글 별로 새로 작성할 답글 내용

onMounted(() => {
  // 게시글 데이터 가져오기
  store.getArticle(route.params.id)
})

const formatCommentTime = (timestamp) => {
  const currentDate = new Date()
  const commentDate = new Date(timestamp)
  const elapsedMillis = currentDate - commentDate;
  const elapsedMinutes = Math.floor(elapsedMillis / (60 * 1000))
  const elapsedHours = Math.floor(elapsedMillis / (60 * 60 * 1000))

  if (elapsedMinutes < 1) {
    return '방금 전';
  } else if (elapsedMinutes < 60) {
    return `${elapsedMinutes}분 전`
  } else if (elapsedHours < 24) {
    return `${elapsedHours}시간 전`
  } else {
    return `${commentDate.getFullYear()}-${String(commentDate.getMonth() + 1).padStart(2, '0')}-${String(commentDate.getDate()).padStart(2, '0')} ${String(commentDate.getHours()).padStart(2, '0')}:${String(commentDate.getMinutes()).padStart(2, '0')}`
  }
}

const editCommentReply = (commentId, replyId=0) => {
  // 댓글/답글 수정
  const updatedContent = prompt('뭐라고 수정할건데?', '')
  const url = replyId
    ? `${store.API_URL}/community/comments/${commentId}/${replyId}/`
    : `${store.API_URL}/community/articles/${route.params.id}/${commentId}/`

  if (updatedContent !== null) {
    axios({
      method: 'put',
      url,
      data: {
        content: updatedContent,
      },
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then(() => {
        // 게시글 데이터 가져오기
        store.getArticle(route.params.id)
      })
      .catch((err) => {
        console.error('댓글 수정 에러:', err)
      })
  }
}

const deleteCommentReply = (commentId, replyId=0) => {
  // 댓글/답글 삭제
  const confirmDelete = confirm('진짜 지울거임? 쫄보처럼?')

  const url = replyId
    ? `${store.API_URL}/community/comments/${commentId}/${replyId}/`
    : `${store.API_URL}/community/articles/${route.params.id}/${commentId}/`

  if (confirmDelete) {
    axios({
      method: 'delete',
      url,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then(() => {
        // 게시글 데이터 가져오기
        store.getArticle(route.params.id)
      })
      .catch((err) => {
        console.error('댓글 삭제 에러:', err)
      })
  }
}

const isLiked = (likeUsers, userId) => {
  return likeUsers && likeUsers.includes(userId);
}

const toggleLike = (userId, commentId, replyId=0) => {
  // 댓글/답글 좋아요/좋아요 취소 요청 보내기
  if (userId === store.currentUser.user_id) {
    alert('자추는 안되지 아 ㅋㅋ')
    return
  }

  const url = replyId
    ? `${store.API_URL}/community/like/reply/${replyId}/`
    : `${store.API_URL}/community/like/comment/${commentId}/`

  axios({
    method: 'post',
    url,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      // 좋아요/좋아요 취소 요청이 성공하면 게시글 데이터를 다시 불러와 갱신
      store.getArticle(route.params.id)
    })
    .catch((err) => {
      console.error('좋아요 토글 에러:', err)
    })
}

const toggleReplyForm = (commentId) => {
  // 댓글 별로 답글 폼 토글
  activeReplyForm.value = activeReplyForm.value === commentId ? null : commentId

  // 답글 폼을 토글할 때마다 내용 초기화
  if (!activeReplyForm.value) {
    newReply.value = ''
  }
}

const createReply = (commentId) => {
  // 새로운 답글 작성
  axios({
    method: 'post',
    url: `${store.API_URL}/community/comments/${commentId}/replies/`,
    data: {
      content: newReply.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      // 답글 작성 후에는 입력 필드 초기화
      newReply.value = ''
      store.getArticle(route.params.id)
      activeReplyForm.value = activeReplyForm.value === commentId ? null : commentId
    })
    .catch((err) => {
      console.log('답글 생성 에러:', err)
    })
}
</script>

<style scoped>
.comment-info {
  display: flex;
  align-items: center; /* 세로 중앙 정렬을 위해 추가 */
}

.comment-info h4 {
  margin-right: 8px; /* 작성자와 content 사이의 간격 조절 */
}

.comment-time {
  margin-left: 8px; /* 작성일과 작성자 사이의 간격 조절 */
  font-size: 0.8em; /* 작성일 폰트 크기 조절 */
  color:#3498db;
}

.comment-content {
  margin-top: 15px; /* content 위쪽 간격 조절 */
  min-height: 80px;
}

.comment-container {
  margin-bottom: 20px;
  padding: 10px;
  position: relative; /* 상대적인 위치 설정 */
}

.like-button {
  position: absolute; /* 절대적인 위치 설정 */
  color: black;
  padding: 8px 8px;
  top: 10px; /* 상단에 위치시킴 */
  right: 10px; /* 오른쪽에 위치시킴 */
  border-radius: 5px;
  border: 1px solid #ddd; /* 테두리 추가 */
  background-color: #ddd;
  transition: border-color 0.3s;
  cursor: pointer;
}

.like-button.liked {
  background-color: #e74c3c; /* 좋아요 눌렀을 때의 배경색 */
  color: #fff; /* 좋아요 눌렀을 때의 글자색 */
}

.like-button:hover {
  border-color: black; /* 호버 시 테두리 색상 변경 */
}

.comment-divider {
  margin-top: 20px; /* hr 위쪽 여백 설정 */
  margin-bottom: 20px; /* hr 아래쪽 여백 설정 */
  border: none; /* 기존 border 제거 */
  border-top: 1px solid #ddd; /* 새로운 연한 회색 border 추가 */
}

.reply-list {
  list-style-type: none;
  padding: 0;
}

.reply-list .comment-container {
  margin-left: 20px; /* 답글 목록은 좀 더 들여쓰기 */
  background-color: #f2f2f2; 
}

.buttons {
  display: flex;
}

.my-buttons {
  display: flex;
  margin-left: auto; /* 현재 위치에서 오른쪽으로 이동하도록 설정 */
  justify-content: flex-end
}

.button {
  margin-left: 10px;
  margin-right: 10px;
  cursor: pointer;  /* 마우스 올리면 손가락 형태로 변경 */
}

.reply-form {
  width: 100%;
  background-color: #f2f2f2;
  padding: 20px;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
}

.reply-area {
  display: flex;
  gap: 20px;
}

.reply-textarea {
  flex: 1;
}

.submit-button {
  background-color: #4CAF50;
  width: 60px;
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
