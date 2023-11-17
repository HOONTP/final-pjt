<template>
  <div>
    <!-- 댓글 list 컴포넌트 -->
    <CommentList :article="article" @load-article="loadArticle"/>

    <!-- 댓글 작성 폼 -->
    <div>
      <label for="comment">댓글 작성:</label>
      <textarea v-model.trim="newComment" id="comment"></textarea>
      <button @click="createComment">댓글 작성</button>
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
const article = ref(null)  // article 초기화

defineProps({
  article: Object
})

onMounted(() => {
  // 게시글 초기화
  if (article.value === null) {
    loadArticle()
  }
})

const createComment = () => {
  // 새로운 댓글 작성
  axios({
    method: 'post',
    url: `${store.API_URL}/community/articles/${route.params.id}/comments/`,
    data: {
      content: newComment.value,
      article: route.params.id
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      // 댓글 작성 후에는 입력 필드 초기화
      newComment.value = ''
      loadArticle()
    })
    .catch((err) => {
      console.log('댓글 생성 에러:', err)
    })
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
      article.value = res.data
    })
    .catch((err) => {
      console.error('게시글 불러오기 에러:', err)
    })
}
</script>

<style scoped>

</style>
