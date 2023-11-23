<template>
  <div class="container">
    <p class="message">HOT 게시물</p>
    <!-- 인기 게시물 출력 -->
    <div v-if="store.hotArticles && store.hotArticles.length > 0">
      <div
        v-for="article in store.hotArticles"
        :key="article.id"
        class="article-box"
        @click="goDetail(article.id)">
        <h3>{{ truncateText(article.title, 15) }}</h3>
        <p>{{ getBoardType(article.board) }} 게시판</p>
        <div class="article-info">
          <p class="like_users">{{ article.like_users.length }} Likes ·</p>
          <p class="counting">조회 {{ article.counting }} ·</p>
          <p class="comment_reply_count">댓글 {{ article.comment_reply_count }}</p>
        </div>
      </div>
    </div>

    <!-- 인기 게시물이 없는 경우에 대한 처리 -->
    <div v-else>
      <p>인기 게시물이 없습니다 ㅠㅠ</p>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const router = useRouter()
const store = useCounterStore()

onMounted(() => {
  // 컴포넌트가 마운트되면 인기 게시물 조회
  store.getHotArticles()
})

const getBoardType = (board) => {
  switch (board) {
    case 1:
      return '코딩'
    case 2:
      return '유머'
    case 3:
      return '리뷰'
    case 4:
      return '자유'
    default:
      return ''
  }
}

const truncateText = function (title, maxLength) {
  if (title && title.length > maxLength) {
    return title.slice(0, maxLength) + '...';
  }
  return title;
}

const goDetail = (articleId) => {
  router.push({ name: 'ArticleDetailView', params: { id: articleId } });
}

</script>

<style scoped>
.container {
  margin-top: 100px;
}

.message {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
  white-space: nowrap;
  text-align: center;
}

.article-box {
  margin-top: 20px;
  border: 1px solid #ccc;
  padding: 10px;
  white-space: nowrap;
  cursor: pointer;
}

.article-info {
  display: flex;
}

.like_users {
  color: #FF3333;
}

.counting {
  color: rgb(0, 153, 204);
}

.comment_reply_count {
  color: rgb(146, 186, 62);
}

</style>
