<template>
  <div>
    <div class="section-links">
      <div
        v-for="section in articleSections"
        :key="section.routeName"
        @click="changeSection(section)"
        class="section-link"
      >
        {{ section.label }}
      </div>
    </div>
    
    <!-- 현재 선택된 section을 표시 -->
    <component :is="currentSection.component" class="current-section"/>
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
.section-links {
  display: flex;
  position: fixed;
  top: 57.2px;
  left: 0;
  width: 100%;
  background-color: rgba(51, 51, 51, 0.8); /* 검정색의 80% 투명도 */
  padding: 10px 40px;
  z-index: 1000;
}

.section-link {
  margin-right: 20px;
  font-size: 14px;
  color: white;
  cursor: pointer;
  white-space: nowrap;  /* 화면 확대해도 글씨가 줄바꿈 되지 않음 */
  transition: color 0.3s ease; /* 색상 변경에 애니메이션 효과를 부여함 */
}

.section-link:hover {
  color: #999999; /* 마우스 올리면 색 변경 */
}

.current-section {
  margin-top: 100px;
}
</style>
