<template>
  <div>
    <h3>Article List</h3>
    <div v-if="store.articles && store.articles.length > 0">
      <ArticleListItem 
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
      />
    </div>
    <div v-else>
      <p>게시글이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/community/ArticleListItem.vue'

const store = useCounterStore()
// store.articles = ref([])

</script>
