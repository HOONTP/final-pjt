<template>
  <div>
    <div class="movie-container">
      <div v-for="movie in store.movies" :key="movie.id" class="movie-box">
        <img
          v-if="movie.poster_path"
          :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path"
          :alt="movie.title"
          @click="goDetail(movie)"
          class="movie-poster"
        />
        <img
          v-else
          src="placeholder_image_url"
          alt="No Poster Available"
          class="movie-poster"
        />
        <h2>{{ movie.original_title }}</h2>
        <p>{{ movie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
// import axios from 'axios'

const store = useCounterStore()
const router = useRouter()

onMounted(async () => {
    store.getMovies()
    console.log(store.movies);
});


const goDetail = (movie) => {
  router.push({ name: 'MovieDetailView', params: { id: movie.id } });
}
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

.movie-poster {
  max-width: 100%; /* 부모 요소에 맞게 크기 조절 */
  max-height: 100%;
  display: block;
  margin: 0 auto;
}
</style>