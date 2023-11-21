<template>
  <div>
    <ProfileSectionUser :user_pk="user_pk" />
    <hr>
    <ProfileSectionContent :user_pk="user_pk" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import ProfileSectionUser from '@/components/profile/ProfileSectionUser.vue'
import ProfileSectionContent from '@/components/profile/ProfileSectionContent.vue'

const route = useRoute()
const user_pk = ref(route.params.nickName)

</script>

<style scoped>

</style>
