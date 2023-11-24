<template>
  <!-- 검색창 -->
  <SearchMovie />

  <div class="container">
    <div class="movie-container">
      <!-- 좌측: MovieCard -->
      <div v-if="store.movies" class="movie-list">
        <div v-for="movie in store.movies" :key="movie.id" class="movie-box">
          <MovieCard :movie="movie" />
        </div>
      </div>
    </div>

    <!-- 페이지 네비게이션 버튼 -->
    <div class="pagination-buttons" v-if="store.isSearch === false">
      <button @click="prevPage" class="pagination-button">이전</button>
      <span class="page-number">{{ store.moviePage }}</span>
      <button @click="nextPage" class="pagination-button">다음</button>
    </div>
    <div v-else></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

// import axios from 'axios'
import MovieCard from '@/components/movie/MovieCard.vue'
import SearchMovie from '../../components/commons/SearchMovie.vue'

const store = useCounterStore()
const router = useRouter()
// const page = ref(1)

onMounted(async () => {
  await store.getMovies(store.moviePage)
  console.log(store.movies);
  console.log(store.profile.data, 'a')
});

const prevPage = () => {
  if (store.moviePage > 1) {
    store.moviePage -= 1
    store.getMovies(store.moviePage)
    scrollToTop()
  }
};

const nextPage = () => {
  store.moviePage = store.moviePage + 1
  store.getMovies(store.moviePage)
  scrollToTop()
};

const scrollToTop = () => {
  // 페이지 상단으로 스크롤
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

</script>

<style scoped>
.container {
  margin: auto;
  margin-top: 120px;
  min-width: 800px;
  max-width: 800px;
}

.movie-container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap; /* 줄 바꿈을 허용하여 다음 줄에 이어서 표시 */
}

.movie-list {
  display: flex;
  flex-wrap: wrap; /* MovieBox들을 한 줄에 여러 개 배치 */
  justify-content: space-between; /* 좌우로 공간 분배하여 정렬 */
}

.movie-box {
  width: calc(33.33% - 10px); /* 한 줄에 3개씩 나오도록 폭 조절, 여백 고려 */
  margin-bottom: 20px; /* 아래 여백 추가 */
}

.pagination-buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  margin-bottom: 50px;
}

.pagination-button {
  font-size: 16px;
  padding: 10px 20px;
  background-color: #333;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.pagination-button:hover {
  background-color: #555;
}

.page-number {
  font-size: 18px;
  margin: 0 10px;
  color: #333;
}

</style>