<template>
  <div>
    <div v-if="article && article.comments.length > 0">
      <h2>댓글 목록</h2>
      <ul>
        <li v-for="comment in article.comments" :key="comment.id">
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
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)  // article 초기화
const emit = defineEmits(['loadArticle'])

defineProps({
  article: Object
})

onMounted(() => {
  // 게시글 초기화
  if (!article.value) {
    loadArticle()
  }
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
        // 수정된 댓글 정보를 부모에게 전달
        emit('loadArticle', { ...article.value })
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
        // 삭제된 댓글 정보를 부모에게 전달
        emit('loadArticle', { ...article.value })
      })
      .catch((err) => {
        console.error('댓글 삭제 에러:', err)
      })
  }
}

const loadArticle = () => {
  // 게시글 갱신
  axios({
    method: 'get',
    url: `${store.API_URL}/community/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      // 게시글을 부모에게 전달
      emit('loadArticle', res.data)
    })
    .catch((err) => {
      console.error('게시글 불러오기 에러:', err)
    })
}
</script>

<style scoped>

</style>
