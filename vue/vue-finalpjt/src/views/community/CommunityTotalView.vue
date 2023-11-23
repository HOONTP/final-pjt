<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />

    <div class="container">
      <div class="header">
        <h2>전체 게시판</h2>
        
        <!-- 글쓰기 버튼 -->
        <RouterLink :to="{ name: 'ArticleCreateView' }" class="write-button">
          글쓰기
        </RouterLink>
      </div>

      <ArticleList v-if="store.articles" :articles="store.articles" />
    </div>
    <div>
      <SearchArticle />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import ArticleList from '@/components/community/ArticleList.vue'
import CommunityNav from '@/components/community/CommunityNav.vue'
import SearchArticle from '../../components/commons/SearchArticle.vue'
const store = useCounterStore()

onMounted(() => {
  // 게시글 데이터 가져오기
  store.getArticles(1)
  store.now_gps = 'community'
})

</script>

<style scoped>
* {
  white-space: nowrap;
}

.container {
  margin: auto;
  margin-top: 120px;
  min-width: 800px;
  max-width: 800px;
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
  transition: background-color 0.3s;
}

.write-button:hover {
  background-color: #45a049;
}

</style>
