<template>
  <div id="profile-container">
    <div id="profile-picture">
      <div v-if="is_edit || !is_edit">
      <img
        v-if="store.profile.data.profile_image && typeof is_edit !== 'undefined' && !is_edit"
        :src="store.API_URL+store.profile.data.profile_image"
        alt="프로필 사진"
        class="profile-image"
      />
      </div>
      <!-- {{ store.API_URL+store.profile.data.profile_image }} -->
      <input type="file" v-if="is_edit && store.currentUser.user_id == props.user_pk" ref="imageInput" @change="handleImageChange" />
    </div>
    <div id="profile-info">
      <div class="profile-header">
        <h1>{{ store.profile.data.nickname }}</h1>
        <div class="buttons">
          <div v-if="store.currentUser.user_id == props.user_pk">
            <button v-if="!is_edit" @click="startEditingProfile" class="edit-button">프로필 수정</button>
            <button v-else @click="finishEditingProfile" class="edit-button">수정 완료</button>
          </div>
          <button
            v-if="store.currentUser.user_id != props.user_pk"
            @click="toggleFollow(props.user_pk)"
            class="follow-button"
          >
            {{ isFollowing ? '팔로우 취소' : '팔로우 하기' }}
          </button>
        </div>
      </div>
      <hr class="hr">
      <div>
        <p v-if="!is_edit" class="bio">{{ store.profile.data.introduce }}</p>
        <textarea v-else v-model="editedBio" class="bio-textarea"></textarea>
      </div>
      <br>
      <div id="profile-stats">
        <div class="stat">
          <p class="stat-value">{{ store.profile.data.user_articles.length }}</p>
          <p>게시물</p>
        </div>
        <div class="stat">
          <p class="stat-value">
            {{ store.profile.data.user_comments.length + store.profile.data.user_replies.length }}
          </p>
          <p>댓글</p>
        </div>
        <div class="stat">
          <p class="stat-value">{{ store.profile.data.followers.length }}</p>
          <p>팔로워</p>
        </div>
        <div class="stat">
          <p class="stat-value">{{ store.profile.data.followings.length }}</p>
          <p>팔로잉</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const props = defineProps(['user_pk', 'nickName'])
const is_edit = ref(false)
const selectedImage = ref(null);
const editedBio = ref(null)

const isFollowing = computed(() => {
  // 현재 로그인한 사용자의 pk 값
  const currentUserPk = store.currentUser.user_id

  // 현재 프로필 유저를 팔로잉한 사람들의 pk 배열
  const followersPks = store.profile.data?.followers || []

  // 현재 로그인한 사용자의 pk가 팔로잉한 사람들의 pk 배열에 포함되어 있는지 확인
  return followersPks.includes(currentUserPk)
})

onMounted(async () => {
  // 특정 유저의 프로필 데이터 가져오기
  try {
    await store.getProfile(props.user_pk)
  } catch (err) {
    console.error(err)
  }
})

const toggleFollow = (userId) => {
  // 팔로우 하기/취소 요청 보내기
  axios({
    method: 'post',
    url: `${store.API_URL}/accounts/${userId}/follow/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      // 좋아요/좋아요 취소 요청이 성공하면 페이지 리로드
      window.location.reload();
    })
    .catch((err) => {
      console.error('팔로우 토글 에러:', err)
    })
}

const startEditingProfile = () => {
  is_edit.value = true
  editedBio.value = store.profile.data.introduce || ''
}

const finishEditingProfile = () => {
  const formData = new FormData();
  console.log(selectedImage.value)

  if (selectedImage.value) {
    formData.append('profile_image', selectedImage.value);
    console.log(selectedImage.value)
  }
  if (editedBio.value) {
    formData.append('bio', editedBio.value);
    console.log(editedBio.value)

  }

  axios.post(`${store.API_URL}/accounts/profile-update/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
      'Authorization': `Token ${store.token}`,
    },
  })
  .then(response => {
    console.log(response.data);
    // 수정이 완료되었을 때의 추가 작업 수행
    is_edit.value = false
    store.getProfile(props.user_pk)
  })
  .catch(error => {
    console.error(error);
  });
};
const handleImageChange = (event) => {
  // 선택된 파일을 가져옵니다.
  const file = event.target.files[0];

  // ref에 선택된 파일을 할당합니다.
  selectedImage.value = file;

  // 선택된 파일 확인 (콘솔에 출력)
  console.log(selectedImage.value);
};
</script>

<style scoped>
#profile-container {
  display: flex;
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

#profile-picture {
  width: 25%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.profile-image {
  width: 100%;
  max-width: 200px; /* 최대 너비 설정 */
  border-radius: 50%; /* 원형 프로필 이미지를 위해 반지름 50% 설정 */
}

.profile-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.buttons {
  display: flex;
}

.edit-button,
.follow-button {
  background-color: rgb(76, 181, 249);
  color: white;
  margin: 10px;
  padding: 8px 16px;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.edit-button:hover,
.submit-button:hover {
  background-color: rgb(0, 120, 215);
}

.bio {
  font-size: 16px;
  margin-bottom: 10px;
  height: 100px;
}

.bio-textarea {
  width: 100%;
  height: 80px;
  margin-bottom: 10px;
  padding: 8px;
  font-size: 14px;
  border-radius: 5px;
}

#profile-info {
  width: 75%;
  padding-left: 20px;
}

#profile-stats {
  display: flex;
}

.stat {
  text-align: center;
  flex: 1;
}

.stat-value {
  font-weight: bold;
}

.hr {
  margin-top: 20px; /* hr 위쪽 여백 설정 */
  margin-bottom: 20px; /* hr 아래쪽 여백 설정 */
  border: none; /* 기존 border 제거 */
  border-top: 1px solid #ddd; /* 새로운 연한 회색 border 추가 */
}
</style>