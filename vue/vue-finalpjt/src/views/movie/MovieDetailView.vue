<template>
  <!-- 검색창 -->
  <SearchMovie />

  <div v-if="store.movie" class="container">
    <div class="movie-poster-container">
      <img
        v-if="store.movie && store.movie.poster_path"
        :src="'https://image.tmdb.org/t/p/w500/' + store.movie.poster_path"
        :alt="store.movie.title"
        class="movie-poster"
      />
    </div>
    <div v-if="store.movie">
      <div class="movie-info">
        <h2 class="movie-title">{{ store.movie.original_title }}</h2>
      </div>
      <div v-if="store.movie" class="black-box">
        <div class="details">
          <p>평점 {{ store.movie.vote_average }}</p>
          <p class="separator">·</p>
          <p>{{ getReleaseYear(store.movie.release_date) }}</p>
          <p class="separator">·</p>
          <p>{{ store.movie.runtime }} 분</p>
          <p class="separator">·</p>
          <div v-for="(genre, index) in store.movie.genre_ids" class="genre">
            <p>{{ genre.name }}</p>
            <div v-if="index < store.movie.genre_ids.length - 1" class="separator">·</div>
          </div>
        </div>
        <p class="overview">{{ store.movie.overview }}</p>

        <!-- 영화 좋아요 버튼 -->
        <button
          :class="{ 'like-button': true, 'liked': isLiked(store.movie.id) }"
          @click="toggleLike(store.movie.id)">
          좋아요 ♥
          {{ store.movie.like_users ? store.movie.like_users.length : 0 }}
        </button>
        <hr class="hr">
        <p class="actors-list">출연</p>
        <div class="actors">
        <span v-for="(actor, index) in store.movie.actors.slice(0, 12)" :key="index" class="actor">
          <img v-if="actor.profile_path" :src="getImageUrl(actor.profile_path)" alt="Actor Image" class="actor-img" />
           <div v-else class="no-profile"></div>
            <br>
          {{ actor.name || actor.original_name }}
        </span>
      </div>

      <!-- 영화 리뷰 목록 -->
      <p class="actors-list">리뷰</p>
      <MovieReview />
      </div>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import MovieReview from '@/components/movie/MovieReview.vue'
import SearchMovie from '../../components/commons/SearchMovie.vue'

const route = useRoute()
const movieId = route.params.id
const store = useCounterStore()

onMounted(async () => {
  store.getMovie(movieId)
})

const isLiked = (movieId) => {
  return store.LikedMovies && store.LikedMovies.some(item => item.id === movieId)
}

const toggleLike = (movieId) => {
  store.likeMovie(movieId)
  store.getMovie(movieId)
}

const getImageUrl = (profilePath) => {
  // 이미지의 URL을 구성하는 로직을 이곳에 작성
  // 예시 URL: https://image.tmdb.org/t/p/w500/AbCqqFxNi5w3nDUFdQt0DGMFh5H.jpg
  return `https://image.tmdb.org/t/p/w500/${profilePath}`;
  }

const getReleaseYear = (date) => {
  return new Date(date).getFullYear();
}
</script>
  
<style scoped>
.container {
  position: relative;
  margin: auto;
  margin-top: 100px;
  min-width: 800px;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 50px;
  height: 100vh; /* 높이를 뷰포트 높이의 100%로 설정 */
}

.movie-poster-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 1000px;
}

.movie-poster {
  width: 100%;
  object-fit: cover;
  margin-bottom: 20px;
  position: relative;
  overflow: hidden;
}

.black-box {
  padding: 20px;
  position: absolute;
  left: 0px;
  top: 750px;
  width: 800px;
  background: black;
  z-index: 1;
}

.movie-info {
  color: white;
  background: linear-gradient(transparent, black); /* 그라데이션 색상 및 투명도 설정 */
  padding: 20px;
  position: absolute;
  left: 0px;
  top: 600px;
  width: 800px;
  height: 150px;
  z-index: 2;
}

.movie-info img {
  max-width: 100%;
  max-height: 80px; /* 최대 높이를 지정하여 비율 유지 */
  margin-right: 5px;
}

.movie-title {
  font-size: 40px;
  font-weight: bold;
  margin-bottom: 10px;
}

.genre {
  margin-bottom: 10px;
  display: flex;
}

.movie-info2 {
  position: absolute;
  width: 800px;
  top: 900px;
  padding: 30px;
  z-index: 2;
}

.like-button {
  background-color: #ddd;
  color: black;
  padding: 10px 40px;
  border: none; /* 테두리 추가 */
  border-radius: 30px;
  cursor: pointer;
  font-size: 1.3em;
  margin: 0 auto; /* 가운데 정렬을 위한 margin 추가 */
  display: block; 
  transition: background-color 0.3s;
}

.like-button.liked {
  background-color: #e74c3c; /* 좋아요 눌렀을 때의 배경색 */
  color: #fff; /* 좋아요 눌렀을 때의 글자색 */
}

.like-button:hover {
  background-color: #d63031;
}

.hr {
  margin-top: 20px; /* hr 위쪽 여백 설정 */
  margin-bottom: 20px; /* hr 아래쪽 여백 설정 */
  border: none; /* 기존 border 제거 */
  border-top: 1px solid #f2f2f2; /* 새로운 연한 회색 border 추가 */
}

.actors-list {
  margin-top: 30px;
  margin-bottom: 20px;
  color: white;
  font-size: 20px;
}

.actors {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  z-index: 2;
}

.actor {
  display: flex;
  flex-direction: column;
  width: 165px;
  margin: 10px;
  margin-bottom: 20px;
  align-items: center;
  color: white;
}

.actor img {
  max-width: 80px;
  max-height: 80px;
  border-radius: 50%; /* 배우 이미지를 동그랗게 만듭니다. */
}

.no-profile {
  width: 80px;
  height: 80px;
  background-color: black;
}

.overview {
  line-height: 1.5;
  color: rgb(124, 123, 132);
  margin-bottom: 50px;
}

.separator {
  margin-left: 5px;
  margin-right: 5px;
  color: rgb(186, 186, 193)
}

.details {
  display: flex;
  margin-bottom: 20px;
}

.details p {
  color: rgb(186, 186, 193)
}

</style>
