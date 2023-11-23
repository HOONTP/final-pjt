<template>
  <div class="article-card" @click="navigateToArticle(article.id)">
    <div class="article-info">
      <p class="like-count">{{ article.like_users.length }} Likes</p>
      <div class="title-wrapper">
        <div class="article-title">
          {{ truncateTitle(article.title, 20) }}
        </div>
      </div>
      <p class="created-at">{{ formatDateTime(article.created_at) }}</p>
    </div>
    <div class="additional-info">
      <p class="board-info">{{ getBoardType(article.board) }} 게시판</p>|
      <p class="read-count">{{ article.counting }}명이 읽었어요</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

defineProps({
  article: Object
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

const getBoardType = (board) => {
  switch (board) {
    case 1:
      return '전체'
    case 2:
      return '인기'
    case 3:
      return '리뷰'
    case 4:
      return '자유'
    default:
      return ''
  }
}
</script>

<style scoped>
.article-card {
  display: flex;
  height: 130px;
  flex-direction: column;
  padding: 20px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer; /* 포인터 커서 추가하여 클릭 가능함을 나타냄 */
}

.article-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.like-count {
  color: #3498db;
  margin: 0;
}

.title-wrapper {
  flex-grow: 1; /* 제목이 왼쪽에 정렬되도록 */
  text-decoration: none;
}

.article-title {
  margin-left: 30px;
  font-size: 1.5em;
  color: #333;
}

.created-at {
  color: #888;
  margin: 0;
}

.additional-info {
  display: flex;
  margin-top: 20px;
  align-items: center;
}

.board-info {
  color: #555;
  margin-right: 10px;
}

.read-count {
  color: #27ae60;
  margin-left: 10px;
  font-size: 0.9em;
}
</style>
