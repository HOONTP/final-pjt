<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <select name="board" v-model="community_pk">
          <option value="1">전체</option>
          <option value="2">인기</option>
          <option value="3">리뷰</option>
          <option value="4">자유</option>
        </select>
      </div>
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit" value="작성하기">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const community_pk = ref("1")  // 초기값 설정
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/community/${community_pk.value}/articles/${0}/`,
    data: {
      title: title.value,
      content: content.value,
      board: community_pk.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      router.push({ name: 'CommunityView' })
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>

</style>
