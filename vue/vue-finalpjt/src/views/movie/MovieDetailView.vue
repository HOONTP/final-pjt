<template>
    <div class="movie-details">
      <img
        v-if="movie && movie.poster_path"
        :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path"
        :alt="movie.title"
        class="movie-poster"
      />
      <div v-if="movie" class="movie-info">
        <h2>{{ movie.original_title }}</h2>
        <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
        <p><strong>러닝타임:</strong> {{ movie.runtime }} 분</p>
        <p><strong>TMDB 평점:</strong> {{ movie.vote_average }}</p>
        <h2><strong>장르</strong></h2>
        <p>
          <span v-for="(genre, index) in movie.genres">
            {{ genre.name }}
            <span v-if="index < movie.genres.length - 1">, </span>
          </span>
        </p>
        <h2>줄거리</h2>
        <p>{{ movie.overview }}</p>
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
  import axios from 'axios'
  
  const route = useRoute()
  const movie = ref({})
  const movieId = route.params.movieId
  const apiKey = 'd1f7efa5fffb21e196b176b6a9ac8029'
  const apiUrl = `https://api.themoviedb.org/3/movie/${movieId}`
  
  onMounted(async () => {
    try {
      const response = await axios.get(apiUrl, {
        params: {
          api_key: apiKey,
          language: 'ko-KR',
        },
      })
      movie.value = response.data
    } catch (error) {
      console.error('Error:', error.message)
    }
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
  