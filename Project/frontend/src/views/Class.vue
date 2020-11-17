<template>
  <div class="wait" @click="goWait">
      <div class="square">
        <h1 class="mytitle animated infinite slower bounce delay-5s"  style="font-size: 6em;">5반 친구들 1년 동안 정말 고생 많았어!</h1>
        <p style="font-size: 2.5em; color:white; margin-left: 50px; margin-right: 50px;">{{ message }}</p>
      </div>
  </div>
</template>

<script>
export default {
name: "Class",
  components: {},
  data() {
    return {
      message: '',
    }
  },
  created() {
    this.message = this.$store.getters.getLetter
    console.log(this.message)
  },
  // watch:{
  //     distance:function(){
  //       if(this.distance>10){
  //         this.$router.push({ path: "Home" });
  //       }
  //     }
  // },
  methods: {
    goWait() {
     this.$router.push({ path: 'Wait' })
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
  height: 1700px;
}
.mytitle{
  padding-top:400px;
  font-family: 'Cafe24Ohsquare';
  letter-spacing: 0.3em;
  margin-left: 100px;
  margin-left: 100px;
  margin-bottom: 100px;
}
</style>