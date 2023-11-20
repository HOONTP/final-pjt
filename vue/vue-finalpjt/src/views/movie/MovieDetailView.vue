<template>
    <div class="movie-details">
      <img
        v-if="store.movie && store.movie.poster_path"
        :src="'https://image.tmdb.org/t/p/w500/' + store.movie.poster_path"
        :alt="store.movie.title"
        class="movie-poster"
      />
      <div v-if="store.movie" class="movie-info">
        <h2>{{ store.movie.original_title }}</h2>
        <p><strong>개봉일:</strong> {{ store.movie.release_date }}</p>
        <p><strong>러닝타임:</strong> {{ store.movie.runtime }} 분</p>
        <p><strong>TMDB 평점:</strong> {{ store.movie.vote_average }}</p>
        <h2><strong>장르</strong></h2>
        <p>
          <span v-for="(genre, index) in store.movie.genres">
            {{ genre.name }}
            <span v-if="index < store.movie.genres.length - 1">, </span>
          </span>
        </p>
        <h2>줄거리</h2>
        <p>{{ store.movie.overview }}</p>
        <h2>공식 예고편</h2>
        <p>공식 예고편이 없습니다.</p>
        <!-- <div v-if="officialTrailer">
        </div>
        <div v-else>
        </div> -->
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
  
  const route = useRoute()
  const movie = ref({})
  const movieId = route.params.id
  const store = useCounterStore()

  onMounted(async () => {
    store.getMovie(movieId)
    console.log(store.movie);
  })
  </script>
  
  <style scoped>
  .movie-details {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px; /* 여기에 원하는 간격을 조절하세요 */
  }
  
  .movie-poster {
    max-width: 100%;
    height: auto;
    margin-bottom: 20px; /* 여기에 원하는 간격을 조절하세요 */
  }
  
  .movie-info {
    text-align: center;
  }
  </style>
  