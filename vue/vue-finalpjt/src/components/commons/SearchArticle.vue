<template>
  <div class="search-container">
    <input v-model="keyword" type="text" placeholder="검색어를 입력하세요" @keyup.enter="search" />
    <button @click="search">🔍︎</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const keyword = ref('')

const search = () => {
  store.searchArticle(keyword.value)
};
</script>

<style scoped>
.search-container {
  margin-top: 40px;
  display: flex;
  align-items: center;
  justify-content: center; /* 가운데 정렬을 위해 추가 */
}

input {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-right: 5px;
}

button {
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  cursor: pointer;
  font-size: 16px;
}
</style>
