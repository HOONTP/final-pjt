<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />

    <div class="container">
      <form @submit.prevent="updateArticle" class="form-container">
        <h2>게시글 수정</h2>
        <div class="form-group">
          <label for="title">제목:</label>
          <input 
            type="text" 
            v-model.trim="title" 
            id="title" 
            class="input-field" 
            placeholder="제목을 입력하세요"
          >
        </div>
        <div class="form-group">
          <label for="content"></label>
          <textarea 
            v-model.trim="content" 
            id="content" 
            class="textarea-field" 
            placeholder="내용을 입력하세요"
            rows="10"
          ></textarea>
        </div>
        <div class="button-container">
          <button type="submit" class="submit-button">수정하기</button>
          <button @click="cancelArticle" class="cancel-button">취소하기</button>
        </div>
      </form>
    </div>
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
.container {
  margin: 0 5%;
  margin-top: 120px;
}

.form-container {
  width: 50%;
  margin: auto;
  min-width: 600px; /* 예시로 설정한 최소 너비 */
  max-width: 800px; /* 예시로 설정한 최대 너비 */
}

.form-group {
  margin-top: 30px;
  margin-bottom: 20px;
}

.input-field,
.textarea-field {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
  margin-top: 5px;
  margin-bottom: 10px;
}

.input-field::placeholder,
.textarea-field::placeholder {
  color: #aaa;
}

.button-container {
  text-align: center;
  margin-top: 20px;
}

.submit-button,
.cancel-button {
  background-color: #4CAF50;
  color: white;
  padding: 8px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 5px; 
  transition: background-color 0.3s;
  cursor: pointer;
  margin-left: 5px;
  margin-right: 5px;
  border: none;
}

.submit-button:hover {
  background-color: #45a049;
}

.cancel-button:hover {
  background-color: #bbb;
}

.cancel-button {
  background-color: #ccc;
  color: #333;
}
</style>
