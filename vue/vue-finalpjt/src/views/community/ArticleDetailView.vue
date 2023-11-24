<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />
    
    <div class="container">
      <div class="detail" v-if="store.article.id">
        <h2>{{ getBoardType(store.article.board) }} 게시판</h2>

        <div v-if="store.article">
          <h1>{{ store.article.title }}</h1>
          <div class="article_info">
            <div class="profile-picture">
              <!-- v-if="store.profile.data.profile_image" -->
              <img
                v-if="store.article.profile_image"
                :src="store.API_URL+'/media/'+store.article.profile_image"
                alt="프로필 사진"
                class="profile-image"
                :key="store.article.profile_image"
                @click="navigateToProfile(store.article.user)"
              />
            </div>
            <div class="user_info">
              <div class="info-top">
                <p @click="navigateToProfile(store.article.user)" class="nickname">
                  {{ store.article.user_nickname }}
                </p>
                <p>조회수: {{ store.article.counting }}</p>
              </div>
              <div>
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
          </div>

          <p class="content">{{ store.article.content }}</p>

        </div>

        <!-- 좋아요 버튼 -->
        <button
          :class="{ 'like-button': true, 'liked': isLiked(store.article.like_users, store.currentUser.user_id) }"
          @click="toggleLike(store.article.user)">
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
            @click="confirmDelete"
            v-if="store.article"
            class="delete-button">
            삭제하기
          </p>
        </div>
      </div>
      <!-- 비로그인 시 -->
      <div v-else>
        <p class="login-message">로그인이 필요합니다.</p>
      </div>
      <!-- 댓글 section 컴포넌트 -->
      <CommentSection />
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommunityNav from '@/components/community/CommunityNav.vue'
import CommentSection from '@/components/community/CommentSection.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()

onMounted( () => {
  if (route) {
    try {
      // 게시글을 가져오기
      store.getArticle(route.params.id);
      console.log(store.article); // 새로운 게시글의 정보가 출력되어야 함
    } catch (err) {
      console.error(err);
    }
  }
  // ;
});

const onIdChange = (newId, oldId) => {
  console.log('새로운 글 ID:', newId);
  // id가 변경될 때 필요한 다른 작업을 수행하세요.
  store.getArticle(route.params.id)
  }

watch(() => route.params.id, onIdChange, { immediate: true });

const navigateToProfile = (userId) => {
  router.push({ name: 'ProfileView', params: { nickName: userId } })
}

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

const toggleLike = (userId) => {
  // 게시글 좋아요/좋아요 취소 요청 보내기

  if (userId === store.currentUser.user_id) {
    alert('니가 쓴 글인데..? 양심좀')
    return
  }

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

const confirmDelete = () => {
  // window.confirm을 사용하여 사용자에게 확인을 받음
  const isConfirmed = window.confirm('우리의 추억을... 정말 지워버릴거니..?')

  // 확인이면 삭제 수행
  if (isConfirmed) {
    deleteArticle()
  }
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
      return '코딩'
    case 2:
      return '유머'
    case 3:
      return '리뷰'
    case 4:
      return '자유'
    default:
      return ''
  }
}
</script>

<style scoped>
.container {
  margin-top: 120px;
}

.profile-picture {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 150px;
  height: 150px;
  padding: 10px; /* 내부 여백 */
  border-radius: 5px; /* 둥근 테두리 적용 */
  margin-right: 10px; /* 프로필 사진과 사용자 정보 사이 간격 조절 */
  overflow: hidden;
}

.profile-image {
  /* width: 100%; */
  width: auto;
  height: 100%;
  border-radius: 50%; /* 원형 프로필 이미지를 위해 반지름 50% 설정 */
  cursor: pointer;  /* 마우스 올리면 손가락 형태로 변경 */
}

.detail {
  min-width: 800px; /* 예시로 설정한 최소 너비 */
  max-width: 800px; /* 예시로 설정한 최대 너비 */
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
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  margin-bottom: 30px;
}

.nickname {
  font-weight: bold;
  font-size: 30px;
  margin-bottom: 10px;
  cursor: pointer;  /* 마우스 올리면 손가락 형태로 변경 */
}

.user_info {
  display: flex;
  flex-direction: column;
  width: 100%;
  justify-content: space-between;
}

.info-top {
  display: flex;
  justify-content: space-between;
  margin-right: 50px;
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
  min-height: 300px; /* 높이 설정 */
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

.login-message {
    font-size: 30px; /* 원하는 크기로 조절 */
    /* 추가적인 스타일링을 원하면 여기에 추가 */
  }
</style>