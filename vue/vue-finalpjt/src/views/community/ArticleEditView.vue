<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />

    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit" value="수정하기">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'
import CommunityNav from '@/components/community/CommunityNav.vue'

const title = ref('')
const content = ref('')
const store = useCounterStore()
const route = useRoute()
const router = useRouter()

// 게시글 ID를 라우터 파라미터에서 가져오기
const articleId = ref(route.params.id)

// 게시글 내용을 가져오는 함수
const fetchArticle = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/community/articles/${articleId.value}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // 기존 게시글 내용을 가져와서 폼에 채우기
      title.value = res.data.title
      content.value = res.data.content
    })
    .catch((err) => {
      console.log(err)
    })
}

// 컴포넌트가 마운트된 후 게시글 내용 가져오기
onMounted(() => {
  fetchArticle()
})

const updateArticle = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/community/articles/${articleId.value}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      router.push({ name: 'ArticleDetailView' })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>
