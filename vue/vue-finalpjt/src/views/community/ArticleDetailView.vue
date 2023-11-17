<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
      <p>좋아요 수 : {{ article.likes_users }}</p>
    </div>

    <!-- 좋아요 버튼 -->
    <button @click="likeArticle" v-if="article && !article.liked">좋아요</button>
    <button @click="unlikeArticle" v-if="article && article.liked">좋아요 취소</button>
    <br>

    <RouterLink v-if="article" :to="{ name: 'ArticleEditView', params: { id: article.id }}">
      [글 수정]
    </RouterLink>

    <!-- 삭제 버튼 -->
    <button @click="deleteArticle" v-if="article">[글 삭제]</button>

    <!-- 댓글 section 컴포넌트 -->
    <CommentSection :article="article"/>
  </div>
</template>

<script setup>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
import CommentSection from '@/components/community/CommentSection.vue'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  // 게시글 데이터 가져오기
  axios({
    method: 'get',
    url: `${store.API_URL}/community/articles/${route.params.id}/`
  })
    .then((res) => {
      article.value = res.data
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
})

const likeArticle = () => {
  // 게시글 좋아요 요청 보내기
  axios({
    method: 'post',
    url: `${store.API_URL}/community/articles/${route.params.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      // 좋아요 요청이 성공하면 게시글 데이터를 다시 불러와 갱신
      loadArticle()
    })
    .catch((error) => {
      console.error('좋아요 에러:', error)
    })
}

const unlikeArticle = () => {
  // 게시글 좋아요 취소 요청 보내기
  axios({
    method: 'delete',
    url: `${store.API_URL}/community/articles/${route.params.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      // 좋아요 취소 요청이 성공하면 게시글 데이터를 다시 불러와 갱신
      loadArticle()
    })
    .catch((error) => {
      console.error('좋아요 취소 에러:', error)
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
      this.$router.push({ name: 'CommunityView' })
      console.log('Article deleted successfully')
    })
    .catch((err) => {
      console.log(err)
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