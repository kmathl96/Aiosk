<template>
  <div class="about">
    <div style="padding-top:100px; padding-bottom:50px; height:1000px;">
        <button class="back-btn" @click="moveTomember()" style="display:flex; justify-content:flex-start; margin-left:50px;">
            <font-awesome-icon icon="chevron-left" style="font-size:5em; "/>
            <font-awesome-icon icon="chevron-left" style="font-size:5em; "/>
        </button>
        <h1 style="font-size: 3em; margin-bottom:50px; margin-top:250px;"><span style="color:#e9967a">포장</span>과 <span style="color:#6699cc">매장 이용</span> 중 하나를 골라주세요</h1>
        <div style="display:flex; justify-content:space-around; align-content:center; margin-top:300px">
            <v-btn
            height="80px"
            type="button"
            dark
            color="#e9967a"
            style="width:400px; height:400px; font-size:2.5rem;"
            @click="nextpage()"
            >
            <div class="col">
            <font-awesome-icon icon="sign-out-alt" style="font-size:10rem; "/>
            <p>포장</p>
            </div>
            </v-btn>
            <v-btn
            height="80px"
            type="button"
            dark
            color="#6699cc"
            style="width:400px; height:400px; font-size:2.5em;"
            @click="nextpage()"
            >
            <div class="col">
            <font-awesome-icon icon="mug-hot" style="font-size:10rem; "/>
            <p>매장 이용</p>
            </div>
            </v-btn>
        </div>
    </div>
  </div>
</template>

<script>
export default {
name: "Take",
  components: {},
  data() {
        return {
            
        }
    },
  methods: {
    nextpage(){
        this.$router.push({path:'Menu'})
    },
    moveTomember(){
        this.$router.push({path:'member'})
    }
  },
  created () {
 },
};
</script>


<style>
.about {
  background-color: white;
  color: #2c3e50;
  min-height: 1800px;
}
.active{
    color:white;
    border-color:#2c3e50;
}


</style>
