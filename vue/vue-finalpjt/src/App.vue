<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'MovieView' }">영화</RouterLink> |
      <RouterLink :to="{ name: 'CommunityView' }">커뮤니티</RouterLink> |

      <!-- 로그인 한 경우 -->
      <div v-if="store.isLogin">
        <RouterLink :to="{ name: 'ProfileView' }">프로필</RouterLink> |
        <form @submit.prevent="store.logOut">
        <input type="submit" value="로그아웃">
        </form>
      </div>

      <!-- 로그인 안한 경우 -->
      <div v-else>
        <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> |
        <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
      </div>
    </nav>
  </header>

  <RouterView />
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterView, RouterLink } from 'vue-router'
const store = useCounterStore()
</script>

<style scoped>
</style>
