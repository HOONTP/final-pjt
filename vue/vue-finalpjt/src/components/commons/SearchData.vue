<template>
    <div>
        <input v-model="keyword" type="text" placeholder="검색어를 입력하세요" />
        <button @click="search">검색</button>
    </div>
</template>
<!-- <components
:where:'community'
/>  -->
<script setup>
import { ref } from 'vue';
const keyword = ref('');
const where = ref('')
const search = () => {
  store.searchTool(where, keyword.value);
};
</script>

<style scoped>

</style>