<template>
  <div>
    <h1>Login page</h1>
    <form @submit.prevent="logIn">
      <input type="text" id="username" v-model.trim="username"><br>

      <input type="password" id="password" v-model.trim="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { userCounterStore } from '@/stores/counter'

const store = userCounterStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payload)
}
</script>

<style>

</style>
