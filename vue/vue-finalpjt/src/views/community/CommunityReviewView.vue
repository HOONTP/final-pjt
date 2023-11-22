<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />

    <div class="container">
      <div class="header">
        <h2>리뷰 게시판</h2>

        <!-- 글쓰기 버튼 -->
        <RouterLink :to="{ name: 'ArticleCreateView' }" class="write-button">
          글쓰기
        </RouterLink>
      </div>

      <ArticleList :articles="store.articles" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import ArticleList from '@/components/community/ArticleList.vue'
import CommunityNav from '@/components/community/CommunityNav.vue'

const store = useCounterStore()

onMounted(() => {
  // 게시글 데이터 가져오기
  store.getArticles(3)
})
</script>

<style scoped>
* {
  white-space: nowrap;
}

.container {
  margin: 0 20px;
  margin-top: 120px;
}

.header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
}

.write-button {
  background-color: #4CAF50;
  color: white;
  padding: 8px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 5px; 
  transition: background-color 0.3s; /* Smooth color transition on hover */
}

.write-button:hover {
  background-color: #45a049; /* Darker green on hover */
}

</style>
