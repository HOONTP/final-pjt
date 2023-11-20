<template>
  <div>
    <div class="movie-container">
      <div v-for="movie in store.movies" :key="movie.id" class="movie-box">
      <MovieCard
      :movie="movie"
      />
      </div>
    </div>
    <div>
      <!-- 좌우 화살표 버튼 -->
      <button @click="prevPage">이전</button>
      <span>{{ page }}</span>
      <button @click="nextPage">다음</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
// import axios from 'axios'
import MovieCard from '@/components/movie/MovieCard.vue'

const store = useCounterStore()
const router = useRouter()
const page = ref(1)

onMounted(async () => {
    store.getMovies(page.value)
    console.log(store.movies);
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


</style>