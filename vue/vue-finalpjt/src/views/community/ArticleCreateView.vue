<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />
    
    <div class="container">
      <h2>새로운 글 등록</h2>
      <form @submit.prevent="createArticle" class="form-container">
        <div class="form-group">
          <label for="board">게시판:</label>
          <select name="board" v-model="community_pk" class="select-board">
            <option value="1">전체</option>
            <option value="2">인기</option>
            <option value="3">리뷰</option>
            <option value="4">자유</option>
          </select>
        </div>
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
          <button type="submit" class="submit-button">작성완료</button>
          <button @click="cancelArticle" class="cancel-button">취소하기</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter,  } from 'vue-router'
import CommunityNav from '@/components/community/CommunityNav.vue'

const store = useCounterStore()
const router = useRouter()
const title = ref(null)
const content = ref(null)
const community_pk = ref(store.articles[0].board)

// const getBoardType = (community_pk) => {
//   switch (community_pk) {
//     case 1:
//       return 'CommunityTotalView'
//     case 2:
//       return 'CommunityHotView'
//     case 3:
//       return 'CommunityReviewView'
//     case 4:
//       return 'CommunityFreeView'
//     default:
//       return ''
//   }
// }

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/community/${community_pk.value}/articles/0/`,
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
      router.go(-1)
    })
    .catch((err) => {
      console.log(err)
    })
}

const cancelArticle = function () {
  // 이전 페이지로 이동
  router.go(-1)
}

</script>

<style scoped>
.container {
  margin: 0 20px;
  margin-top: 120px;
}

.form-container {
  width: 80%;
  margin: auto;
}

.form-group {
  margin-top: 30px;
  margin-bottom: 20px;
}

.select-board,
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
