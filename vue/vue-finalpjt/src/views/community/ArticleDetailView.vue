<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />
    
    <div class="container">
      <div class="detail">
        <h2>{{ getBoardType(store.article.board) }} 게시판</h2>

        <div v-if="store.article">
          <h1>{{ store.article.title }}</h1>

          <div class="article_info">
            <div class="profile_img">
              <p>[프로필 사진]</p>
            </div>
            <div class="user_info">
              <h4>{{ store.article.user_nickname }}</h4>
              <p class="timestamp">
                작성일: {{ formatDateTime(store.article.created_at) }} 
                <span class="time-ago">{{ formatTimestamp(store.article.created_at) }}</span>
              </p>
              <p class="timestamp">
                수정일: {{ formatDateTime(store.article.updated_at) }} 
                <span class="time-ago">{{ formatTimestamp(store.article.updated_at) }}</span>
              </p>
            </div>
          </div>

          <p class="content">{{ store.article.content }}</p>

        </div>

        <!-- 좋아요 버튼 -->
        <button
          :class="{ 'like-button': true, 'liked': isLiked(store.article.like_users, store.currentUser.user_id) }"
          @click="toggleLike">
          👍
          {{ store.article.like_users ? store.article.like_users.length : 0 }}
        </button>
        <br>

        <!-- 내가 작성한 게시글만 수정/삭제 버튼 존재 -->
        <div v-if="store.currentUser.user_id === store.article.user" class="buttons">
          <!-- 수정 버튼 -->
          <RouterLink
            v-if="store.article"
            class="edit-button"
            :to="{
              name: 'ArticleEditView',
              // params: { id: store.article.id },
            }">
            수정하기
          </RouterLink>|
          
          <!-- 삭제 버튼 -->
          <p
            @click="deleteArticle"
            v-if="store.article"
            class="delete-button">
            삭제하기
          </p>
        </div>
      </div>

      <!-- 댓글 section 컴포넌트 -->
      <CommentSection />
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommunityNav from '@/components/community/CommunityNav.vue'
import CommentSection from '@/components/community/CommentSection.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()

onMounted(() => {
  // 게시글 데이터 가져오기
  if (route) {
  store.getArticle(route.params.id)
  }
})

const formatDateTime = (timestamp) => {
  const createdDate = new Date(timestamp)
  const year = createdDate.getFullYear()
  const month = String(createdDate.getMonth() + 1).padStart(2, '0')
  const day = String(createdDate.getDate()).padStart(2, '0')
  const hours = String(createdDate.getHours()).padStart(2, '0')
  const minutes = String(createdDate.getMinutes()).padStart(2, '0')

  return `${year}년 ${month}월 ${day}일 ${hours}:${minutes}`
};

const formatTimestamp = (timestamp) => {
  const now = new Date()
  const createdDate = new Date(timestamp)
  const elapsedMillis = now - createdDate
  const elapsedMinutes = Math.floor(elapsedMillis / (60 * 1000))
  const elapsedHours = Math.floor(elapsedMillis / (60 * 60 * 1000))

  if (elapsedMinutes < 1) {
    return '(방금 전)';
  } else if (elapsedMinutes < 60) {
    return `(${elapsedMinutes}분 전)`
  } else if (elapsedHours < 24) {
    return `(${elapsedHours}시간 전)`
  }
}

const isLiked = (likeUsers, userId) => {
  return likeUsers && likeUsers.includes(userId)
}

const toggleLike = () => {
  // 게시글 좋아요/좋아요 취소 요청 보내기
  axios({
    method: 'post',
    url: `${store.API_URL}/community/like/article/${route.params.id}/`,
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
      router.push({ name: 'CommunityTotalView' })
      console.log('Article deleted successfully')
    })
    .catch((err) => {
      console.log(err)
    })
}

const getBoardType = (board) => {
  switch (board) {
    case 1:
      return '전체';
    case 2:
      return '인기';
    case 3:
      return '리뷰';
    case 4:
      return '자유';
    default:
      return '';
  }
}
</script>

<style scoped>
.container {
  margin: 0 5%;
  margin-top: 120px;
}

.detail {
  width: 60%;
  min-width: 800px; /* 예시로 설정한 최소 너비 */
  max-width: 1200px; /* 예시로 설정한 최대 너비 */
  margin: auto;
  margin-top: 30px;
  margin-bottom: 20px;
}

.article_info {
  display: flex;
  margin-top: 30px;
  margin-bottom: 20px;
  background-color: #f2f2f2; /* 연한 회색 배경색 */
  padding: 10px; /* 내부 여백 */
  border-radius: 5px; /* 둥근 테두리 적용*/
}

.profile_img {
  background-color: #d9d9d9; /* 프로필 사진 배경색 */
  padding: 10px; /* 내부 여백 */
  border-radius: 5px; /* 둥근 테두리 적용 */
  margin-right: 10px; /* 프로필 사진과 사용자 정보 사이 간격 조절 */
}
h2 {
  margin-bottom: 30px;
}

h4 {
  margin-bottom: 10px;
}

.user_info {
  display: flex;
  flex-direction: column;
}

.timestamp {
  font-size: 0.8em; /* 작성일과 수정일 폰트 크기 조절 */
  margin: 5px 0; /* 간격 조절 */
}

.time-ago {
  color: #3498db; /* 연한 파란색 */
}

.content {
  margin-top: 30px;
  margin-bottom: 10px;
  font-size: 1.5em;
  height: 300px; /* 높이 설정 */
  overflow-y: auto; /* 세로 스크롤 추가 */
}

.like-button {
  background-color: #ddd;
  color: black;
  padding: 10px 40px;
  border: 1px solid #ddd; /* 테두리 추가 */
  border-radius: 30px;
  cursor: pointer;
  font-size: 1.3em;
  margin: 0 auto; /* 가운데 정렬을 위한 margin 추가 */
  display: block; /* Full width로 표시되도록 변경 */
  transition: border-color 0.3s;
}

.like-button.liked {
  background-color: #e74c3c; /* 좋아요 눌렀을 때의 배경색 */
  color: #fff; /* 좋아요 눌렀을 때의 글자색 */
}

.like-button:hover {
  border-color: black; /* 호버 시 테두리 색상 변경 */
}

.buttons {
  display: flex;
  justify-content: flex-end;
}

.edit-button {
  margin-left: 10px;
  margin-right: 10px;
  color: black;
  text-decoration: none; /* 링크 텍스트에 밑줄 제거 */
  font-size: 1em;
}

.delete-button {
  margin-left: 10px;
  margin-right: 10px;
  cursor: pointer;  /* 마우스 올리면 손가락 형태로 변경 */
}

</style>