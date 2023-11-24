<template>
  <div>
    <div class="search-nav">
      <p @click="search" class="icon">🔍︎</p>
      <input
        v-model="keyword"
        type="text"
        placeholder="영화를 검색하세요"
        @keyup.enter="search"
        class="search"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const keyword = ref('')
const router = useRouter()

const search = () => {
  store.searchMovie(keyword.value)
  router.push({ name: 'MovieView' })
};
</script>

<style scoped>
.search-nav {
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 60px;
  left: 0;
  width: 100%;
  height: 40px;
  background-color: rgba(51, 51, 51, 0.8);
  z-index: 1000;
}

.icon {
  margin-left: 50px;
  color: rgb(132, 134, 141);
  height: 30px;
  width: 40px;
  background-color: rgba(51, 51, 51, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  border-top-left-radius: 5px; /* 왼쪽 위 모서리 둥글게 */
  border-bottom-left-radius: 5px; /* 왼쪽 아래 모서리 둥글게 */
  cursor: pointer;
}

.search {
  color: white;
  border: none;
  outline: none;
  width: 500px;
  height: 30px;
  margin-right: 10px;
  background-color: rgba(51, 51, 51, 0.8);
  z-index: 1000;
  border-top-right-radius: 5px; /* 오른쪽 위 모서리 둥글게 */
  border-bottom-right-radius: 5px; /* 오른쪽 아래 모서리 둥글게 */
}

.search-nav::placeholder {
  color: rgb(132, 134, 141);
}

.search-nav {
  caret-color: red;
}

</style>
