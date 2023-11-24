<template>
  <div class="signup-container">
    <h1>HoonChul 에 회원가입</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <label for="nickname">닉네임</label>
      <input type="text" v-model.trim="nickname" required>

      <label for="username">아이디</label>
      <input type="text" v-model.trim="username" required>

      <label for="password">비밀번호</label>
      <input type="password" v-model.trim="password" required>

      <label for="password2">비밀번호 확인</label>
      <input type="password" v-model.trim="password2" required>

      <input type="submit" value="가입하기">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()
const nickname = ref(null)
const username = ref(null)
const password = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    nickname: nickname.value,
    username: username.value,
    password: password.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
.signup-container {
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.signup-form {
  margin-top: 30px;
  width: 300px;
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 15px;
  border: 1px solid #ced4da;
  border-radius: 4px;
}

input[type="submit"] {
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

input[type="submit"]:hover {
  background-color: #0056b3;
}
</style>