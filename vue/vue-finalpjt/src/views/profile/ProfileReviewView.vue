<template>
  <div class="container" v-if="store.profile.data">
    <ProfileReviewItem 
      v-for="review in store.profile.data.user_reviews"
      :key="review.id"
      :review="review"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProfileReviewItem from '@/components/profile/ProfileReviewItem.vue'

const store = useCounterStore()
const props = defineProps(['user_pk'])

onMounted(async () => {
  // 특정 유저의 프로필 데이터 가져오기
  try {
    await store.getProfile(props.user_pk)
  } catch (err) {
    console.error(err)
  }
})

</script>

<style scoped>
.container {
  margin-bottom: 50px;
}
</style>