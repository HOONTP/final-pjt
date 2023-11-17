<template>
  <div>
    <h5>{{ myArticle.id }}</h5>
    <p>{{ myArticle.title }}</p>
    <RouterLink :to="{ name: 'ArticleDetailView', params: { id: myArticle.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  myArticle: Object
})
</script>
