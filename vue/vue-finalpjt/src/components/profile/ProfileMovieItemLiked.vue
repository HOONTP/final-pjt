<template>
  <div class="movie-card" @click="navigateToMovie(movie.id)">
    <div class="poster-wrapper">
      <img
        v-if="movie && movie.poster_path"
        :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path"
        :alt="movie.title"
        class="movie-poster"
      />
    </div>
    <div class="movie-info">
      <p class="movie-title">{{ movie.title }}</p>
      <div class="movie-preference">
        <p class="like-count">{{ movie.like_users.length }} Likes</p>
        <p class="popularity">{{ movie.popularity }} Popularity</p>
      </div>
      <p>{{ truncateTitle(movie.overview, 120) }}</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

defineProps({
  movie: Object
})

const navigateToMovie = (movieId) => {
  router.push({ name: 'MovieDetailView', params: { id: movieId } })
}

const truncateTitle = (overview, maxLength) => {
  if (overview.length <= maxLength) {
    return overview;
  } else {
    return overview.slice(0, maxLength) + '...';
  }
}
</script>

<style scoped>

.poster-wrapper {
  max-width: 300px;
}

.movie-poster {
  width: auto;
  height: 100%;
}

.movie-card {
  display: flex;
  height: 200px;
  padding: 20px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer; /* 포인터 커서 추가하여 클릭 가능함을 나타냄 */
}

.movie-info {
  margin-left: 30px;
}

.movie-title {
  font-size: 1.5em;
  color: #333;
  margin-bottom: 10px;
}

.movie-preference {
  display: flex;
  margin-bottom: 10px;
}
.like-count {
  color: #3498db;
}

.popularity {
  color: #F1948A;
  margin-left: 20px;
}
</style>
