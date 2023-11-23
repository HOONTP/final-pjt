<template>
  <div class="comment-card" @click="navigateToArticle(comment.article)">
    <div class="comment-info">
      <p class="like-count">{{ comment.like_users.length }} Likes</p>
      <div class="content-wrapper">
        <div class="comment-content">
          {{ truncateTitle(comment.content, 20) }}
        </div>
      </div>
      <p class="created-at">{{ formatDateTime(comment.created_at) }}</p>
    </div>
    <p class="comment-type">댓글</p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

defineProps({
  comment: Object
})

const router = useRouter()

const formatDateTime = (timestamp) => {
  const createdDate = new Date(timestamp)
  const formattedDate = createdDate.toLocaleString('ko-KR', { dateStyle: 'long', timeStyle: 'short' })
  return formattedDate
}

const navigateToArticle = (articleId) => {
  router.push({ name: 'ArticleDetailView', params: { id: articleId } })
}

const truncateTitle = (title, maxLength) => {
  if (title.length <= maxLength) {
    return title;
  } else {
    return title.slice(0, maxLength) + '...';
  }
}

</script>

<style scoped>
.comment-card {
  display: flex;
  height: 130px;
  flex-direction: column;
  padding: 20px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer; /* 포인터 커서 추가하여 클릭 가능함을 나타냄 */
}

.comment-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.like-count {
  color: #3498db;
  margin: 0;
}

.content-wrapper {
  flex-grow: 1; /* 제목이 왼쪽에 정렬되도록 */
  text-decoration: none;
}

.comment-content {
  margin-left: 30px;
  font-size: 1.5em;
  color: #333;
}

.comment-type {
  color: #F1948A;
  margin-top: 30px;
}

</style>
