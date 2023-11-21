<template>
  <div>
    <p>{{ comment }}</p>
    <h5>{{ comment.id }}</h5>
    <p>{{ comment.title }}</p>
    <!-- 내가 쓴 댓글을 선택하면 해당 댓글이 작성 된 게시글로 이동 -->
    <RouterLink :to="{ name: 'ArticleDetailView', params: { id: comment.article_id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  comment: Object
})
</script>
