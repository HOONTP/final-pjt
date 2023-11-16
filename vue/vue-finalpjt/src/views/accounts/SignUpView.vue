<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="signUp">
      <label for="nickname">nickname : </label>
      <input type="text" v-model.trim="nickname"><br>

      <label for="username">username : </label>
      <input type="text" v-model.trim="username"><br>

      <label for="password">password : </label>
      <input type="password" v-model.trim="password"><br>

      <label for="password2">password confirmation : </label>
      <input type="password" v-model.trim="password2">

      <input type="submit" value="SingUp">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

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
</style>