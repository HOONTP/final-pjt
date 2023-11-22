<template>
  <div>
    <!-- Community Nav 바 -->
    <CommunityNav />
    
    <h2>{{ getBoardType(store.article.board) }} 게시판</h2>
    <div v-if="store.article">
      <p>제목 : {{ store.article.title }}</p>
      <p>내용 : {{ store.article.content }}</p>
      <p>작성일 : {{ store.article.created_at }}</p>
      <p>수정일 : {{ store.article.updated_at }}</p>
    </div>

    <!-- 좋아요 버튼 -->
    <button @click="toggleLike">
      {{ store.article.like_users && store.article.like_users.includes(store.currentUser.user_id) ? '좋아요 취소' : '좋아요' }}
      {{ store.article.like_users ? store.article.like_users.length : 0 }}
    </button>
    <br>

    <!-- 내가 작성한 게시글만 수정/삭제 버튼 존재 -->
    <div v-if="store.currentUser.user_id === store.article.user">
      <!-- 수정 버튼 -->
      <RouterLink
        v-if="store.article"
        :to="{
          name: 'ArticleEditView',
          params: { id: store.article.id },
        }">
        [글 수정]
      </RouterLink>

      <!-- 삭제 버튼 -->
      <button @click="deleteArticle" v-if="store.article">[글 삭제]</button>
    </div>
    
    <!-- 댓글 section 컴포넌트 -->
    <CommentSection />
  </div>
</template>

<script setup>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommunityNav from '@/components/community/CommunityNav.vue'
import CommentSection from '@/components/community/CommentSection.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()

onMounted(() => {
  // 게시글 데이터 가져오기
  store.getArticle(route.params.id)
})

const toggleLike = () => {
  // 게시글 좋아요/좋아요 취소 요청 보내기
  axios({
    method: 'post',
    url: `${store.API_URL}/community/like/article/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      // 좋아요/좋아요 취소 요청이 성공하면 게시글 데이터를 다시 불러와 갱신
      store.getArticle(route.params.id)
    })
    .catch((err) => {
      console.error('좋아요 토글 에러:', err)
    })
}

const deleteArticle = () => {
  // 게시글 삭제
  axios({
    method: 'delete',
    url: `${store.API_URL}/community/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      // 삭제가 성공하면 홈 화면으로 이동
      router.push({ name: 'CommunityTotalView' })
      console.log('Article deleted successfully')
    })
    .catch((err) => {
      console.log(err)
    })
}

const getBoardType = (board) => {
  switch (board) {
    case 1:
      return '전체';
    case 2:
      return '인기';
    case 3:
      return '리뷰';
    case 4:
      return '자유';
    default:
      return '';
  }
}
</script>

<style scoped>
h2 {
  margin-top: 100px;  /* header의 높이 */
}
</style>