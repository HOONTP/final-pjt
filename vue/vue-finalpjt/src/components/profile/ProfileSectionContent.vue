<template>
  <div>
    <div class="section-buttons">
      <div
        v-for="section in profileSections"
        :key="section.routeName"
        @click="changeSection(section)"
        class="section-button"
      >
        {{ section.label }}
      </div>
    </div>

    <!-- 현재 선택된 section을 표시 -->
    <component :is="currentSection.component" />

  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProfileArticleView from '@/views/profile/ProfileArticleView.vue'
import ProfileCommentView from '@/views/profile/ProfileCommentView.vue'
import ProfileBookmarkView from '@/views/profile/ProfileBookmarkView.vue'
import ProfileLikeView from '@/views/profile/ProfileLikeView.vue'

const profileSections = [
  { label: '내 게시글', routeName: 'ProfileArticleView', component: ProfileArticleView },
  { label: '내 댓글', routeName: 'ProfileCommentView', component: ProfileCommentView },
  { label: '북마크', routeName: 'ProfileBookmarkView', component: ProfileBookmarkView },
  { label: '좋아요', routeName: 'ProfileLikeView', component: ProfileLikeView },
]

const currentSection = ref(profileSections[0])

const changeSection = (section) => {
  currentSection.value = section
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
