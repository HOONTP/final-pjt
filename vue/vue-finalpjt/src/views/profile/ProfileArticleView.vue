<template>
  <div>
    <h3>내가 쓴 게시글 목록</h3>
    <ProfileArticleItem 
      v-for="myArticle in store.myArticles"
      :key="myArticle.id"
      :myArticle="myArticle"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ProfileArticleItem from '@/components/profile/ProfileArticleItem.vue'

const store = useCounterStore()
</script>
