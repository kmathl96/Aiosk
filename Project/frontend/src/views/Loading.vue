<template>
  <div class="load">
    <div style="padding-top: 500px;">
      <!-- <video id="player" controls autoplay></video> -->
        <h3 style="margin-top:200px; margin-bottom:50px;">분석중입니다. 잠시만 기다려주세요.</h3>
        <div class="col" style=" display:flex; justify-content:center;">
            <div class="loader" ></div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
// var player = document.getElementById("player");

// var handleSuccess = function (stream) {
//   player.srcObject = stream;
// };

// navigator.mediaDevices.getUserMedia({ video: true }).then(handleSuccess);
name: "Loading",
  computed: {
    getAge() {
      return this.$store.getters.getAge
    }
  },
  watch: {
    getAge() {
      this.$router.push({ path: 'Member' })
    }
  }
};
</script>


<style>
.load {
  background-color: white;
  min-height: 1800px;
  color: #2c3e50;
}
.loader {
  border: 16px solid #3498db; /* Light grey */
  border-top: 16px solid lightcoral; /* Blue */
  border-radius: 50%;
  width: 120px;
  height: 120px;
  margin-left:0px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
