<template>
  <div>
    <h3>내가 쓴 댓글 목록</h3>
    <ProfileCommentItem 
      v-for="myComment in store.myComment"
      :key="myComment.id"
      :myComment="myComment"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ProfileCommentItem from '@/components/profile/ProfileCommentItem.vue'

const store = useCounterStore()
</script>
