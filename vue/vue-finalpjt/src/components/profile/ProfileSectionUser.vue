<template>
  <div id="profile-container">
    <div id="profile-picture">
      <p>[프로필 사진]</p>
    </div>
    <div id="profile-info">
      <h1>{{ store.profile.data.nickname }}</h1>
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
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const props = defineProps(['user_pk'])

onMounted(() => {
  // 특정 유저의 프로필 데이터 가져오기
  store.getProfile(user_pk)
    .catch((err) => {
      console.error(err)
    })
})

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
