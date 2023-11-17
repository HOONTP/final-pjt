<template>
  <div>
    <h5>{{ myComment.id }}</h5>
    <p>{{ myComment.title }}</p>
    <!-- 내가 쓴 댓글을 선택하면 해당 댓글이 작성 된 게시글로 이동해야함.. -->
    <!-- <RouterLink :to="{ name: 'ArticleDetailView', params: { id: myComment.id }}">
      [Detail]
    </RouterLink> -->
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  myComment: Object
})
</script>
