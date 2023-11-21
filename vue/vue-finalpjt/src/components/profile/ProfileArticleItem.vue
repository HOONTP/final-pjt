<template>
  <div>
    <p>{{ article }}</p>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
