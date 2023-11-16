<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" v-model.trim="username"><br>

      <label for="password1">password : </label>
      <input type="password" v-model.trim="password1"><br>

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
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
</style>