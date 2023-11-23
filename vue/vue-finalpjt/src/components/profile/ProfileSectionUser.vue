<template>
  <!-- {{ store.profile }} -->
  <div id="profile-container">
    <div id="profile-picture">
      <img
        v-if="store.profile.data.profile_image"
        :src="store.profile.data.profile_image"
        alt="프로필 사진"
      />
      <!-- {{ store.profile.data.profile_image }} -->
      <input type="file" v-if="is_edit && store.currentUser.user_id == props.user_pk" ref="imageInput" @change="handleImageChange" />
    </div>
    <div id="profile-info">
      <h1>{{ store.profile.data.nickname }}</h1>
      <button v-if="store.currentUser.user_id == props.user_pk && !is_edit" @click="startEditingProfile">프로필 수정</button>
      <button v-else
        @click="finishEditingProfile">
        수정 완료
      </button>
      <button
      v-if="store.currentUser.user_id != props.user_pk"
        @click="toggleFollow(props.user_pk)">
        팔로우 {{ isFollowing ? '취소' : '하기' }}
      </button>
      <hr>
      <div>
      <p v-if="!is_edit">{{ store.profile.data.introduce }}</p>
      <textarea v-else v-model="editedBio"></textarea>
      </div>
      <br>
      <div id="profile-stats">
        <div class="stat">
          <p class="stat-value">[게시글 수]</p>
          <p>게시물</p>
        </div>
        <div class="stat">
          <p class="stat-value">[댓글 수]</p>
          <p>댓글</p>
        </div>
        <div class="stat">
          <p class="stat-value">[팔로워 수]</p>
          <p>팔로워</p>
        </div>
        <div class="stat">
          <p class="stat-value">[팔로잉 수]</p>
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
const props = defineProps(['user_pk'])
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
      // 좋아요/좋아요 취소 요청이 성공하면 게시글 데이터를 다시 불러와 갱신
      store.getArticle(route.params.id)
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
}

#profile-picture {
  width: 25%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#profile-info {
  width: 75%;
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
</style>
