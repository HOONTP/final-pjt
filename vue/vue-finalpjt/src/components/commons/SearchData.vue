<template>
  <div>
    <input v-model="keyword" type="text" placeholder="검색어를 입력하세요" @keyup.enter="search" />
    <button @click="search">🔍︎</button>
  </div>
</template>
<!-- <components
:where:'community'
/>  -->
<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const keyword = ref('')

const search = () => {
  store.searchTool(keyword.value)
}

</script>

<style scoped>

</style>