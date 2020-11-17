<template>
  <div class="wait" @click="goHome">
      <div class="square">
        <h1 class="mytitle animated infinite slower bounce delay-5s"  style="font-size: 6em;">AIOSK</h1>
        <p style="font-size: 2.5em; color:white;">AI기술을 이용한 <span style="color:#FFD740; font-weight:600;">스마트 </span>키오스크</p>
        <img
         src="@/assets/img/kiosk.png"
         style="margin-top:200px"
         width="600px"
        />
      </div>
  </div>
</template>

<script>
export default {
name: "Wait",
  components: {},
  // data() {
  //   return {
  //     distance:0
  //   }
  // },
  // created() {
  //   setTimeout(()=>{this.distance+=11},1000);
  // },
  // watch:{
  //     distance:function(){
  //       if(this.distance>10){
  //         this.$router.push({ path: "Home" });
  //       }
  //     }
  // },
  methods: {
   goHome() {
     this.$router.push({ path: 'Home' })
   }
  },
}
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1";
@font-face {
    font-family: 'Cafe24Ohsquare';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/Cafe24Ohsquare.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.square{
  border: 6px solid white;
  height: 1800px;
}
.mytitle{
  padding-top:300px;
  font-family: 'Cafe24Ohsquare';
  letter-spacing: 0.3em;
}
</style>