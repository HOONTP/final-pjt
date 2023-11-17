<template>
  <div id="profile-container">
    <div id="profile-picture">
      <p>[프로필 사진]</p>
    </div>
    <div id="profile-info">
      <p>[유저 닉네임]</p>
      <hr>
      <p>[한 줄 자기소개]</p>
      <br>
      <div id="profile-stats">
        <div class="stat">
          <p class="stat-value">[게시물 수]</p>
          <p>게시물</p>
        </div>
        <div class="stat">
          <p class="stat-value">[댓글 수]</p>
          <p>댓글</p>
        </div>
        <div class="stat">
          <p class="stat-value">[팔로워 수]</p>
          <p>팔로워</p>
        </div>
        <div class="stat">
          <p class="stat-value">[팔로잉 수]</p>
          <p>팔로잉</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
#profile-container {
  display: flex;
}

#profile-picture {
  width: 25%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#profile-info {
  width: 75%;
}

#profile-stats {
  display: flex;
}

.stat {
  text-align: center;
  flex: 1;
}

.stat-value {
  font-weight: bold;
}
</style>
