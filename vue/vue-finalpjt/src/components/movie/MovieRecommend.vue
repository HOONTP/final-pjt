<template>
  <div class="container">
    <p class="recommend">이런 영화는 어때요?</p>
    <div v-if="store.recommendmovies.message === `관심 영화가 5개 이상 필요합니다.`">
      <p class="message">관심 영화가 5개 이상 필요합니다!</p>
    </div>
    <div v-else="store.recommendmovies" class="movie-container">
      <div v-for="movie in store.recommendmovies" :key="movie.id" class="movie-box">
        <img
        v-if="movie.poster_path"
        :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path"
        :alt="movie.title"
        @click="goDetail(movie.id)"
        class="movie-poster"
        />
        <img
        v-else
        src=""
        alt="포스터가 없어요.."
        class="movie-poster"
        />
        <h2 @click="goDetail(movie.id)" class="link">
          {{ truncateText(movie.original_title, 15) }}
        </h2>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()

const truncateText = function (overview, maxLength) {
  if (overview && overview.length > maxLength) {
    return overview.slice(0, maxLength) + '...';
  }
  return overview;
}
const goDetail = (movieId) => {
  router.push({ name: 'MovieDetailView', params: { id: movieId } });
  store.getMovie(movieId)
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

</script>

<style scoped>
.container {
  margin-top: 100px;
}

.recommend {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
  white-space: nowrap;
  text-align: center;
  white-space: nowrap;
}

.message{
  white-space: nowrap;
}

.movie-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.movie-box {
  box-sizing: border-box;
  width: 300px;
  margin: 1rem;
  padding: 1rem;
  border: 1px solid #ccc;
}

.movie-poster {
  max-width: 100%; /* 이미지의 최대 너비를 설정 */
  height: auto; /* 가로 너비에 따라 세로 비율을 자동으로 조절 */
  cursor: pointer;
}

.link {
  color: black;
  font-size: 20px;
  cursor: pointer;
}

</style>
