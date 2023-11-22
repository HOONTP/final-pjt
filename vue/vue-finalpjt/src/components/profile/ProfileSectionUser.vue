<template>
  {{ store.profile }}
  <div id="profile-container">
    <div id="profile-picture">
      <p>[프로필 사진]</p>
    </div>
    <div id="profile-info">
      <h1>{{ store.profile.data.nickname }}</h1>
      <button v-if="store.currentUser.user_id == props.user_pk">프로필 수정</button>
      <button 
        v-else
        @click="toggleFollow(props.user_pk)">
        팔로우 {{ isFollowing ? '취소' : '하기' }}
      </button>
      <hr>
      <p>[한 줄 자기소개]</p>
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
import { computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const props = defineProps(['user_pk'])

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
