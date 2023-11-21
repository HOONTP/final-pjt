<template>
  <div>
    <p>작성자: {{ article.user_nickname }}</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
