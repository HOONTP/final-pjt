<template>
    <div>
        <div v-for="movie in store.recommendmovies" :key="movie.id">
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
        <h2 @click="goDetail(movie)">{{ movie.title && movie.original_title }}</h2>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()

const goDetail = (movie) => {
  router.push({ name: 'MovieDetailView', params: { id: movie.id } });
}
</script>

<style scoped>

</style>