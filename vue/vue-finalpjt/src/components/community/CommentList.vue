<template>
  <div>
    <div v-if="store.article && store.article.comments && store.article.comments.length > 0">
      <h2>댓글 목록</h2>
      <ul>
        <li v-for="comment in store.article.comments" :key="comment.id">
          <p>작성자 : {{ comment.user_nickname }}</p>
          <p>작성일 : {{ comment.created_at }}</p>
          <p>{{ comment.content }}</p>

          <!-- 내가 작성한 댓글만 수정/삭제 버튼 존재 -->
          <div v-if="store.currentUser.user_id === comment.user">
            <!-- 댓글 수정 버튼 -->
            <button @click="editCommentReply(comment.id)">수정</button>
            <!-- 댓글 삭제 버튼 -->
            <button @click="deleteCommentReply(comment.id)">삭제</button>
          </div>

          <!-- 답글 버튼 -->
          <button @click="toggleReplyForm(comment.id)">답글</button>

          <!-- 답글 작성 폼 -->
          <div v-if="activeReplyForm === comment.id">
            <textarea v-model.trim="newReply" id="reply"></textarea>
            <button @click="createReply(comment.id)">등록</button>
          </div>
          
          <!-- 댓글 좋아요 버튼 -->
          <button @click="toggleLike(comment.user, comment.id)">
            {{ comment.like_users && comment.like_users.includes(store.currentUser.user_id) ? '좋아요 취소' : '좋아요' }}
            {{ comment.like_users ? comment.like_users.length : 0 }}
          </button>
          <br>
          
          <!----------------------------- 답글 목록 시작 ----------------------------->
          <ul>
            <li v-for="reply in comment.replies" :key="reply.id">
              <div>(답글)</div>
              <div>
                <p>작성자 : {{ reply.user_nickname }}</p>
                <p>작성일 : {{ reply.created_at }}</p>
                <p>{{ reply.content }}</p>

                <!-- 내가 작성한 답글만 수정/삭제 버튼 존재 -->
                <div v-if="store.currentUser.user_id === reply.user">
                  <!-- 답글 수정 버튼 -->
                  <button @click="editCommentReply(comment.id, reply.id)">수정</button>
                  <!-- 답글 삭제 버튼 -->
                  <button @click="deleteCommentReply(comment.id, reply.id)">삭제</button>
                </div>

                <!-- 답글 좋아요 버튼 -->
                <button @click="toggleLike(reply.user, comment.id, reply.id)">
                  {{ reply.like_users && reply.like_users.includes(store.currentUser.user_id) ? '좋아요 취소' : '좋아요' }}
                  {{ reply.like_users ? reply.like_users.length : 0 }}
                </button>
              </div>
            </li>
          </ul>
          <!----------------------------- 답글 목록 끝 ----------------------------->

        </li>
      </ul>
    </div>
    <div v-else>
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

const editCommentReply = (commentId, replyId=0) => {
  // 댓글/답글 수정
  const updatedContent = prompt('수정하세요:', '')
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
  const confirmDelete = confirm('정말로 삭제하시겠습니까?')

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

const toggleLike = (userId, commentId, replyId=0) => {
  // 댓글/답글 좋아요/좋아요 취소 요청 보내기
  if (userId === store.currentUser.user_id) {
    alert('니가 쓴 글인데..? 양심좀')
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
    })
    .catch((err) => {
      console.log('답글 생성 에러:', err)
    })
}
</script>

<style scoped>

</style>
