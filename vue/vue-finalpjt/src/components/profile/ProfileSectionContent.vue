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
    <component :is="currentSection.component" :user_pk="props.user_pk" />

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProfileArticleView from '@/views/profile/ProfileArticleView.vue'
import ProfileCommentView from '@/views/profile/ProfileCommentView.vue'
import ProfileLikeView from '@/views/profile/ProfileLikeView.vue'

const profileSections = [
  { label: '게시글', routeName: 'ProfileArticleView', component: ProfileArticleView },
  { label: '댓글', routeName: 'ProfileCommentView', component: ProfileCommentView },
  { label: '좋아요', routeName: 'ProfileLikeView', component: ProfileLikeView },
]

const store = useCounterStore()
const props = defineProps(['user_pk'])
const currentSection = ref(profileSections[0])

onMounted(async () => {
  // 특정 유저의 프로필 데이터 가져오기
  try {
    await store.getProfile(props.user_pk)
  } catch (err) {
    console.error(err)
  }
})

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
