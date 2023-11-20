<template>
  <div>
    <div class="section-buttons">
      <div
        v-for="section in articleSections"
        :key="section.routeName"
        @click="changeSection(section)"
        class="section-button"
      >
        {{ section.label }}

      </div>
    </div>
    
    <!-- 현재 선택된 section을 표시 -->
    <component :is="currentSection.component" />
    <RouterLink :to="{ name: 'ArticleCreateView' }">
      글쓰기
    </RouterLink>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import CommunityTotalView from '@/views/community/CommunityTotalView.vue'
import CommunityHotView from '@/views/community/CommunityHotView.vue'
import CommunityReviewView from '@/views/community/CommunityReviewView.vue'
import CommunityFreeView from '@/views/community/CommunityFreeView.vue'

const articleSections = [
  { id: 1, label: '전체 게시판', routeName: 'CommunityTotalView', component: CommunityTotalView },
  { id: 2, label: '인기 게시판', routeName: 'CommunityHotView', component: CommunityHotView },
  { id: 3, label: '리뷰 게시판', routeName: 'CommunityReviewView', component: CommunityReviewView },
  { id: 4, label: '자유 게시판', routeName: 'CommunityFreeView', component: CommunityFreeView },
]
const store = useCounterStore()
const currentSection = ref(articleSections[0])

onMounted(() => {
  store.getArticles(1)
})

const changeSection = (section) => {
  currentSection.value = section
  store.getArticles(section.id)
}
</script>

<style scoped>
.section-buttons {
  display: flex;
  justify-content: space-evenly;
}

.section-button {
  cursor: pointer;
  padding: 10px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.section-button:hover {
  background-color: #f0f0f0;
}
</style>
