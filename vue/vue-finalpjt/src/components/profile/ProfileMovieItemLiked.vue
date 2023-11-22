<template>
  <div>
    <p>{{ movie }}</p>
    <img
      v-if="movie && movie.poster_path"
      :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path"
      :alt="movie.title"
      class="movie-poster"
      />
    <h5>{{ movie.id }}</h5>
    <p>{{ movie.title }}</p>
    <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  movie: Object
})
</script>
