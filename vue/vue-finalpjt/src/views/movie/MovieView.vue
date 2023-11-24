<template>
  <div>
    <h3>검색 기능</h3>
    <p>
      <SearchMovie />
    </p>
    <div class="movie-container">
      <!-- 좌측: MovieCard -->
      <div v-if="store.movies" class="movie-list">
        <div v-for="movie in store.movies" :key="movie.id" class="movie-box">
          <MovieCard :movie="movie" />
        </div>
      </div>
    </div>

    <!-- 페이지 네비게이션 버튼 -->
    <div>
      <button @click="prevPage" class="pagination-button">이전</button>
      <span>{{ page }}</span>
      <button @click="nextPage" class="pagination-button">다음</button>
    </div>
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
const page = ref(1)

onMounted(async () => {
  await store.getMovies(page.value)
  console.log(store.movies);
  console.log(store.profile.data, 'a')
});

const prevPage = () => {
  if (page.value > 1) {
    page.value -= 1
    store.getMovies(page.value)
    scrollToTop()

  }
};

const nextPage = () => {
  page.value += 1
  store.getMovies(page.value)
  scrollToTop()
};

const scrollToTop = () => {
  // 페이지 상단으로 스크롤
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

</script>

<style scoped>
.movie-container {
  display: flex;
  justify-content: space-between;
}

.movie-list {
  display: flex;
  flex-wrap: wrap;
}
</style>