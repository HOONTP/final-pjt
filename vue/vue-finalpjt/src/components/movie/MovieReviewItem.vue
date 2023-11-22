<template>
  <div>
    <h1>리뷰 목록이 나오지요</h1>
    <p>{{ store.movieReviews }}</p>
    <p>{{ store.movie }}</p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const movieId = route.params.id

onMounted(async () => {
    store.getMovie(movieId)
    store.getMovieReview(movieId)
  })
</script>

<style scoped>

</style>
