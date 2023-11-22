<template>
  <div>
    <div class="article-header">
      <p>번호</p>
      <p>제목</p>
      <p>글쓴이</p>
      <p>등록일</p>
      <p>조회</p>
      <p>추천</p>
    </div>
    
    <ArticleListItem :articles="articles"/>
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/community/ArticleListItem.vue'

const props = defineProps(['articles'])

</script>

<style scoped>
.article-header {
  display: grid;
  grid-template-columns: 1fr 6fr 2fr 1fr 1fr 1fr;
  background-color: #f0f0f0;
  margin-top: 10px;
  padding: 10px;
  gap: 10px;
  text-align: center;
  white-space: nowrap; /* 화면 확대해도 글씨가 줄바꿈 되지 않음 */
}

</style>