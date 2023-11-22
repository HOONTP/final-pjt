<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />

    <h2>자유 게시판</h2>
    <ArticleList />

    <!-- 글쓰기 버튼 -->
    <RouterLink :to="{ name: 'ArticleCreateView' }">
      글쓰기
    </RouterLink>
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
  store.getArticles(4)
})
</script>

<style scoped>
h2 {
  margin-top: 100px;  /* header의 높이 */
}
</style>
