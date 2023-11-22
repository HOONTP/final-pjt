<template>
  <div>
    <div v-for="article in articles" :key="article.id">
      <div class="article-item">
        <p>{{ article.id }}</p>
        <div class="titleComment">
          <RouterLink
            :to="{ name: 'ArticleDetailView', params: { id: article.id }}"
            class="title">
            {{ article.title }}
          </RouterLink>
          <p class="comment">{{ getCommentsLength(article) }}</p>
        </div>
        <p>{{ article.user_nickname }}</p>
        <p>{{ formatCreatedAt(article.created_at) }}</p>
        <p>조회수</p>
        <p>{{ getLikeUsersLength(article) }}</p>
      </div>
      <hr>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const props = defineProps(['articles']);
const store = useCounterStore()

const formatCreatedAt = (createdAt) => {
  const today = new Date()
  const articleDate = new Date(createdAt)
  
  if (
    today.getDate() === articleDate.getDate() &&
    today.getMonth() === articleDate.getMonth() &&
    today.getFullYear() === articleDate.getFullYear()
  ) {
    // 등록일이 오늘이면 시간 및 분 출력
    const hours = articleDate.getHours()
    const minutes = articleDate.getMinutes()
    return `${hours}:${minutes < 10 ? '0' : ''}${minutes}`
  } else {
    // 등록일이 오늘이 아니면 날짜(월-일) 출력
    return `${articleDate.getMonth() + 1}-${articleDate.getDate()}`
  }
}

const getCommentsLength = (article) => {
  // article.comments가 정의되지 않았을 때를 고려하여 길이를 가져오는 함수
  return article.comments ? `[${article.comments.length}]` : '';
}

const getLikeUsersLength = (article) => {
  // article.like_users가 정의되지 않았을 때를 고려하여 길이를 가져오는 함수
  return article.like_users ? article.like_users.length : 0;
}

</script>

<style scoped>
.article-item {
  display: grid;
  grid-template-columns: 1fr 6fr 2fr 1fr 1fr 1fr;
  padding: 10px;
  gap: 10px;
  text-align: center;
  white-space: nowrap;  /* 화면 확대해도 글씨가 줄바꿈 되지 않음 */
}

.titleComment {
  display: flex;
}

.title {
  text-decoration: none;
  color: black;
}

.comment {
  color: red;
  font-weight: bold;
}
</style>