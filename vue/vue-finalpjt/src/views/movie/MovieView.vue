<template>
  <div>
    <div class="movie-container">
      <div v-for="movie in movies.results" :key="movie.id" class="movie-box">
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const movies = ref([])
const apiKey = 'd1f7efa5fffb21e196b176b6a9ac8029'
const apiUrl = 'https://api.themoviedb.org/3/movie/popular'

axios.get(apiUrl, {
  params: {
    api_key: apiKey,
    language: 'ko-KR',
  },
})
  .then((response) => {
    // console.log(response.data)
    movies.value = response.data
  })
  .catch((error) => {
    console.error('Error:', error.message)
  })

  const goDetail = (movie) => {
    router.push(`/${movie.id}`)
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