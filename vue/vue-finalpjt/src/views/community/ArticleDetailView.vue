<template>
  <div>
    <h1>Detail</h1>
    <div v-if="store.article">
      <p>제목 : {{ store.article.title }}</p>
      <p>내용 : {{ store.article.content }}</p>
      <p>작성일 : {{ store.article.created_at }}</p>
      <p>수정일 : {{ store.article.updated_at }}</p>
      <p>좋아요 수 : {{ store.article.likes_users }}</p>
    </div>

    <!-- 좋아요 버튼 -->
    <button @click="toggleLike" v-if="store.article">
      {{ store.article.liked ? '좋아요 취소' : '좋아요' }}
    </button>
    <br>

    <RouterLink v-if="store.article" :to="{ name: 'ArticleEditView', params: { id: store.article.id }}">
      [글 수정]
    </RouterLink>

    <!-- 삭제 버튼 -->
    <button @click="deleteArticle" v-if="store.article">[글 삭제]</button>

    <!-- 댓글 section 컴포넌트 -->
    <CommentSection />
  </div>
</template>

<script setup>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommentSection from '@/components/community/CommentSection.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()

onMounted(() => {
  // 게시글 데이터 가져오기
  store.getArticle(route.params.id)
})

const toggleLike = () => {
  const isLiked = store.LikedArticles()
  // 게시글 좋아요/좋아요 취소 요청 보내기
  axios({
    method: 'post',
    url: `${store.API_URL}/community/articles/${route.params.id}/like/`,
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

const deleteArticle = () => {
  // 게시글 삭제
  axios({
    method: 'delete',
    url: `${store.API_URL}/community/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      // 삭제가 성공하면 홈 화면으로 이동
      router.push({ name: 'CommunityView' })
      console.log('Article deleted successfully')
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>