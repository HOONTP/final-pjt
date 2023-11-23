<template>
  <div>
    <div class="section-links">
      <div v-for="section in articleSections" :key="section.id">
        <RouterLink
          :to="{ name: section.routeName }"
          class="section-router-link">
          <p class="section-link">{{ section.label }}</p>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
const articleSections = [
  { id: 1, label: '전체 게시판', routeName: 'CommunityTotalView' },
  { id: 2, label: '인기 게시판', routeName: 'CommunityHotView' },
  { id: 3, label: '리뷰 게시판', routeName: 'CommunityReviewView' },
  { id: 4, label: '자유 게시판', routeName: 'CommunityFreeView' },
]

</script>

<style scoped>
.section-links {
  display: flex;
  position: fixed;
  top: 60px;
  left: 0;
  width: 100%;
  height: 40px;
  background-color: rgba(51, 51, 51, 0.8); /* 검정색의 80% 투명도 */
  padding: 10px 40px;
  z-index: 1000;
}

.section-router-link {
  text-decoration: none;
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

</style>
