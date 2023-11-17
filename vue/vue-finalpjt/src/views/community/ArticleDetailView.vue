<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
    </div>

    <RouterLink v-if="article" :to="{ name: 'ArticleEditView', params: { id: article.id }}">
      [글 수정]
    </RouterLink>

    <!-- 댓글 목록 표시 -->
    <div v-if="article">
    <div v-if="article.comments.length > 0">
      <h2>댓글 목록</h2>
      <ul>
        <li v-for="comment in article.comments" :key="comment.id">
          <p>{{ comment.content }}</p>
          <p>작성일 : {{ comment.created_at }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>댓글이 없습니다.</p>
    </div>
    </div>


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
import { RouterLink } from 'vue-router'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)
const comments = ref([])  // 댓글 목록을 담을 배열
const newComment = ref('')  // 새로 작성할 댓글을 담을 변수

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

// 댓글 목록 가져오기
  // axios({
  //   method: 'get',
  //   url: `${store.API_URL}/api/v1/comments/?article=${route.params.id}`
  // })
  //   .then((res) => {
  //     comments.value = res.data
  //   })
  //   .catch((err) => {
  //     console.log(err)
  //   })
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
    .then((res) => {
      // 작성이 성공하면 댓글 목록을 다시 불러와 갱신
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

      // 댓글 작성 후에는 입력 필드 초기화
      newComment.value = ''
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>