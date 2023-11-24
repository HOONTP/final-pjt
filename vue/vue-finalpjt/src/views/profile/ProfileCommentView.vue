<template>
  <div class="container">
    <!-- 댓글 목록 -->
    <ProfileCommentItem 
      v-for="comment in store.profile.data.user_comments"
      :key="comment.id"
      :comment="comment"
    />

    <!-- 답글 목록 -->
    <ProfileReplyItem 
      v-for="reply in store.profile.data.user_replies"
      :key="reply.id"
      :reply="reply"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProfileCommentItem from '@/components/profile/ProfileCommentItem.vue'
import ProfileReplyItem from '@/components/profile/ProfileReplyItem.vue'

const store = useCounterStore()
const props = defineProps({
  'user_pk':String
})
onMounted(async () => {
  // 특정 유저의 프로필 데이터 가져오기
  try {
    await store.getProfile(props.user_pk)
  } catch (err) {
    console.error(err)
  }
})

</script>

<style scoped>
.container {
  margin-bottom: 50px;
}
</style>