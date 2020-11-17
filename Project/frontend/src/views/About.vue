<template>
  <div class="about">
    <div style="padding-top: 200px; ">
      <h1 style="font-size: 5em;">인공지능 분석</h1>
      <vue-web-cam
        ref="webcam"
        style="margin-top: 150px"
        width=700
        height=700
        autoplay
        selectFirstDevice
        @cameras="onCameras"
        @camera-change="onCameraChange"
        :deviceId='deviceId'
      />
      <v-btn
        height="120px"
        type="button"
        class="about-btn mr-3"
        style="margin-top: 200px"
        dark
        color="#6699cc"
        @click="onCapture"
      >
      분석하기
      </v-btn>
    </div>
  </div>
</template>

<script>
import { WebCam } from "vue-web-cam"
import axios from 'axios'

export default {
name: "About",
  components: {
    'vue-web-cam': WebCam
  },
  date() {
    return {
      img: null,
      deviceId: null,
      autoplay: true,
      devices: [],
      camera: null,
    }
  },
  computed: {
    device: function() {
      return this.devices.find(n => n.deviceId === this.deviceId);
    }
  },
  watch: {
    camera: function(id) {
      this.deviceId = id;
    },
    devices: function() {
      const first = this.devices[0];
      console.log(first)
      if (first) {
        this.camera = first.deviceId;
        this.deviceId = first.deviceId;
      }
    }
  },
  methods: {
    moveload() {
      this.$router.push({ path: "Loading" });
    },
    onCameras(cameras) {
      this.devices = cameras;
      console.log(this.devices)
      this.deviceId = this.devices[0].deviceId
      console.log(this.deviceId)
    },
    onCameraChange(deviceId) {
      this.deviceId = deviceId;
      this.camera = deviceId;
    },
    onCapture() {
      var image = new Image();
      image.src = this.$refs.webcam.capture()
      var fd = new FormData();
      fd.append('files', image.src)
      // for (var key of fd.entries()) {
      //   console.log(key[0] + ', ' + key[1]);
      // }
      axios.post(this.$SERVER_URL+'kiosks/detect_age/', fd,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
        .then(res => {
          console.log(res.data['answer'])
          this.$store.commit('setAge', res.data['answer']);
        })
        .catch(() => {
          this.$router.push({ path: 'About'} )
        })
      this.moveload()
    }
  }
}
</script>


<style>
.about {
  background-color: white;
  color: #6699cc;
  height: 1800px;
}
.about-btn{
  width: 300px;
  margin-bottom:100px;
}
.about-btn span{
  font-size: 3em;
}
</style>
