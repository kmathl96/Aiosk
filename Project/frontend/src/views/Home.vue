<template>
  <div class="home" style="margin-top:200px">
    <h1 style="font-size: 5em; padding-top:50px;">SMOOTH COFFEE</h1>
    <div class="jb" style="margin-top:200px; margin-bottom:300px; ">
    <video muted autoplay loop>
        <source :src="require(`@/assets/background/Coffee.mp4`)" type="video/mp4">
      </video>
    </div>
    <v-btn
        height="80px"
        class="home-btn"
        color="white"
        @click="moveabout"
    >주문하기</v-btn>
  </div>
</template>

<script>
export default {
  name: "Home",
  components: {},
  created() {
    this.$store.commit('reset');
  },
  methods: {
    moveabout() {
      this.$router.push({ path: "About" });
    },
  },
};
</script>
<style>
.home-btn {
  width:300px;
}
.home-btn span{
  color:#6699cc;
  font-size: 2em;
}
.jb{
  z-index:99;
   width: 100% !important; height: 500px; overflow: hidden;margin: 0px auto; position: relative; 
   opacity:0.8;
}
video{
  width:100%;
}
</style>