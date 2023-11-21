<template>
  <div>
    <h3>작성한 댓글</h3>
    {{ store.profile.data.user_comments }}
    <ProfileCommentItem 
      v-for="comment in store.profile.data.user_comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProfileCommentItem from '@/components/profile/ProfileCommentItem.vue'

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
