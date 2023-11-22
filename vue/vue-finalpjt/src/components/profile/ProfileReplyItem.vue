<template>
  <div>
    <p>{{ reply }}</p>
    <h5>{{ reply.id }}</h5>
    <p>{{ reply.content }}</p>
    <!-- 내가 쓴 댓글을 선택하면 해당 댓글이 작성 된 게시글로 이동 -->
    <!-- <RouterLink :to="{ name: 'ArticleDetailView', params: { id: reply.comment.article }}">
      [Detail]
    </RouterLink> -->
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  reply: Object
})
</script>
  