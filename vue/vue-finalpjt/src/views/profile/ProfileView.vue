<template>
  <div class="container">
    <ProfileSectionUser :user_pk="user_pk" />
    <hr class="hr">
    <ProfileSectionContent
      :user_pk="user_pk" />
      <!-- v-if="store.currentUser.user_id == user_pk" -->
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import ProfileSectionUser from '@/components/profile/ProfileSectionUser.vue'
import ProfileSectionContent from '@/components/profile/ProfileSectionContent.vue'

const store = useCounterStore()
const route = useRoute()
const user_pk = ref(route.params.nickName)

</script>

<style scoped>
.container {
  margin: auto;
  margin-top: 120px;
  min-width: 800px;
  max-width: 800px;
}

.hr {
  margin-top: 20px; /* hr 위쪽 여백 설정 */
  margin-bottom: 20px; /* hr 아래쪽 여백 설정 */
  border: none; /* 기존 border 제거 */
  border-top: 1px solid #ddd; /* 새로운 연한 회색 border 추가 */
}
</style>
