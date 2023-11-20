<template>
    <div>
        <img
        v-if="props.movie.poster_path"
        :src="'https://image.tmdb.org/t/p/w500/' + props.movie.poster_path"
        :alt="props.movie.title"
        @click="goDetail(props.movie)"
        class="movie-poster"
        />
        <img
        v-else
        src="placeholder_image_url"
        alt="No Poster Available"
        class="movie-poster"
        />
        <h2>{{ props.movie.original_title }}</h2>
        <p>{{ props.movie.overview }}</p>

    </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
    movie:Object
})
const goDetail = (movie) => {
  router.push({ name: 'MovieDetailView', params: { id: movie.id } });
}
</script>

<style scoped>
.movie-poster {
  max-width: 100%; /* 부모 요소에 맞게 크기 조절 */
  max-height: 100%;
  display: block;
  margin: 0 auto;
}

</style>