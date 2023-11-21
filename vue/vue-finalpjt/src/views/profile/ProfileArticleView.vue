<template>
  <div>
    <h3>작성한 게시글</h3>
    {{ store.profile.data.user_articles }}
    <ProfileArticleItem 
      v-for="article in store.profile.data.user_articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProfileArticleItem from '@/components/profile/ProfileArticleItem.vue'

const store = useCounterStore()
const props = defineProps(['user_pk'])

onMounted(() => {
  // 특정 유저의 프로필 데이터 가져오기
  store.getProfile(user_pk)
    .catch((err) => {
      console.error(err)
    })
})

</script>
