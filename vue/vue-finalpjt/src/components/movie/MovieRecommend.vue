<template>
    <div class="movie-container">
        <div v-for="movie in store.recommendmovies" :key="movie.id" class="movie-box">
            <MovieCard
            :movie="movie"
            />
        </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import MovieCard from '@/components/movie/MovieCard.vue'

const store = useCounterStore()

</script>

<style scoped>
.movie-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.movie-box {
  box-sizing: border-box;
  width: 30%;
  margin: 1rem;
  padding: 1rem;
  border: 1px solid #ccc;
}
</style>