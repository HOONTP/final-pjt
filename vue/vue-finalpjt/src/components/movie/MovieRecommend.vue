<template>
    <div v-if="store.recommendmovies" class="movie-container">
      <div v-for="movie in store.recommendmovies" :key="movie.id" class="movie-box">
      <MovieCard :movie="movie" />
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

/* 우측 배너 스타일 */
.movie-box::after {
  content: '추천';
  position: absolute;
  top: 0;
  right: 0;
  background-color: #3498db;
  color: #fff;
  padding: 0.5rem;
  border-radius: 0 0 0 5px; /* 우측 하단만 둥글게 */
}



</style>