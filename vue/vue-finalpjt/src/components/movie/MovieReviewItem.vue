<template>
  <div>
    <div v-for="review in store.movie.reviews" :key="review.id">
      <div class="user">
        <!-- {{ review }} -->
        <div class="profile-picture">
          <img
            v-if="review.profile_image"
            :src="store.API_URL+'/media/'+review.profile_image"
            alt="프로필 사진"
            class="profile-image"
            @click="navigateToProfile(review.user)"
          />
        </div>
        <div class="review-item">
          <p class="nickname" @click="navigateToProfile(review.user)">{{ review.user_nickname }}</p>
          <!-- ⭐⭐⭐⭐⭐ -->
          <p class="content">{{ review.content }}</p>
        </div>
          <!-- 내가 작성한 리뷰만 삭제 버튼 존재 -->
          <div v-if="store.currentUser.user_id === review.user" class="my-buttons">
            <p class="button" @click="deleteCommentReview(review.id)">삭제하기</p>
          </div>
            <!-- 리뷰 좋아요 버튼 -->
          <button
            v-else
            :class="{ 'like-button': true, 'liked': isLiked(review.like_users, store.currentUser.user_id) }"
            @click="toggleLike(review.id)">
            👍
            {{ review.like_users ? review.like_users.length : 0 }}
          </button>
      </div>
      <hr class="hr">
    </div>
    <p v-if="store.movie.reviews.length === 0" class="no-review">
      리뷰가 없습니다.
    </p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const movieId = route.params.id
const router = useRouter()

onMounted(async () => {
  store.getMovie(movieId)
  // store.getMovieReview(movieId)

  // try {
  //   await store.getProfile(store.movie.user)
  // } catch (err) {
  //   console.error(err)
  // }
})

const navigateToProfile = (userId) => {
  router.push({ name: 'ProfileView', params: { nickName: userId } })
}

const deleteCommentReview = (moviePk) => {
  // 리뷰 삭제
  const confirmDelete = confirm('재밌게 잘 봐놓고 리뷰도 안씀?ㅋㅋ')

  if (confirmDelete) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/movies/reviews/${moviePk}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then(() => {
        // 게시글 데이터 가져오기
        store.getMovie(movieId)
        // store.getMovieReview(movieId)
      })
      .catch((err) => {
        console.error('댓글 삭제 에러:', err)
      })
  }
}

const isLiked = (likeUsers, userId) => {
  return likeUsers && likeUsers.includes(userId);
}

const toggleLike = (reviewId) => {
  axios({
    method: 'post',
    url: `${store.API_URL}/movies/reviews/${reviewId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      store.getMovie(movieId)
      // store.getMovieReview(movieId)
    })
    .catch((err) => {
      console.error('좋아요 토글 에러:', err)
    })
}

</script>

<style scoped>
.user {
  display: flex;
  align-items: center;
}

.profile-picture {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px;
  height: 80px;
  padding: 10px; /* 내부 여백 */
  border-radius: 5px; /* 둥근 테두리 적용 */
  margin-right: 10px; /* 프로필 사진과 사용자 정보 사이 간격 조절 */
  overflow: hidden;
}

.profile-image {
  width: auto;
  height: 100%;
  border-radius: 50%; /* 원형 프로필 이미지를 위해 반지름 50% 설정 */
  cursor: pointer;  /* 마우스 올리면 손가락 형태로 변경 */
}

.nickname {
  color: white;
  font-weight: bold;
  cursor: pointer;  /* 마우스 올리면 손가락 형태로 변경 */
}

.content {
  color: rgb(132, 134, 141);
}

.hr {
  margin-top: 10px; /* hr 위쪽 여백 설정 */
  margin-bottom: 10px; /* hr 아래쪽 여백 설정 */
  border: none; /* 기존 border 제거 */
  border-top: 1px solid #ddd; /* 새로운 연한 회색 border 추가 */
}

.my-buttons {
  display: flex;
  margin-left: auto; /* 현재 위치에서 오른쪽으로 이동하도록 설정 */
  justify-content: flex-end
}

.button {
  margin-right: 20px;
  color: white;
  cursor: pointer;  /* 마우스 올리면 손가락 형태로 변경 */
}

.no-review {
  color: rgb(124, 123, 132);
}

.like-button {
  margin-left: auto;
  margin-right: 20px;
  color: black;
  padding: 8px 8px;
  border-radius: 20%;
  border: none;
  background-color: #ddd;
  transition: background-color 0.3s;
  cursor: pointer;
}

.like-button.liked {
  background-color: #e74c3c; /* 좋아요 눌렀을 때의 배경색 */
  color: #fff; /* 좋아요 눌렀을 때의 글자색 */
}

.like-button:hover {
  background-color: #c0392b; /* 호버 시 테두리 색상 변경 */
}
</style>
