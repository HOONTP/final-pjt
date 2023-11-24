<template>
  <div class="login-container">
    <h1>HoonChul에 로그인</h1>
    <form @submit.prevent="logIn" class="login-form">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model.trim="username" required><br>

      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model.trim="password" required><br>
      
      <input type="submit" value="로그인">

      <p class="find" @click="showAlert">비밀번호 찾기</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payload)
}

const showAlert = function () {
  alert('니 비번은 나도 모름(진짜 모름)')
}

</script>

<style scoped>
.login-container {
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-form {
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

.find {
  color: rgb(130, 135, 153);
  cursor: pointer;
  text-align: center;
}
</style>
