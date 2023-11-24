<template>
  <div class="review-card" @click="navigateToArticle(review.movie)">
    <div class="review-info">
      <p class="like-count">{{ review.like_users.length }} Likes</p>
      <div class="review-wrapper">
        <div class="review-content">
          {{ truncateContent(review.content, 20) }}
        </div>
      </div>
      <p class="created-at">{{ formatDateTime(review.created_at) }}</p>
    </div>
    <p class="review-type">리뷰</p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

defineProps({
  review: Object
})

const router = useRouter()

const formatDateTime = (timestamp) => {
  const createdDate = new Date(timestamp)
  const formattedDate = createdDate.toLocaleString('ko-KR', { dateStyle: 'long', timeStyle: 'short' })
  return formattedDate
}

const navigateToArticle = (movieId) => {
  router.push({ name: 'MovieDetailView', params: { id: movieId } })
}

const truncateContent = (content, maxLength) => {
  if (content.length <= maxLength) {
    return content;
  } else {
    return content.slice(0, maxLength) + '...';
  }
}
  
</script>

<style scoped>
.review-card {
  display: flex;
  height: 130px;
  flex-direction: column;
  padding: 20px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer; /* 포인터 커서 추가하여 클릭 가능함을 나타냄 */
}

.review-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.like-count {
  color: #3498db;
  margin: 0;
}

.review-wrapper {
  flex-grow: 1; /* 제목이 왼쪽에 정렬되도록 */
  text-decoration: none;
}

.review-content {
  margin-left: 30px;
  font-size: 1.5em;
  color: #333;
}

.review-type {
  color: #F1948A;
  margin-top: 30px;
}

</style>
