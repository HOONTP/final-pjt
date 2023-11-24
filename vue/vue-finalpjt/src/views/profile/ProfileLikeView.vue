<template>
  <div class="like-container">
    <div class="container">
      <h3>좋아요 한 게시글</h3>
      <ProfileArticleItem 
        v-for="article in store.profile.data.like_articles"
        :key="article.id"
        :article="article"
      />
    </div>

    <div class="container">
      <h3>좋아요 한 댓글</h3>
      <!-- 댓글 목록 -->
      <ProfileCommentItem 
        v-for="comment in store.profile.data.like_comments"
        :key="comment.id"
        :comment="comment"
      />

      <!-- 답글 목록 -->
      <ProfileReplyItem 
        v-for="reply in store.profile.data.like_replies"
        :key="reply.id"
        :reply="reply"
      />
    </div>

    <div class="container">
      <h3>좋아요 한 영화</h3>
      <ProfileMovieItemLiked 
        v-for="movie in store.profile.data.like_movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>

    <div class="container">
      <h3>좋아요 한 리뷰</h3>
      <ProfileReviewItem 
        v-for="review in store.profile.data.like_reviews"
        :key="review.id"
        :review="review"
      />
    </div>

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProfileArticleItem from '@/components/profile/ProfileArticleItem.vue'
import ProfileCommentItem from '@/components/profile/ProfileCommentItem.vue'
import ProfileReplyItem from '@/components/profile/ProfileReplyItem.vue'
import ProfileMovieItemLiked from '@/components/profile/ProfileMovieItemLiked.vue'
import ProfileReviewItem from '@/components/profile/ProfileReviewItem.vue'

const store = useCounterStore()
const props = defineProps({
  'user_pk':String
})

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
.like-container{
  margin-bottom:50px;
}
.container {
  margin-top: 30px;
}
</style>
