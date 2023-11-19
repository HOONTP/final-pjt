<template>
  <div>
    <div v-if="store.article && store.article.comments.length > 0">
      <h2>댓글 목록</h2>
      <ul>
        <li v-for="comment in store.article.comments" :key="comment.id">
          <p>{{ comment.content }}</p>
          <p>작성일 : {{ comment.created_at }}</p>
            <!-- 수정 버튼 -->
            <button @click="editComment(comment.id)">수정</button>
            <!-- 삭제 버튼 -->
            <button @click="deleteComment(comment.id)">삭제</button>
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
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()

onMounted(() => {
  // 게시글 데이터 가져오기
  store.getArticle(route.params.id)
})

const editComment = (commentId) => {
  // 댓글 수정
  const updatedContent = prompt('댓글을 수정하세요:', '')

  if (updatedContent !== null) {
    axios({
      method: 'put',
      url: `${store.API_URL}/community/comments/${commentId}/`,
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

const deleteComment = (commentId) => {
  // 댓글 삭제
  const confirmDelete = confirm('정말로 이 댓글을 삭제하시겠습니까?')

  if (confirmDelete) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/community/comments/${commentId}/`,
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
</script>

<style scoped>

</style>
