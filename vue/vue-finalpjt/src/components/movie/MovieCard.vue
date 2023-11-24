<template>
  <div>
    <img
    v-if="props.movie.poster_path"
    :src="'https://image.tmdb.org/t/p/w500/' + props.movie.poster_path"
    :alt="props.movie.title"
    @click="goDetail(props.movie.id)"
    class="movie-poster"
    />
    <img
    v-else
    src=""
    alt="No Poster Available"
    class="movie-poster"
    />
    <h2 @click="goDetail(props.movie.id)" class="link">
      {{ truncateText(props.movie.original_title, 15) }}
    </h2>
    <p>{{ truncateText(props.movie.overview, 50) }}</p>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const router = useRouter()
const props = defineProps({
    movie:Object
})
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
.movie-poster {
  max-width: 100%; /* 부모 요소에 맞게 크기 조절 */
  max-height: 100%;
  display: block;
  margin: 0 auto;
  cursor: pointer;
}

.link {
  cursor: pointer;
}
</style>