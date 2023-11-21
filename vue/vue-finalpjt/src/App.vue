<template>
  <div>
    <header class="main-header">
      <nav>
        <h1>Hoon&Hochul</h1>
        <RouterLink class="nav-link" :to="{ name: 'MovieView' }">영화</RouterLink>
        <RouterLink class="nav-link" :to="{ name: 'CommunityView' }">커뮤니티</RouterLink>

        <!---------------------- 로그인 한 경우 ---------------------->
        <div v-if="store.isLogin" class="nav-right">
          <RouterLink
            v-if="store.currentUser.user_id"
            class="nav-link"
            :to="{
              name: 'ProfileView',
              params: { nickName: store.currentUser.user_id }
            }">프로필
          </RouterLink>
          <form @submit.prevent="store.logOut">
            <input type="submit" value="로그아웃" class="logout-button">
          </form>
        </div>
        <!----------------------------------------------------------->

        <!---------------------- 로그인 안한 경우 ---------------------->
        <div v-else class="nav-right">
          <RouterLink
            class="router-link-button signup"
            :to="{ name: 'SignUpView' }">
            회원가입
          </RouterLink>
          <RouterLink
            class="router-link-button"
            :to="{ name: 'LogInView' }">
            로그인
          </RouterLink>
        </div>
        <!----------------------------------------------------------->

      </nav>
    </header>
    <RouterView class="router-view" />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterView, RouterLink } from 'vue-router'

const store = useCounterStore()
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Kdam+Thmor+Pro&display=swap');

h1 {
  font-family: 'Kdam Thmor Pro', sans-serif;
  color: #722BFF;
}

.main-header {
  position: fixed;  /* header 상단 고정 */
  top: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  padding: 10px 40px;
  z-index: 1000;  /* 다른 요소 위로 올리기 위한 z-index 설정 */
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
}

.nav-link,
.logout-button,
.router-link-button {
  white-space: nowrap;  /* 화면 확대해도 글씨가 줄바꿈 되지 않음 */
}

.nav-link {
  font-size: 16px;
  margin: 0 20px;
  color: white;
  text-decoration: none;
  transition: color 0.3s ease; /* 색상 변경에 애니메이션 효과를 부여함 */
}

.nav-link:hover {
  color: #999999; /* 마우스 올리면 색 변경 */
}

.nav-right {
  display: flex;
  margin-left: auto;
  align-items: center;  /* 세로로 가운데 정렬 */
}

.logout-button,
.router-link-button {
  font-size: 16px;
  margin: 0 20px;
  padding: 5px 15px;
  color: white;
  text-decoration: none;
  background-color: transparent;  /* 배경색 투명 */
  border: 1px solid white;
  cursor: pointer;  /* 마우스 올리면 손가락 형태로 변경 */
  transition: background-color 0.3s ease;  /* 배경 색상 변경에 애니메이션 효과를 부여함 */
}

.logout-button:hover,
.router-link-button:hover {
  background-color: #555;  /* 마우스 올리면 색 변경 */
}

.router-link-button.signup {
  border-color: #e74c3c;
  background-color: #e74c3c;
}

.router-link-button.signup:hover {
  background-color: #c0392b;  /* 마우스 올리면 색 변경 */
  border-color: #c0392b;
}

.router-view {
  margin-top: 70px;  /* header의 높이 + 여백 만큼의 여백 추가 */
}
</style>

<style>
/* Style 전역 설정 */

/* Noto Sans Korean 한글 글씨체 import  */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap');

* {
  /* 기본 스타일 초기화 */
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Noto Sans KR', sans-serif;
}
</style>