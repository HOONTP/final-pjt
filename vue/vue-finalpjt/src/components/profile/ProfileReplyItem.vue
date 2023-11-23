<template>
  <div class="reply-card" @click="navigateToArticle(reply.article)">
    <div class="reply-info">
      <p class="like-count">{{ reply.like_users.length }} Likes</p>
      <div class="content-wrapper">
        <div class="reply-content">
          {{ truncateTitle(reply.content, 20) }}
        </div>
      </div>
      <p class="created-at">{{ formatDateTime(reply.created_at) }}</p>
    </div>
    <p class="reply-type">답글</p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

defineProps({
  reply: Object
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
.reply-card {
  display: flex;
  height: 130px;
  flex-direction: column;
  padding: 20px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer; /* 포인터 커서 추가하여 클릭 가능함을 나타냄 */
}

.reply-info {
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

.reply-content {
  margin-left: 30px;
  font-size: 1.5em;
  color: #333;
}

.created-at {
  color: #888;
  margin: 0;
}

.reply-type {
  color: #7DCEA0;
  margin-top: 30px;
}
</style>
